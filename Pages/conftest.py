import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.common_imports import *
# Cargar el archivo .env desde la carpeta Utils
load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'Utils', '.env'))

load_dotenv()

@pytest.fixture(scope="function")
def login_setup():
    url = os.getenv('LOGIN_URL')
    username = os.getenv('LOGIN_USERNAME')
    contraseña = os.getenv('LOGIN_PASSWORD')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.maximize_window()
    email = driver.find_element(By.XPATH, "//input[@type='email']")
    email.send_keys(username)
    password = driver.find_element(By.XPATH, "//input[@type='password']")
    password.send_keys(contraseña)
    boton = driver.find_element(By.XPATH, "//button[@type='submit']")
    boton.click()
    yield driver

    