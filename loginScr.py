# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginScr.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginScr(object):
    def setupUi(self, loginScr):
        loginScr.setObjectName("loginScr")
        loginScr.resize(651, 346)
        loginScr.setMinimumSize(QtCore.QSize(484, 294))
        loginScr.setMaximumSize(QtCore.QSize(805, 346))
        loginScr.setAccessibleName("")
        self.gridLayout_3 = QtWidgets.QGridLayout(loginScr)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblLogin = QtWidgets.QLabel(loginScr)
        self.lblLogin.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setUnderline(True)
        self.lblLogin.setFont(font)
        self.lblLogin.setTextFormat(QtCore.Qt.AutoText)
        self.lblLogin.setObjectName("lblLogin")
        self.gridLayout_3.addWidget(self.lblLogin, 0, 0, 1, 1)
        self.loginScrGrid = QtWidgets.QGridLayout()
        self.loginScrGrid.setObjectName("loginScrGrid")
        self.credentialLayout = QtWidgets.QGridLayout()
        self.credentialLayout.setObjectName("credentialLayout")
        self.userLayout = QtWidgets.QVBoxLayout()
        self.userLayout.setObjectName("userLayout")
        self.lblUsr = QtWidgets.QLabel(loginScr)
        self.lblUsr.setMinimumSize(QtCore.QSize(0, 0))
        self.lblUsr.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblUsr.setFont(font)
        self.lblUsr.setTextFormat(QtCore.Qt.AutoText)
        self.lblUsr.setObjectName("lblUsr")
        self.userLayout.addWidget(self.lblUsr)
        self.editboxUsr = QtWidgets.QLineEdit(loginScr)
        self.editboxUsr.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editboxUsr.setFont(font)
        self.editboxUsr.setObjectName("editboxUsr")
        self.userLayout.addWidget(self.editboxUsr)
        self.credentialLayout.addLayout(self.userLayout, 0, 0, 1, 1)
        self.passLayout = QtWidgets.QVBoxLayout()
        self.passLayout.setObjectName("passLayout")
        self.lblPass = QtWidgets.QLabel(loginScr)
        self.lblPass.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblPass.setFont(font)
        self.lblPass.setTextFormat(QtCore.Qt.AutoText)
        self.lblPass.setObjectName("lblPass")
        self.passLayout.addWidget(self.lblPass)
        self.editboxPass = QtWidgets.QLineEdit(loginScr)
        self.editboxPass.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editboxPass.setFont(font)
        self.editboxPass.setObjectName("editboxPass")
        self.passLayout.addWidget(self.editboxPass)
        self.credentialLayout.addLayout(self.passLayout, 1, 0, 1, 1)
        self.loginScrGrid.addLayout(self.credentialLayout, 0, 0, 1, 1)
        self.btnLayout = QtWidgets.QHBoxLayout()
        self.btnLayout.setContentsMargins(-1, 20, -1, -1)
        self.btnLayout.setSpacing(65)
        self.btnLayout.setObjectName("btnLayout")
        self.btnClear = QtWidgets.QPushButton(loginScr)
        self.btnClear.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnClear.setFont(font)
        self.btnClear.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.btnClear.setObjectName("btnClear")
        self.btnLayout.addWidget(self.btnClear)
        self.btnConfim = QtWidgets.QPushButton(loginScr)
        self.btnConfim.setMinimumSize(QtCore.QSize(10, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnConfim.setFont(font)
        self.btnConfim.setAutoFillBackground(False)
        self.btnConfim.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.btnConfim.setObjectName("btnConfim")
        self.btnLayout.addWidget(self.btnConfim)
        self.btnLayout.setStretch(0, 1)
        self.btnLayout.setStretch(1, 2)
        self.loginScrGrid.addLayout(self.btnLayout, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.loginScrGrid, 1, 0, 1, 1)

        self.retranslateUi(loginScr)
        self.btnClear.clicked.connect(self.editboxUsr.clear) # type: ignore
        self.btnClear.clicked.connect(self.editboxPass.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(loginScr)

    def retranslateUi(self, loginScr):
        _translate = QtCore.QCoreApplication.translate
        loginScr.setWindowTitle(_translate("loginScr", "Login"))
        self.lblLogin.setAccessibleName(_translate("loginScr", "sddvsdv"))
        self.lblLogin.setText(_translate("loginScr", "Food Hub - Login:"))
        self.lblUsr.setText(_translate("loginScr", "Username:"))
        self.lblPass.setText(_translate("loginScr", "Password:"))
        self.btnClear.setText(_translate("loginScr", "Cancel"))
        self.btnConfim.setText(_translate("loginScr", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginScr = QtWidgets.QWidget()
    ui = Ui_loginScr()
    ui.setupUi(loginScr)
    loginScr.show()
    sys.exit(app.exec_())
