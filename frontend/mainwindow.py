# -*- coding: utf-8 -*-

import sys
sys.path.append('../backend/')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QCompleter, QComboBox
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

class Ui_MainWindow(object):
    def button_add_clicked(self):
        if self.cmb_entrada.currentText() in doctor.lista_sintomas:
            items = [str(self.list_sintomas.item(i).text()) for i in range(self.list_sintomas.count())] 
            if self.cmb_entrada.currentText() not in items:
                self.list_sintomas.addItem(self.cmb_entrada.currentText())

    def button_del_clicked(self):
    	item = self.list_sintomas.takeItem(self.list_sintomas.currentRow())
    	item = None

    def button_ok_clicked(self):
        items = [str(self.list_sintomas.item(i).text()) for i in range(self.list_sintomas.count())]
        doctor.get_sintomas(items)
        doctor.provaveis()
        res = doctor.resultado
        texto = ("Você provavelmente está com:\n")
        if len(res) == 0:
            texto = 'Nenhum sintoma foi informado'
        else:
            texto += '1- ' + res[0] + '\n'
            if len(res) >= 2:
                texto += '2- ' + res[1] + '\n'
            if len(res) >= 3:
                texto += '3- ' + res[2] + '\n'

        self.lbl_res.setText(texto)


    def setupUi(self, MainWindow):
        icone = QtGui.QIcon()
        icone.addPixmap(QtGui.QPixmap('Dr.jpg'))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 510)               
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(icone)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setWindowTitle("DoctorAche")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)

        self.btn_ok = QtWidgets.QPushButton(MainWindow)
        self.btn_ok.setGeometry(QtCore.QRect(590, 390, 60, 60))
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.btn_ok.setText("OK")
        self.btn_ok.clicked.connect(self.button_ok_clicked)

        self.btn_add = QtWidgets.QPushButton(MainWindow)
        self.btn_add.setGeometry(QtCore.QRect(280, 40, 60, 60))
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.btn_add.setText("ADD")
        self.btn_add.clicked.connect(self.button_add_clicked)

        self.btn_del = QtWidgets.QPushButton(MainWindow)
        self.btn_del.setGeometry(QtCore.QRect(350, 390, 60, 60))
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")
        self.btn_del.setText("DEL")
        self.btn_del.clicked.connect(self.button_del_clicked)

        self.cmb_entrada = ExtendedComboBox(MainWindow)
        self.cmb_entrada.setGeometry(QtCore.QRect(30, 40, 240, 60))
        self.cmb_entrada.setObjectName("cmb_entrada")
        self.cmb_entrada.addItems(doctor.lista_sintomas)
        self.cmb_entrada.setCurrentText("")

        self.list_sintomas = QtWidgets.QListWidget(MainWindow)
        self.list_sintomas.setGeometry(QtCore.QRect(350, 40, 300, 320))
        self.list_sintomas.setObjectName("list_sintomas")

        self.lbl_res = QtWidgets.QLabel(MainWindow)
        self.lbl_res.setGeometry(QtCore.QRect(30, 200, 240, 60))
        self.lbl_res.setObjectName("lbl_res")
        self.lbl_res.setText("")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    doctor = DA()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())