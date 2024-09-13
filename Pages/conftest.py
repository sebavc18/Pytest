import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.common_imports import *

@pytest.fixture(scope="function")
def login_setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("https://pluton-stg.biomakers.net/")
    driver.maximize_window()
    email = driver.find_element(By.XPATH, "//input[@type='email']")
    email.send_keys("svillalba@biomakers.net")
    password = driver.find_element(By.XPATH, "//input[@type='password']")
    password.send_keys("Shannaly14")
    boton = driver.find_element(By.XPATH, "//button[@type='submit']")
    boton.click()
    yield driver

    