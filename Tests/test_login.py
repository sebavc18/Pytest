import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.common_imports import *
from Pages.conftest import *


def test_login(login_setup):
    driver = login_setup
    

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//img[@id='main-logo']"))
        )
        # Asegúrate de que la imagen esté visible
        img_element = driver.find_element(By.XPATH, "//img[@id='main-logo']")
        assert img_element.is_displayed(), "El logo principal no está visible en la página"
        print("Logo visible")

    finally:
        # No cierres el navegador en esta prueba para depuración

        pass

    f = Global_Functions(driver)
    f.button("//a[@class='floating-action-button']")
    f.select_field(By.XPATH,"//select[@class='primary-tumor form-control custom-select']", "Pulmón")
    f.select_field(By.XPATH, "//select[@class='sample-type form-control custom-select']", "Sólida")
    f.select_field(By.XPATH, "//select[@class='form-control custom-select']", "Adenocarcinoma")
    f.scrollintoview(By.XPATH, "(//h6[@class='m-0 p-0 d-inline-block'])[5]")
    f.button("//label[contains(.,'KRAS G12C')]")
    f.select_field(By.XPATH, "(//select[@id='pharmaSelect'])[1]", "Takeda")
    f.select_field(By.XPATH, "(//select[@id='pharmaSelect'])[2]", "Merck Sharp & Dohme")
    f.select_field(By.XPATH, "(//select[@id='pharmaSelect'])[4]", "Biomakers")
    f.text_field(By.XPATH, "//input[@class='uppercase large-form-text form-control']", "ASXNFJ23")
    f.text_field(By.XPATH, "//input[@class='uppercase large-form-text form-control is-invalid']", "AR-0039")
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH,"//div[contains(@class,'invalid-feedback')]")))
    allure.attach(driver.get_screenshot_as_png(), name="habilitacion formulario", attachment_type=AttachmentType.PNG)
    f.scrollintoview(By.XPATH, "(//input[contains(@name,'code')])[2]")
    f.text_field(By.XPATH,"//input[contains(@placeholder,'Nombres del paciente')]", "Prueba")
    f.text_field(By.XPATH, "//input[contains(@placeholder,'Apellidos del paciente')]", "Pytest10")
    f.button("(//div[contains(@class,'meta')])[2]")
    f.scrollintoview(By.XPATH, "(//input[@type='text'])[5]")
    f.text_field(By.XPATH, "(//input[@type='number'])[1]", 12)
    f.select_field(By.XPATH,"//select[contains(@class,'form-control custom-select border-danger')]", "Agosto")
    f.text_field(By.XPATH, "(//input[@type='number'])[2]", 1945)
    f.text_field(By.XPATH, "//input[contains(@placeholder,'Documento Nacional De Identidad/Cédula De Identidad/RUT')]", 1649785)
    f.text_field(By.XPATH, "//input[@placeholder='Busque una cobertura médica']", "OSDE")
    f.button("(//div[contains(.,'OSDE')])[14]")
    f.select_field(By.XPATH, "//select[contains(@id,'gender-select')]", "Masculino")
    f.button("//button[contains(@value,'12_to_15')]")
    f.select_field(By.XPATH, "//select[@id='ethinicity-select']", "Asian")
    f.text_field(By.XPATH, "//input[contains(@name,'telephone')]", "19734682" + Keys.TAB + "mail@mail" + Keys.TAB + "B")
    f.text_field(By.XPATH, "//input[contains(@placeholder,'Localidad')]", "Localidad")
    f.scrollintoview(By.XPATH, "//button[contains(.,'No fumador')]")
    f.button("(//button[@class='btn btn-primary btn-white'][contains(.,'No')])[2]")
    f.select_field(By.XPATH, "//select[contains(@id,'diagnosis_stage-select')]", "IA")
    f.select_field(By.XPATH,"(//select[@class='form-control custom-select'])[6]", "Resectable NSCLC")
    f.select_field(By.XPATH, "(//select[@class='form-control custom-select'])[7]", "IA")
    f.scrollintoview(By.XPATH, "(//li[contains(@class,'px-3 py-1')])[3]")
    f.button("//span[@class='custom-control-description'][contains(.,'Incluí en el sobre todos los items mencionados en la lista.')]")
    f.button("(//div[contains(.,'Consentimiento Informado General')])[11]")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Enviar Pedido')]")))
    allure.attach(driver.get_screenshot_as_png(), name="boton habilitado", attachment_type=AttachmentType.PNG)
    f.button("//button[contains(.,'Enviar Pedido')]")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[contains(.,'Cerrar')]")))
    allure.attach(driver.get_screenshot_as_png(), name="pop up", attachment_type=AttachmentType.PNG)
    f.pop_up(By.XPATH, "//button[contains(.,'Cerrar')]")
    allure.attach(driver.get_screenshot_as_png(), name="pedido realizado", attachment_type=AttachmentType.PNG)







    
    
    

    



    time.sleep(2)


  