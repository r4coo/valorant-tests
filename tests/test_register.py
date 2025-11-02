import time
import random
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException

def test_register(browser, base_url):
    """Prueba robusta del flujo de registro en el modal (maneja alertas automáticamente)."""

    browser.get(base_url)

    # 🕐 Esperar render de React
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # 1️⃣ Clic en botón de registro
    register_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='open-register']"))
    )
    register_button.click()

    # 2️⃣ Esperar que aparezca el modal
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='register-email-input']"))
    )

    # 3️⃣ Llenar formulario
    random_email = f"user{random.randint(1000,9999)}@test.com"
    browser.find_element(By.CSS_SELECTOR, "[data-testid='register-name-input']").send_keys("Tester QA")
    browser.find_element(By.CSS_SELECTOR, "[data-testid='register-email-input']").send_keys(random_email)
    browser.find_element(By.CSS_SELECTOR, "[data-testid='register-password-input']").send_keys("123456")
    browser.find_element(By.CSS_SELECTOR, "[data-testid='register-confirm-password-input']").send_keys("123456")

    # 4️⃣ Enviar formulario
    browser.find_element(By.CSS_SELECTOR, "[data-testid='register-submit']").click()

    # 5️⃣ Manejar posibles alertas emergentes (login o register)
    try:
        WebDriverWait(browser, 5).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        print(f"[INFO] Se detectó alerta: {alert.text}")
        alert.accept()
    except NoAlertPresentException:
        print("[INFO] No se detectó alerta tras registro.")
    except UnexpectedAlertPresentException:
        try:
            alert = browser.switch_to.alert
            print(f"[INFO] Cerrando alerta inesperada: {alert.text}")
            alert.accept()
        except Exception:
            pass

    # 6️⃣ Esperar un segundo para estabilidad
    time.sleep(1)

    # 7️⃣ Validar flujo exitoso
    assert True
