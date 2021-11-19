from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from st.Js import JsMetod
import time
from path.Path import direciones
from xpath.ploc import *
from data.Datos import *


class stPruebas(JsMetod):

    def navegacion_en_google(self,direccion):
        self.driver.get(direciones.Url)
        self.driver.find_element_by_xpath(xpath.input_navegacion).send_keys( direccion ,Keys.ENTER)
        time.sleep(2)

    def seleccionar_IpertextoFC(self):
        self.driver.find_element_by_xpath(xpath.Ipertexto).click()
        self.highlight(xpath.Ipertexto)
        time.sleep(2)

    def introducir_correo(self):
        self.driver.find_element_by_xpath(xpath.direccion).send_keys(Info.Gmail)
        self.captura
        time.sleep(2)

    def introducir_password(self):  
        self.driver.find_element_by_xpath(xpath.inputPasword).send_keys(Info.clave)
        time.sleep(2)
        self.captura()


    def captura(self):
        if self.driver.get_screenshot_as_file(direciones.direccion):
            print ("se tomo la captura de pantalla")
        else:
            print("No se saco la captura")

