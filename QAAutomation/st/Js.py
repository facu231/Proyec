import time
from data.Datos2 import contastantes as Cs
class JsMetod(Cs):


    def highlight(self,xpath):    
        """Metod for highlight Elements with CSS and JavaScripts"""  
        def apply_Style(s):    
            self.driver.execute_script(Cs.ARGUMENTO,objeto,s)
        objeto = self.driver.find_element_by_xpath(xpath)
        estilo_Original = objeto.get_attribute(Cs.STYLLE)
        apply_Style(Cs.BORDE_ROJO)
        time.sleep(0.3)
        apply_Style(estilo_Original)

    
    
