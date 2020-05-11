from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot

from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import openpyxl as excel
from openpyxl import load_workbook
from openpyxl import Workbook
from datetime import datetime
import time
import os
import json
import numpy as np

class Parseador (QThread):

    countChanged = pyqtSignal(int)
    
    def __init__(self, nav, parent = None):
      super (Parseador, self).__init__(parent)
      self.nav = nav
      self.driver = self.nav.abrir_Cr()
      self.username = os.environ['username']
      self.directorio = r"C:\Users\{}\Documents".format(self.username)
      self.fecha_hora = self.fecha_y_hora()
      self.hoy = datetime.now().date()
      #definimos donde guardo datos del parseo, hoy es excel mañana bbdd
      self.ruta_parseo = r"{}\parseos\{}_mensajes_{}.xlsx".format(self.directorio, self.origen, self.fecha_hora)
      self.excel_parseo = self.crea_archivo_parseo()
      self.val = 0

    def run(self):
      while 1:
        val = self.emitidos()
        self.countChanged.emit(val)

    def fecha_y_hora (self):
      hoy = str(datetime.now().date())
      ahora = str(datetime.now().time())
      ahora = ahora.replace(":","")
      ahora = ahora[:6]
      fecha_hora = hoy + ahora
      return fecha_hora
    
    def crea_archivo_parseo (self):
      try:
        os.stat(self.directorio + "\parseos")
      except:
        os.mkdir(self.directorio + "\parseos")

      wb=Workbook()
      wb.save(self.ruta_parseo)
      self.excel_parseo = load_workbook(self.ruta_parseo)
      self.parseo = self.excel_parseo.active
      self.parseo['A1'] = 'titleColumn'
      self.parseo['B1'] = 'peli'
      self.parseo['C1'] = 'Contacto'
      self.parseo['D1'] = 'Mensajes'
      self.excel_parseo.save(self.ruta_parseo)
      return self.excel_parseo

  
    def guarda_archivo_parseo(self):
      self.excel_parseo.save(self.ruta_parseo)

    def emitidos(self):
      return self.val
    
    @pyqtSlot()
    def parsea (self):
      #self.ui.plainTextEdit.appendPlainText("Contactos definitivos: " + str(total))
      #self.progressBar_pars.setMaximum(total)
      for index, row in enumerate(self.contactos_definitivos, start=1): 
        self.val = index
        self.emitidos()
        contacto = row[0]
        #self.ui.plainTextEdit.appendPlainText(contacto + " " + str(index) + "/" + str(total))
        #self.progressBar_pars.setValue (index)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        pass
            