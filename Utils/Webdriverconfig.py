#Import
import time



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Config_chrome:
    def Set_Up(self):
        # Configura el controlador Chrome con webdriver_manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)
        return driver
