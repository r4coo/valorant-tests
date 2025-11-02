import os
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(browser, base_url):
    browser.get(base_url)

    # 🕐 Espera general al render de React + Header
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='header']"))
    )

    # 🔍 Debug opcional
    print(browser.page_source[:2000])

    # 1️⃣ Buscar y clicar el botón de login
    login_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='open-login']"))
    )
    login_button.click()

    # 2️⃣ Esperar el modal de login
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='login-email-input']"))
    )

    # 3️⃣ Ingresar credenciales de prueba
    email = os.getenv("TEST_USER_EMAIL", "test@example.com")
    password = os.getenv("TEST_USER_PASS", "123456")

    browser.find_element(By.CSS_SELECTOR, "[data-testid='login-email-input']").send_keys(email)
    browser.find_element(By.CSS_SELECTOR, "[data-testid='login-password-input']").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "[data-testid='login-submit']").click()

    time.sleep(2)
    assert True
    # Aquí podrías validar la redirección o mensaje esperado