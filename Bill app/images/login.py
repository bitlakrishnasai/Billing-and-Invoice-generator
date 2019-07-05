# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Krishna Sai\Desktop\Coding\Python\Bill app\images\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# from SJ_front import *
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_BillApp(object):
    usernam = ["abc", "bcd"]
    def setupUi(self, BillApp):
        BillApp.setObjectName("BillApp")
        BillApp.setWindowModality(QtCore.Qt.NonModal)
        BillApp.resize(800, 557)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        BillApp.setFont(font)
        BillApp.setFocusPolicy(QtCore.Qt.NoFocus)
        BillApp.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(BillApp)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 121, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(25)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 280, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-1, 9, 801, 551))
        self.frame_2.setStyleSheet("background-color: rgb(221, 81, 69);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(100, 80, 701, 471))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("\n"
"background-color: rgb(126, 126, 126);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(150, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 100, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setMaxLength(25)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.frame_2.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        BillApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(BillApp)
        QtCore.QMetaObject.connectSlotsByName(BillApp)
        self.pushButton.clicked.connect(self.login)

    def retranslateUi(self, BillApp):
        _translate = QtCore.QCoreApplication.translate
        BillApp.setWindowTitle(_translate("BillApp", "Bill App"))
        self.lineEdit.setPlaceholderText(_translate("BillApp", "id"))
        self.pushButton.setText(_translate("BillApp", "Login"))
        self.label.setText(_translate("BillApp", "User"))
        self.label_2.setText(_translate("BillApp", "Password"))
        self.lineEdit_3.setPlaceholderText(_translate("BillApp", "pass"))

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_3.text()
        Ui_BillApp.usernam[0] = username

        if username == "u" and password == "":
            print("working")
            import SJ_front
        else:
            print("not working")

        print(Ui_BillApp.usernam[0])
        print("hi")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BillApp = QtWidgets.QMainWindow()
    ui = Ui_BillApp()
    ui.setupUi(BillApp)
    BillApp.show()
    sys.exit(app.exec_())


