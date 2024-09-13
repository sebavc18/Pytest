# Proyecto de Automatización de Pruebas con Pytest y Selenium
Versión: 0.1.0
Este proyecto implementa pruebas automatizadas para pagina web utilizando Selenium como herramienta de automatización del navegador y Pytest como framework de pruebas.

## Requisitos del Proyecto

Para ejecutar este proyecto, necesitas instalar las siguientes dependencias. Puedes hacerlo utilizando `pip` y el archivo `requirements.txt`.

### Dependencias Principales

- **pytest**: Herramienta para ejecutar pruebas.
- **selenium**: Biblioteca para automatización de navegadores web.
- **webdriver-manager**: Facilita la gestión de controladores para los navegadores.
- **pytest-cov**: Genera informes de cobertura de código.
- **pytest-html**: Genera informes HTML de las pruebas.
- **pytest-metadata**: Agrega metadatos a los informes de prueba.
- **pytest-soft-assertions**: Permite usar aserciones suaves.
- **parameterized**: Permite realizar pruebas con múltiples conjuntos de datos.
- **python-dotenv**: Carga variables de entorno desde un archivo `.env`.
- **requests**: Realiza solicitudes HTTP.

### Dependencias Adicionales (Opcionales)

- **colorama**: Mejora el formato de salida en la terminal.
- **coverage**: Otra herramienta para medir la cobertura de pruebas.
- **allure-pytest**: Genera informes de pruebas en formato Allure.
- **allure-python-commons**: Dependencia común para Allure.
- **pytest-xdist**: Ejecuta pruebas en paralelo.
- **Faker**: Genera datos ficticios para pruebas.
- **pytest-rerunfailures**: Reintenta automáticamente las pruebas fallidas.




## Estructura del Proyecto

- `Pages/`: Contiene las clases que representan las páginas web (Page Objects).
- `Tests/`: Contiene los archivos de prueba.
- `Utils/`: Contiene funciones utilitarias y configuraciones.
- `requirements.txt`: Archivo con las dependencias del proyecto.
- 'Reports/' Si utilizas Allure reports aqui se generaran los archivos temporales para el report

## Configuración de WebDriver

Este proyecto utiliza `webdriver-manager` para manejar las versiones de los controladores del navegador. No es necesario descargar manualmente ChromeDriver o GeckoDriver.

## Generar reportes
pytest --html=report.html

## Notas Adicionales

- Para ejecutar solo un test específico:
  ```bash
  pytest -k "nombre_del_test"
  ```

- Para generar un reporte Allure (si lo estás utilizando):
  ```bash
  pytest --alluredir=reportes/
  allure serve reportes/
  ```

### Instalación

Puedes instalar todas las dependencias utilizando el archivo `requirements.txt`. Asegúrate de estar en el entorno virtual adecuado y ejecuta el siguiente comando:

```bash
pip install -r requirements.txt