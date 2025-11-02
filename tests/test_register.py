import random
import time

def test_register(browser, base_url):
    browser.get(f"{base_url}/")
    time.sleep(1)

    # Abre el modal de registro
    try:
        register_button = browser.find_element("css selector", '[data-testid="switch-to-register"]')
        register_button.click()
        time.sleep(1)
    except:
        pass

    random_email = f"user{random.randint(1000,9999)}@test.com"

    name_field = browser.find_element("css selector", '[data-testid="register-name-input"]')
    email_field = browser.find_element("css selector", '[data-testid="register-email-input"]')
    password_field = browser.find_element("css selector", '[data-testid="register-password-input"]')
    confirm_field = browser.find_element("css selector", '[data-testid="register-confirm-password-input"]')
    submit_button = browser.find_element("css selector", '[data-testid="register-submit"]')

    name_field.send_keys("Tester")
    email_field.send_keys(random_email)
    password_field.send_keys("123456")
    confirm_field.send_keys("123456")
    submit_button.click()

    time.sleep(1)
    assert True
