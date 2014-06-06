# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Jun  5 22:02:59 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(580, 505)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnPathSelect = QtGui.QPushButton(self.centralwidget)
        self.btnPathSelect.setObjectName(_fromUtf8("btnPathSelect"))
        self.horizontalLayout.addWidget(self.btnPathSelect)
        self.pathView = QtGui.QLineEdit(self.centralwidget)
        self.pathView.setEnabled(False)
        self.pathView.setObjectName(_fromUtf8("pathView"))
        self.horizontalLayout.addWidget(self.pathView)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.resultBox = QtGui.QTextEdit(self.centralwidget)
        self.resultBox.setEnabled(False)
        self.resultBox.setObjectName(_fromUtf8("resultBox"))
        self.verticalLayout.addWidget(self.resultBox)
        self.btnCrypt = QtGui.QPushButton(self.centralwidget)
        self.btnCrypt.setObjectName(_fromUtf8("btnCrypt"))
        self.verticalLayout.addWidget(self.btnCrypt)
        self.btnDecrypt = QtGui.QPushButton(self.centralwidget)
        self.btnDecrypt.setObjectName(_fromUtf8("btnDecrypt"))
        self.verticalLayout.addWidget(self.btnDecrypt)
        self.btnSign = QtGui.QPushButton(self.centralwidget)
        self.btnSign.setObjectName(_fromUtf8("btnSign"))
        self.verticalLayout.addWidget(self.btnSign)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnPathSelect.setText(_translate("MainWindow", "Выбор файла", None))
        self.btnCrypt.setText(_translate("MainWindow", "Шифровать", None))
        self.btnDecrypt.setText(_translate("MainWindow", "Дешифровать", None))
        self.btnSign.setText(_translate("MainWindow", "Подписать", None))

