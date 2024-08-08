from PyQt5.QtCore import QThread, pyqtSignal

from data.db_hendler import login, register


class CheckThread(QThread):
    mysignal = pyqtSignal(str)

    def thr_login(self, name, passw):
        login(name, passw, self.mysignal)

    def thr_register(self, name, passw):
        register(name, passw, self.mysignal)



