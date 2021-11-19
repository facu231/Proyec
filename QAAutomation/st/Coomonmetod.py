from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

class metodosComunes:

    def encontrarXpath(self,xpath):
        self.driver.find_element_by_xpath(xpath)

    def escribirLebel(self,xpath,text):
        self.encontrarXpath(xpath).send_keys(text)   


    def _xpath_element(self, XPATH):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
            elements = self.driver.find_element_by_xpath(XPATH)
            print(u"Esperar_Elemento: Se visualizo el elemento " + XPATH)
            return True
        except TimeoutException:
            print(u"Esperar_Elemento: No presente " + XPATH)
        except NoSuchElementException:
            print(u"Esperar_Elemento: No presente " + XPATH)






    