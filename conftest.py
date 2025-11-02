import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    """
    Crea una nueva instancia de Chrome para cada test.
    Esto evita que el estado, cookies o alertas del test anterior
    afecten al siguiente (por ejemplo, el login previo).
    """

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")   # Ejecución sin interfaz gráfica
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)

    yield driver

    # 🧹 Asegura que el navegador se cierre al final del test
    try:
        driver.quit()
    except Exception:
        pass


@pytest.fixture(scope="session")
def base_url():
    """URL base del proyecto desplegado en Vercel."""
    return "https://front-end-valorant-store-ev-2.vercel.app/"
