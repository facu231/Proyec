import unittest
from selenium import webdriver
from path.Path import direciones
from st.stPruebas import stPruebas
class Teste_case(unittest.TestCase,stPruebas):
    def setUp(self):
        self.driver = webdriver.Chrome(direciones.Chromedriver)
        
    def test_prueba(self):
        try:
            self.navegacion_en_google(direciones.facebook)
            self.seleccionar_IpertextoFC()
            self.captura()
            self.introducir_correo()
            self.introducir_password()
            self.driver.quit()
        except Exception as Q:
            print(f"error de tipo {Q}" )


if __name__ == "__main__":
    unittest.main()




