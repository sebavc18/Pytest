import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.common_imports import *

class Global_Functions():
    def __init__(self,driver) -> None:
        self.driver = driver
        pass

    def text_field(self,tipo,locator, text):
        driver = self.driver
        field = driver.find_element(tipo, locator)
        field.send_keys(text)
    
    def select_field(self, tipo, locator, option):
        driver = self.driver
        field = driver.find_element(tipo, locator)
        fields = Select(field)
        fields.select_by_visible_text(option)

    def button(self, xpath ):
        driver = self.driver
        btn = driver.find_element(By.XPATH, xpath)
        btn.click()

    def scrollintoview(self, tipo, locator):
        driver = self.driver
        element = driver.find_element(tipo, locator)
        val = self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def text_field(self, tipo, locator, text):
        driver = self.driver
        field = driver.find_element(tipo, locator)
        field.send_keys(text)

    def select_value(self, tipo, locator, option):
        driver = self.driver
        field = driver.find_element(tipo, locator)
        fields = Select(field)
        fields.select_by_value(option)

    def pop_up(self, tipo, locator):
        driver = self.driver
        try:
            boton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((tipo, locator)))
            boton.click()

        except TimeoutError as e:
            print(e)
   

