# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('../backend/')
from DoctorAche import DoctorAche as DA

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 510)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BalaoFala.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(390, 390, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.cmb_entrada = QtWidgets.QComboBox(Dialog)
        self.cmb_entrada.setGeometry(QtCore.QRect(50, 40, 241, 61))
        self.cmb_entrada.setObjectName("cmb_entrada")
        self.list_sintomas = QtWidgets.QListView(Dialog)
        self.list_sintomas.setGeometry(QtCore.QRect(350, 30, 291, 321))
        self.list_sintomas.setObjectName("list_sintomas")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "teste"))
        self.btn_ok.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    doctor = DA()

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

