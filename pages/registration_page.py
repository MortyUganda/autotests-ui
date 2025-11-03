from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.ui_course_title = page.get_by_test_id('dashboard-toolbar-title-text')
        self.email_form_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_form_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_form_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.login_link = page.get_by_test_id('registration-page-login-link')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form_input(self, email: str, password: str, username: str):
        self.email_form_input.fill(email)
        expect(self.email_form_input).to_have_value(email)

        self.username_form_input.fill(username)
        expect(self.username_form_input).to_have_value(username)
        
        self.password_form_input.fill(password)
        expect(self.password_form_input).to_have_value(password)
    
    def click_registration_button(self):
        expect(self.registration_button).to_be_visible()
        self.registration_button.click()
    
    def click_login_link(self):
        expect(self.login_link).to_be_visible()
        self.login_link.click()
    
    def check_course_title(self):
        expect(self.ui_course_title).to_be_visible()
        expect(self.ui_course_title).to_have_text('Dashboard')
    

