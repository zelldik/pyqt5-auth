from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QDialog

from data import CheckThread


# Проверка провильности ввода
def check_input(funct):
    def wrapper(self):
        for line_edit in self.base_line_edit:
            if len(line_edit.text()) == 0:
                return
        funct(self)

    return wrapper


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('assets/MainWindow.ui', self)
        self.pushButton.clicked.connect(self.reg)
        self.pushButton_2.clicked.connect(self.auth)
        self.base_line_edit = [self.lineEdit, self.lineEdit_2]
        self.check_db = CheckThread()
        self.check_db.my_signal.connect(self.signal_handler)

    # обработчик сигналов
    def signal_handler(self, value):
        QMessageBox.about(self, 'Оповещение', value)

    @check_input
    def auth(self):
        name = self.lineEdit.text()
        passw = self.lineEdit_2.text()
        self.check_db.thr_login(name, passw)

    @check_input
    def reg(self):
        name = self.lineEdit.text()
        passw = self.lineEdit_2.text()
        self.check_db.thr_register(name, passw)
