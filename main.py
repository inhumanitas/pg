#coding: utf-8

import sys
from PyQt4 import QtCore, QtGui

from mainWindow import Ui_MainWindow
from pg import SimpleGPG


class PGMainWindow(Ui_MainWindow, QtGui.QDialog):
    #cryptFile = QtCore.pyqtSignal()

    def __init__(self):
        super(PGMainWindow, self).__init__()
        self.encrypt_file = None

    def setupUi(self, MainWindow):
        super(PGMainWindow, self).setupUi(MainWindow)
        self._connect_signals()

    def _connect_signals(self):
        u""" Connect handlers with form elemnts"""
        self.connect(self.btnPathSelect, QtCore.SIGNAL('clicked()'), self.select_path)

    def update_info(self, message):
        #self.statusbar.showMessage(message)
        self.resultBox.setText(message)

    def update_pathView_bar(self, message):
        self.pathView.setText(message)

    def select_path(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        if filename:
            print unicode(filename)
            self.encrypt_file = unicode(filename)
            self.update_pathView_bar(filename)
            self.update_info(filename)

class PG(object):
    u""" GUI App for signing files """

    def __init__(self):
        self.ui = PGMainWindow()
        self.ui.setupUi(QMainWindow)
        self.ui.connect(self.ui.btnCrypt, QtCore.SIGNAL('clicked()'), self.crypt_file)
        self.ui.connect(self.ui.btnDecrypt, QtCore.SIGNAL('clicked()'), self.decrypt_file)
        self.ui.connect(self.ui.btnSign, QtCore.SIGNAL('clicked()'), self.sign_file)

        QMainWindow.show()
        self.pg = SimpleGPG()

    def crypt_file(self):
        print self.ui.encrypt_file
        log = u'Выберите файл для шифрования'
        if self.ui.encrypt_file:
            log = u'Начато шифрование'
            is_encrypted = self.pg.encrypt(self.ui.encrypt_file)
            if is_encrypted:
                log = u'Шифрование завершилось'
            else:
                log = u'Шифрование завершилось неудачей'

        self.ui.update_info(log)

    def decrypt_file(self):
        log = u'Нет зашифрованного файла'
        is_decrypted = self.pg.decrypt()
        if is_decrypted:
            log = u'Дешифрование завершилось'
        else:
            log = u'Дешифрование завершилось неудачей'

        self.ui.update_info(log)

    def sign_file(self):
        signed_data = self.pg.sign(self.ui.encrypt_file)
        res = u'Подпись файла завершилось неудачей'
        if signed_data:
            res = signed_data
        self.ui.update_info(res)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    QMainWindow = QtGui.QMainWindow()
    pg = PG()
    sys.exit(app.exec_())
