# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 799)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 70, 421, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 396, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_vidstart = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_vidstart.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_vidstart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_vidstart.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_vidstart.setObjectName("lineEdit_vidstart")
        self.gridLayout.addWidget(self.lineEdit_vidstart, 2, 2, 1, 1)
        self.lineEdit_vid = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_vid.setAutoFillBackground(False)
        self.lineEdit_vid.setObjectName("lineEdit_vid")
        self.gridLayout.addWidget(self.lineEdit_vid, 1, 1, 1, 4)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 6)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.pushButton_vid = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_vid.setObjectName("pushButton_vid")
        self.gridLayout.addWidget(self.pushButton_vid, 1, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)
        self.lineEdit_vidend = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_vidend.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_vidend.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_vidend.setObjectName("lineEdit_vidend")
        self.gridLayout.addWidget(self.lineEdit_vidend, 2, 4, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 391, 235))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 5, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 6, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 4, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 1, 0, 1, 1)
        self.pushButton_vid4 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_vid4.setObjectName("pushButton_vid4")
        self.gridLayout_4.addWidget(self.pushButton_vid4, 4, 5, 1, 1)
        self.lineEdit_vid1 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_vid1.setObjectName("lineEdit_vid1")
        self.gridLayout_4.addWidget(self.lineEdit_vid1, 1, 1, 1, 4)
        self.pushButton_vid2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_vid2.setObjectName("pushButton_vid2")
        self.gridLayout_4.addWidget(self.pushButton_vid2, 2, 5, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 3, 0, 1, 1)
        self.pushButton_vid1 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_vid1.setObjectName("pushButton_vid1")
        self.gridLayout_4.addWidget(self.pushButton_vid1, 1, 5, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 6)
        self.lineEdit_vidsend = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_vidsend.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_vidsend.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_vidsend.setObjectName("lineEdit_vidsend")
        self.gridLayout_4.addWidget(self.lineEdit_vidsend, 6, 4, 1, 2)
        self.pushButton_vid5 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_vid5.setObjectName("pushButton_vid5")
        self.gridLayout_4.addWidget(self.pushButton_vid5, 5, 5, 1, 1)
        self.pushButton_vid3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_vid3.setObjectName("pushButton_vid3")
        self.gridLayout_4.addWidget(self.pushButton_vid3, 3, 5, 1, 1)
        self.lineEdit_vid2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_vid2.setObjectName("lineEdit_vid2")
        self.gridLayout_4.addWidget(self.lineEdit_vid2, 2, 1, 1, 4)
        self.lineEdit_vid3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_vid3.setObjectName("lineEdit_vid3")
        self.gridLayout_4.addWidget(self.lineEdit_vid3, 3, 1, 1, 4)
        self.lineEdit_vid4 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_vid4.setObjectName("lineEdit_vid4")
        self.gridLayout_4.addWidget(self.lineEdit_vid4, 4, 1, 1, 4)
        self.lineEdit_vid5 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_vid5.setObjectName("lineEdit_vid5")
        self.gridLayout_4.addWidget(self.lineEdit_vid5, 5, 1, 1, 4)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 6, 0, 1, 1)
        self.lineEdit_vidsstart = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_vidsstart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_vidsstart.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_vidsstart.setObjectName("lineEdit_vidsstart")
        self.gridLayout_4.addWidget(self.lineEdit_vidsstart, 6, 1, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_render = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_render.setGeometry(QtCore.QRect(33, 670, 451, 32))
        self.pushButton_render.setObjectName("pushButton_render")
        self.lineEdit_output = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_output.setGeometry(QtCore.QRect(121, 630, 254, 21))
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.pushButton_output = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_output.setGeometry(QtCore.QRect(377, 626, 87, 32))
        self.pushButton_output.setObjectName("pushButton_output")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(60, 630, 51, 21))
        self.label_11.setObjectName("label_11")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 360, 394, 117))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)
        self.corrGMSlider = QtWidgets.QSlider(self.layoutWidget1)
        self.corrGMSlider.setMinimum(-100)
        self.corrGMSlider.setMaximum(100)
        self.corrGMSlider.setPageStep(5)
        self.corrGMSlider.setProperty("value", 0)
        self.corrGMSlider.setOrientation(QtCore.Qt.Horizontal)
        self.corrGMSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.corrGMSlider.setTickInterval(10)
        self.corrGMSlider.setObjectName("corrGMSlider")
        self.gridLayout_2.addWidget(self.corrGMSlider, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 3)
        self.corrABSlider = QtWidgets.QSlider(self.layoutWidget1)
        self.corrABSlider.setMinimum(-100)
        self.corrABSlider.setMaximum(100)
        self.corrABSlider.setSingleStep(1)
        self.corrABSlider.setPageStep(5)
        self.corrABSlider.setProperty("value", 0)
        self.corrABSlider.setTracking(False)
        self.corrABSlider.setOrientation(QtCore.Qt.Horizontal)
        self.corrABSlider.setInvertedAppearance(False)
        self.corrABSlider.setInvertedControls(False)
        self.corrABSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.corrABSlider.setTickInterval(10)
        self.corrABSlider.setObjectName("corrABSlider")
        self.gridLayout_2.addWidget(self.corrABSlider, 2, 1, 1, 1)
        self.self = QtWidgets.QLabel(self.centralwidget)
        self.self.setGeometry(QtCore.QRect(200, 20, 59, 16))
        self.self.setObjectName("self")
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(60, 470, 398, 101))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_audio = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_audio.setObjectName("pushButton_audio")
        self.gridLayout_5.addWidget(self.pushButton_audio, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 2, 0, 1, 1)
        self.lineEdit_audio = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_audio.setObjectName("lineEdit_audio")
        self.gridLayout_5.addWidget(self.lineEdit_audio, 1, 1, 1, 3)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 3, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 2, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 1, 0, 1, 1)
        self.lineEdit_offset = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_offset.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_offset.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_offset.setObjectName("lineEdit_offset")
        self.gridLayout_5.addWidget(self.lineEdit_offset, 2, 2, 1, 2)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(61, 710, 401, 20))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 590, 259, 33))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_previewTime = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_previewTime.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_previewTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_previewTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_previewTime.setObjectName("lineEdit_previewTime")
        self.horizontalLayout_2.addWidget(self.lineEdit_previewTime)
        self.pushButton_previewFrame = QtWidgets.QPushButton(self.widget)
        self.pushButton_previewFrame.setObjectName("pushButton_previewFrame")
        self.horizontalLayout_2.addWidget(self.pushButton_previewFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_render.clicked.connect(self.renderSlot)
        self.pushButton_vid.clicked.connect(self.browseSlot_vid)
        self.pushButton_audio.clicked.connect(self.browseSlot_audio)
        self.pushButton_output.clicked.connect(self.browseSlot_output)
        self.pushButton_previewFrame.clicked.connect(self.previewFrameSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Samostrih"))
        self.lineEdit_vidstart.setText(_translate("MainWindow", "00:00:00"))
        self.lineEdit_vid.setText(_translate("MainWindow", "sample4.mp4"))
        self.label_9.setText(_translate("MainWindow", "Sermon Video:"))
        self.label_2.setText(_translate("MainWindow", "Start:"))
        self.pushButton_vid.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Video:"))
        self.label_3.setText(_translate("MainWindow", "End:"))
        self.lineEdit_vidend.setText(_translate("MainWindow", "00:00:10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "One File"))
        self.label_19.setText(_translate("MainWindow", "Video 5:"))
        self.label_16.setText(_translate("MainWindow", "End:"))
        self.label_20.setText(_translate("MainWindow", "Video 4:"))
        self.label_17.setText(_translate("MainWindow", "Video 2:"))
        self.label_15.setText(_translate("MainWindow", "Video 1:"))
        self.pushButton_vid4.setText(_translate("MainWindow", "Browse"))
        self.pushButton_vid2.setText(_translate("MainWindow", "Browse"))
        self.label_21.setText(_translate("MainWindow", "Video 3:"))
        self.pushButton_vid1.setText(_translate("MainWindow", "Browse"))
        self.label_13.setText(_translate("MainWindow", "Sermon Videos:"))
        self.lineEdit_vidsend.setText(_translate("MainWindow", "00:00:00"))
        self.pushButton_vid5.setText(_translate("MainWindow", "Browse"))
        self.pushButton_vid3.setText(_translate("MainWindow", "Browse"))
        self.label_14.setText(_translate("MainWindow", "Start:"))
        self.lineEdit_vidsstart.setText(_translate("MainWindow", "00:00:00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Multiple Files"))
        self.pushButton_render.setText(_translate("MainWindow", "Render"))
        self.lineEdit_output.setText(_translate("MainWindow", "output.mp4"))
        self.pushButton_output.setText(_translate("MainWindow", "Browse"))
        self.label_11.setText(_translate("MainWindow", "Output:"))
        self.label_5.setText(_translate("MainWindow", "Green"))
        self.label_4.setText(_translate("MainWindow", "Blue (cold)"))
        self.label_7.setText(_translate("MainWindow", "Magenta"))
        self.label_6.setText(_translate("MainWindow", "Amber (warm)"))
        self.label_8.setText(_translate("MainWindow", "White Balance:"))
        self.self.setText(_translate("MainWindow", "I have:"))
        self.pushButton_audio.setText(_translate("MainWindow", "Browse"))
        self.label_18.setText(_translate("MainWindow", "Sermon Audio: (optional)"))
        self.label_22.setText(_translate("MainWindow", "Offset:"))
        self.label_23.setText(_translate("MainWindow", "Audio:"))
        self.lineEdit_offset.setText(_translate("MainWindow", "00:00:00"))
        self.label_10.setText(_translate("MainWindow", "Progress:"))
        self.lineEdit_previewTime.setText(_translate("MainWindow", "00:00:30"))
        self.pushButton_previewFrame.setText(_translate("MainWindow", "Preview Frame"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
