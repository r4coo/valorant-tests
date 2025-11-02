import os

def test_login(browser, base_url):
    browser.get(f"{base_url}/login")
    email = os.getenv("TEST_USER_EMAIL")
    password = os.getenv("TEST_USER_PASS")

    email_field = browser.find_element("name", "email")
    password_field = browser.find_element("name", "password")
    login_button = browser.find_element("tag name", "button")

    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()

    assert "dashboard" in browser.current_url or "home" in browser.current_url
