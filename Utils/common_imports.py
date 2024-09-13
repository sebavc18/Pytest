#Import
import time
import pytest
import allure





from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Utils.Webdriverconfig import Config_chrome
from Pages.Funciones import Global_Functions
from allure_commons.types import AttachmentType

# Ajuste del path para facilitar imports
