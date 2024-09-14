import sys
import os
import sqlite3
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



def get_next_code():
    # Conectar a la base de datos
    conn = sqlite3.connect('../Utils/code_db.sqlite')
    cursor = conn.cursor()

    # Seleccionar el primer código no utilizado
    cursor.execute('SELECT id, code FROM codes WHERE used = 0 LIMIT 1')
    result = cursor.fetchone()

    if result:
        code_id, code = result
        # Marcar el código como utilizado
        cursor.execute('UPDATE codes SET used = 1 WHERE id = ?', (code_id,))
        conn.commit()
        conn.close()
        return code
    else:
        conn.close()
        raise Exception("No hay más códigos disponibles.")

@pytest.fixture(scope="function")
def code_setup():
    # Obtener el siguiente código disponible
    code = get_next_code()
    yield code


    