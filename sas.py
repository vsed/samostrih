from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot, QThread
from mainwindow import Ui_MainWindow
import sys, threading, time
from model import Model
from saslib import rgb_correction, render, preview


class qrender(QtCore.QObject):
    newData = QtCore.pyqtSignal(object)

    def __init__(self, parent=None, name="Sermon Title", name_fontsize=90, verse="Verse", intro_length=3,
                 overlay=2, input_video="sample.mp4", video_start="00:00:00", video_end="00:00:10",
                 amber_blue=0, green_magenta=0):
        QtCore.QObject.__init__(self)
        # self.parent = parent
        # self.sizey = sizey
        # self.rangey = rangey
        # self.delay = delay
        # self.mutex = QMutex()
        # self.y = [0 for i in range(sizey)]
        self.input_video = input_video
        self.video_start = video_start
        self.video_end = video_end
        self.amber_blue=amber_blue
        self.green_magenta=green_magenta

    def doRender(self):
        render(input_video=self.input_video, video_start=self.video_start, video_end=self.video_end,
               amber_blue=self.amber_blue, green_magenta=self.green_magenta)


class MainWindowUIClass(Ui_MainWindow):
    def __init__(self):
        '''Initialize the super class
        '''
        super().__init__()
        self.model = Model()

    def setupUi(self, MW):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi(MW)

        # close the lower part of the splitter to hide the
        # debug window under normal operations


    def refreshAll(self):
        '''
        Updates the widgets whenever an interaction happens.
        Typically some interaction takes place, the UI responds,
        and informs the model of the change.  Then this method
        is called, pulling from the model information that is
        updated in the GUI.
        '''
        self.lineEdit_vid.setText(self.model.getFileNameVid())
        self.lineEdit_audio.setText(self.model.getFileNameAudio())
        self.lineEdit_output.setText(self.model.getFileNameOutput())

    # slot
    def returnPressedSlot(self):
        ''' Called when the user enters a string in the line edit and
        presses the ENTER key.
        '''
        fileName = self.lineEdit.text()
        if self.model.isValid(fileName):
            self.model.setFileName(self.lineEdit.text())
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name!\n" + fileName)
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                 | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit.setText("")
            self.refreshAll()
            self.debugPrint("Invalid file specified: " + fileName)

    # slot
    def browseSlot_vid(self):
        ''' Called when the user presses the Browse button
        '''
        # self.debugPrint( "Browse button pressed" )
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options)
        if fileName:
            self.model.setFileNameVid(fileName)
            self.refreshAll()


    def browseSlot_audio(self):
        ''' Called when the user presses the Browse button
        '''
        # self.debugPrint( "Browse button pressed" )
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options)
        if fileName:
            self.model.setFileNameAudio(fileName)
            self.refreshAll()


    def browseSlot_output(self):
        ''' Called when the user presses the Browse button
        '''
        # self.debugPrint( "Browse button pressed" )
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options)
        if fileName:
            self.model.setFileNameOutput(fileName)
            self.refreshAll()

    def previewFrameSlot(self):
        input_video = self.lineEdit_vid.text()
        video_start = self.lineEdit_previewTime.text()
        amber_blue = self.corrABSlider.value()
        green_magenta = self.corrGMSlider.value()
        preview(input_video=input_video, video_start=video_start, amber_blue=amber_blue, green_magenta=green_magenta)

    def renderSlot(self):
        input_video = self.lineEdit_vid.text()
        video_start = self.lineEdit_vidstart.text()
        video_end = self.lineEdit_vidend.text()
        amber_blue = self.corrABSlider.value()
        green_magenta = self.corrGMSlider.value()
        self.thread1 = QThread()
        self.x = qrender(input_video=input_video, video_start=video_start, video_end=video_end, amber_blue=amber_blue, green_magenta=green_magenta)
        self.x.moveToThread(self.thread1)
        self.thread1.started.connect(self.x.doRender)
        self.thread1.start()
        self.thread1.quit()

def main():
    """
    This is the MAIN ENTRY POINT of our application.  The code at the end
    of the mainwindow.py script will not be executed, since this script is now
    our main program.   We have simply copied the code from mainwindow.py here
    since it was automatically generated by '''pyuic5'''.

    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


main()
