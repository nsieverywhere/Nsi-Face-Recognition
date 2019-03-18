import os
import sys

from PyQt5 import QtWidgets
from capture_image2 import capture

from face import Ui_MainWindow


class MainPage(QtWidgets.QMainWindow):
    # def __init__(self):
        # super().__init__()

    def registerKeys(self):
        self.submitform.clicked.connect(self.submitForm)
        self.captureface.clicked.connect(self.startCapture)

    def startCapture(self):
        capture(self.path)

    def submitForm(self):
        self.retrieveText()
        self.createDir()
        self.writeUserData()

    def createDir(self):
        self.path = "C:/Users/user/Dev/images/%s" % self.name
        try:
            os.mkdir(self.path)
        except OSError:
            print("creation of the directory %s failed" % self.path)
        else:
            print("successfully created the directory %s " % self.path)

    def writeUserData(self):
        f = open("%s/%s.txt" % (self.path, self.name), "w")
        f.write("%s\n%s\n%s" % (self.name, self.department, self.matric))
        f.close()

    def retrieveText(self):
        self.name = self.namelineEdit.text()
        self.department = self.departmentlineEdit.text()
        self.matric = self.matriclineEdit.text()

        print("Student: %s" % str(self.name))
        print("Department Code: %s" % str(self.department))
        print("Matriculation ID: %s" % str(self.matric))


app = QtWidgets.QApplication(sys.argv)
MainWindow = MainPage()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
# MainWindow.registerKeys()
MainWindow.show()
sys.exit(app.exec_())
