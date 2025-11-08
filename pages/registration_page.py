from playwright.sync_api import Page, expect
from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.ui_course_title = page.get_by_test_id('dashboard-toolbar-title-text')
        self.login_link = page.get_by_test_id('registration-page-login-link')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.registration_form = RegistrationFormComponent(page)
        
    def click_registration_button(self):
        expect(self.registration_button).to_be_visible()
        self.registration_button.click()
    
    def click_login_link(self):
        expect(self.login_link).to_be_visible()
        self.login_link.click()
    
    def check_course_title(self):
        expect(self.ui_course_title).to_be_visible()
        expect(self.ui_course_title).to_have_text('Dashboard')
    

