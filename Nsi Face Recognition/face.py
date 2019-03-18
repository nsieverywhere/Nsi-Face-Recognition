
import numpy as np
import os
import cv2
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from capture_image2 import capture


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 504)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 461, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(140, 180, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(120, 40, 240, 61))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(90, 310, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(90, 230, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.submitform = QtWidgets.QPushButton(self.tab)
        self.submitform.setGeometry(QtCore.QRect(190, 350, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.submitform.setFont(font)
        self.submitform.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitform.setObjectName("submitform")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(90, 270, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(170, 100, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.captureface = QtWidgets.QPushButton(self.tab)
        self.captureface.setGeometry(QtCore.QRect(290, 350, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.captureface.setFont(font)
        self.captureface.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.captureface.setObjectName("captureface")
        self.matriclineEdit = QtWidgets.QLineEdit(self.tab)
        self.matriclineEdit.setGeometry(QtCore.QRect(180, 310, 191, 20))
        self.matriclineEdit.setObjectName("matriclineEdit")
        self.namelineEdit = QtWidgets.QLineEdit(self.tab)
        self.namelineEdit.setGeometry(QtCore.QRect(180, 230, 191, 20))
        self.namelineEdit.setObjectName("namelineEdit")
        self.departmentlineEdit = QtWidgets.QLineEdit(self.tab)
        self.departmentlineEdit.setGeometry(QtCore.QRect(180, 270, 191, 20))
        self.departmentlineEdit.setObjectName("departmentlineEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.takeattendance = QtWidgets.QPushButton(self.tab_2)
        self.takeattendance.setGeometry(QtCore.QRect(160, 380, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.takeattendance.setFont(font)
        self.takeattendance.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.takeattendance.setObjectName("takeattendance")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableView = QtWidgets.QTableView(self.tab_3)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 461, 441))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Register Student"))
        self.label_3.setText(_translate("MainWindow", "Nsieverywhere"))
        self.label_6.setText(_translate("MainWindow", "Matric No:"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.submitform.setText(_translate("MainWindow", "Submit Form"))
        self.label_2.setText(_translate("MainWindow", "Department:"))
        self.label_4.setText(_translate("MainWindow", "FACE RECOGNITION"))
        self.captureface.setText(_translate("MainWindow", "Capture Face"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "Register "))
        self.takeattendance.setText(
            _translate("MainWindow", "Take Attendance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "Take Attendance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_3), _translate("MainWindow", "View List"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_4), _translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
