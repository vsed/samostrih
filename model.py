class Model:
    def __init__(self):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.fileNameVid = None
        self.fileNameAudio = None
        self.fileNameOutput = None

    def isValid(self, fileName):
        '''
        returns True if the file exists and can be
        opened.  Returns False otherwise.
        '''
        try:
            file = open(fileName, 'r')
            file.close()
            return True
        except:
            return False

    def setFileNameVid(self, fileNameVid):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        self.fileNameVid = fileNameVid

    def setFileNameAudio(self, fileNameAudio):
        '''
        sets the member fileNameAudio to the value of the argument
        if the file exists.  Otherwise resets both the fileNameAudio
        and file contents members.
        '''
        self.fileNameAudio = fileNameAudio

    def setFileNameOutput(self, fileNameOutput):
        '''
        sets the member fileNameOutput to the value of the argument
        if the file exists.  Otherwise resets both the fileNameOutput
        and file contents members.
        '''
        self.fileNameOutput = fileNameOutput


    def getFileNameVid(self):
        '''
        Returns the NameVid of the file NameVid member.
        '''
        return self.fileNameVid


    def getFileNameAudio(self):
        '''
        Returns the NameAudio of the file NameAudio member.
        '''
        return self.fileNameAudio


    def getFileNameOutput(self):
        '''
        Returns the NameOutput of the file NameOutput member.
        '''
        return self.fileNameOutput

    def getFileContents(self):
        '''
        Returns the contents of the file if it exists, otherwise
        returns an empty string.
        '''
        return self.fileContents

    def writeDoc(self, text):
        '''
        Writes the string that is passed as argument to a
        a text file with name equal to the name of the file
        that was read, plus the suffix ".bak"
        '''
        if self.isValid(self.fileName):
            fileName = self.fileName + ".bak"
            file = open(fileName, 'w')
            file.write(text)
            file.close()
