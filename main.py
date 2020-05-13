from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from chrome import Cr
from pars import Parseador
import Ui_window_lite

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
        nav = Cr()
        self.parseo = Parseador(nav)
        #apertura de hilos
        self.parseo.countChanged.connect(self.updateProgressBar)
        self.parseo.start()
        self.parseo.parsea()
        nav.driver.close()

def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        ui = MainUiClass()
        apli = Aplicacion(ui)
        ui.show()
        ui.btn_parsear.clicked.connect(apli.ejecutar_parseo)
        app.exec_()

if __name__ == "__main__":
    main()