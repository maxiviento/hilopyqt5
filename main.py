from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from chrome import Cr
from pars import Parseador
import Ui_window_lite
import time


class ThreadClass(QtCore.QThread):
    
    change_value = QtCore.pyqtSignal(int)

    def __init__(self, parent = None):
        super(ThreadClass, self).__init__(parent)
    
    def run(self):
        self.nav = Cr()
        self.parseo = Parseador(self.nav, self.change_value)
        self.parseo.parsea()
        self.nav.driver.close()

class MainUiClass (QtWidgets.QMainWindow, Ui_window_lite.Ui_MainWindow):
    def __init__(self, parent=None):
        super (MainUiClass, self).__init__(parent)
        self.setupUi(self)

class Aplicacion(object):
    def __init__(self, ui):
        self.ui = ui
        
    def updateProgressBar(self, val):
        self.ui.progressBar_pars.setValue(val)

    
    def ejecutar_parseo(self):        
        self.thread = ThreadClass()
        self.thread.change_value.connect(self.updateProgressBar)
        self.thread.start()


def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        ui = MainUiClass()
        apli = Aplicacion(ui)
        ui.show()
        ui.btn_parsear.clicked.connect(apli.ejecutar_parseo)
        #ui.btn_parsear.clicked.connect(apli.startProgressBar)
        app.exec_()

if __name__ == "__main__":
    main()