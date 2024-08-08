from PyQt5.QtCore import QThread, pyqtSignal

from data.db_handler import login, register


class CheckThread(QThread):
    my_signal = pyqtSignal(str)

    def thr_login(self, name, passw):
        login(name, passw, self.my_signal)

    def thr_register(self, name, passw):
        register(name, passw, self.my_signal)
