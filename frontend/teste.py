# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QCompleter, QComboBox
sys.path.append('../backend/')
from DoctorAche import DoctorAche as DA
from spellChecker import spellChecker as SC

class ExtendedComboBox(QComboBox):
    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)

    # on selection of an item from the completer, select the corresponding item from combobox 
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))

    # on model change, update the models of the filter and completer as well 
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)


    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)  

class Ui_Dialog(object):
    def button_add_clicked(self):
        if self.cmb_entrada.currentText() in doctor.lista_sintomas:
            items = [str(self.list_sintomas.item(i).text()) for i in range(self.list_sintomas.count())] 
            if self.cmb_entrada.currentText() not in items:
                self.list_sintomas.addItem(self.cmb_entrada.currentText())

    def button_del_clicked(self):
    	item = self.list_sintomas.takeItem(self.list_sintomas.currentRow())
    	item = None

    def button_ok_clicked(self):
    	pass

    def setupUi(self, Dialog):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/BalaoFala.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)

        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 510)               
        Dialog.setFont(font)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)

        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(590, 390, 60, 60))
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.btn_ok.clicked.connect(self.button_ok_clicked)

        self.btn_add = QtWidgets.QPushButton(Dialog)
        self.btn_add.setGeometry(QtCore.QRect(280, 40, 60, 60))
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.btn_add.clicked.connect(self.button_add_clicked)

        self.btn_del = QtWidgets.QPushButton(Dialog)
        self.btn_del.setGeometry(QtCore.QRect(350, 390, 60, 60))
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")
        self.btn_del.clicked.connect(self.button_del_clicked)

        self.cmb_entrada = ExtendedComboBox(Dialog)
        self.cmb_entrada.setGeometry(QtCore.QRect(30, 40, 240, 60))
        self.cmb_entrada.setObjectName("cmb_entrada")
        self.cmb_entrada.addItems(doctor.lista_sintomas)
        self.cmb_entrada.setCurrentText("")

        self.list_sintomas = QtWidgets.QListWidget(Dialog)
        self.list_sintomas.setGeometry(QtCore.QRect(350, 40, 300, 320))
        self.list_sintomas.setObjectName("list_sintomas")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "teste"))
        self.btn_ok.setText(_translate("Dialog", "OK"))
        self.btn_add.setText(_translate("Dialog", "ADD"))
        self.btn_del.setText(_translate("Dialog", "DEL"))


if __name__ == "__main__":
    doctor = DA()

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())