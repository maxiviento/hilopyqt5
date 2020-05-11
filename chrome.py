from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class Cr (object):  
    def abrir_Cr(self):
      """Metodo para abrir navegador"""
      directorio = os.path.dirname(__file__)
      self.driver = webdriver.Chrome(directorio + "\\chromedriver.exe")
      self.wait = WebDriverWait(self.driver, 2)
      self.driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

      landing_class = 'ipc-button__text'
      ipc=""
      while bool(ipc) == False:
        try:
          ipc = self.driver.find_element_by_class_name(landing_class)
        except NoSuchElementException:
          pass
      return self.driver
