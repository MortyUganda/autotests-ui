from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.focus()

    for char in 'username@email.ru':
        page.keyboard.type(char, delay=100)

    username_email_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_email_input.focus()
    
    for char in 'user':
        page.keyboard.type(char, delay=100)
    
    password_email_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_email_input.focus()
    
    for char in '1234567890':
        page.keyboard.type(char, delay=100)

    page.keyboard.press("ControlOrMeta+A")
    page.wait_for_timeout(1000)
    page.keyboard.press("Delete")
    
    page.wait_for_timeout(3000)