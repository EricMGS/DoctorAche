# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(569, 307)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BalaoFala.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Btn_Comecar = QtWidgets.QPushButton(Dialog)
        self.Btn_Comecar.setGeometry(QtCore.QRect(310, 262, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Btn_Comecar.setFont(font)
        self.Btn_Comecar.setObjectName("Btn_Comecar")
        self.Btn_Sair = QtWidgets.QPushButton(Dialog)
        self.Btn_Sair.setGeometry(QtCore.QRect(400, 262, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Btn_Sair.setFont(font)
        self.Btn_Sair.setObjectName("Btn_Sair")
        self.Label_LogoDrAche = QtWidgets.QLabel(Dialog)
        self.Label_LogoDrAche.setGeometry(QtCore.QRect(50, 160, 119, 140))
        self.Label_LogoDrAche.setLineWidth(1)
        self.Label_LogoDrAche.setText("")
        self.Label_LogoDrAche.setPixmap(QtGui.QPixmap("img/Dr.jpg"))
        self.Label_LogoDrAche.setScaledContents(False)
        self.Label_LogoDrAche.setObjectName("Label_LogoDrAche")
        self.Label_Balao = QtWidgets.QLabel(Dialog)
        self.Label_Balao.setGeometry(QtCore.QRect(30, -10, 231, 171))
        self.Label_Balao.setText("")
        self.Label_Balao.setPixmap(QtGui.QPixmap("img/balão verde.png"))
        self.Label_Balao.setObjectName("Label_Balao")
        self.Label_Texto = QtWidgets.QLabel(Dialog)
        self.Label_Texto.setGeometry(QtCore.QRect(70, 20, 141, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Label_Texto.setFont(font)
        self.Label_Texto.setAutoFillBackground(False)
        self.Label_Texto.setStyleSheet("background-color: rgb(181, 230, 29);")
        self.Label_Texto.setObjectName("Label_Texto")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 30, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Txt_Nome = QtWidgets.QTextEdit(Dialog)
        self.Txt_Nome.setGeometry(QtCore.QRect(350, 30, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Txt_Nome.setFont(font)
        self.Txt_Nome.setObjectName("Txt_Nome")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(310, 90, 201, 101))
        self.groupBox.setObjectName("groupBox")
        self.Op_Masculino = QtWidgets.QRadioButton(self.groupBox)
        self.Op_Masculino.setGeometry(QtCore.QRect(10, 20, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Op_Masculino.setFont(font)
        self.Op_Masculino.setObjectName("Op_Masculino")
        self.Op_Feminino = QtWidgets.QRadioButton(self.groupBox)
        self.Op_Feminino.setGeometry(QtCore.QRect(10, 60, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Op_Feminino.setFont(font)
        self.Op_Feminino.setObjectName("Op_Feminino")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cadastro"))
        self.Btn_Comecar.setText(_translate("Dialog", "Começar"))
        self.Btn_Sair.setText(_translate("Dialog", "Sair"))
        self.Label_Texto.setText(_translate("Dialog", "Olá, para começar\n"
"preencha o formulário."))
        self.label_3.setText(_translate("Dialog", "Nome:"))
        self.groupBox.setTitle(_translate("Dialog", "Sexo"))
        self.Op_Masculino.setText(_translate("Dialog", "Masculino"))
        self.Op_Feminino.setText(_translate("Dialog", "Feminino"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

