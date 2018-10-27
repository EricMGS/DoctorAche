# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doencas.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(330, 445)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/balão azul.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Label_Logo = QtWidgets.QLabel(Dialog)
        self.Label_Logo.setGeometry(QtCore.QRect(120, 210, 119, 140))
        self.Label_Logo.setLineWidth(1)
        self.Label_Logo.setText("")
        self.Label_Logo.setPixmap(QtGui.QPixmap("img/Dr.jpg"))
        self.Label_Logo.setScaledContents(False)
        self.Label_Logo.setObjectName("Label_Logo")
        self.Label_Balao = QtWidgets.QLabel(Dialog)
        self.Label_Balao.setGeometry(QtCore.QRect(0, 0, 330, 221))
        self.Label_Balao.setText("")
        self.Label_Balao.setPixmap(QtGui.QPixmap("img/balão azul.png"))
        self.Label_Balao.setObjectName("Label_Balao")
        self.Label_Doencas = QtWidgets.QLabel(Dialog)
        self.Label_Doencas.setGeometry(QtCore.QRect(80, 30, 191, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Label_Doencas.setFont(font)
        self.Label_Doencas.setStyleSheet("background-color: rgb(153, 217, 234);")
        self.Label_Doencas.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Label_Doencas.setObjectName("Label_Doencas")
        self.Btn_Ok = QtWidgets.QPushButton(Dialog)
        self.Btn_Ok.setGeometry(QtCore.QRect(10, 400, 91, 31))
        self.Btn_Ok.setObjectName("Btn_Ok")
        self.Btn_Sair = QtWidgets.QPushButton(Dialog)
        self.Btn_Sair.setGeometry(QtCore.QRect(220, 400, 91, 31))
        self.Btn_Sair.setObjectName("Btn_Sair")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Doenças possíveis"))
        self.Label_Doencas.setText(_translate("Dialog", "<html><head/><body><p>[], as possíveis doenças são:</p></body></html>"))
        self.Btn_Ok.setText(_translate("Dialog", "Ok"))
        self.Btn_Sair.setText(_translate("Dialog", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

