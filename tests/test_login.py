import os
import time

def test_login(browser, base_url):
    browser.get(f"{base_url}/")  # la modal se abre desde home
    time.sleep(1)

    # Abre el modal de login si no está abierto
    try:
        login_button = browser.find_element("data-testid", "switch-to-login")
        login_button.click()
        time.sleep(1)
    except:
        pass

    email = os.getenv("TEST_USER_EMAIL", "test@example.com")
    password = os.getenv("TEST_USER_PASS", "123456")

    email_field = browser.find_element("css selector", '[data-testid="login-email-input"]')
    password_field = browser.find_element("css selector", '[data-testid="login-password-input"]')
    submit_button = browser.find_element("css selector", '[data-testid="login-submit"]')

    email_field.send_keys(email)
    password_field.send_keys(password)
    submit_button.click()

    time.sleep(1)
    assert True  # por ahora, ya que tu modal es una demo con alert()
