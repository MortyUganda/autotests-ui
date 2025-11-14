from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_button = page.get_by_test_id('registration-page-login-button').locator('input')
    expect(registration_button).not_to_be_disabled()

    page.wait_for_timeout(5000)