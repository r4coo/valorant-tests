import random

def test_register(browser, base_url):
    browser.get(f"{base_url}/register")
    random_email = f"user{random.randint(1000,9999)}@test.com"

    email_field = browser.find_element("name", "email")
    password_field = browser.find_element("name", "password")
    register_button = browser.find_element("tag name", "button")

    email_field.send_keys(random_email)
    password_field.send_keys("123456")
    register_button.click()

    assert "welcome" in browser.current_url or "login" in browser.current_url
