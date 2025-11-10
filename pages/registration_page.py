from playwright.sync_api import Page
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)

        self.login_link = Link(page, 'registration-page-login-link', 'Login')
        self.ui_course_title = Text(page, 'dashboard-toolbar-title-text', 'UI title')
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')
        
    def click_registration_button(self):
        self.registration_button.check_visible()
        self.registration_button.click()
    
    def click_login_link(self):
        self.login_link.check_visible()
        self.login_link.click()
    
    def check_course_title(self):
        self.ui_course_title.check_visible()
        self.ui_course_title.check_have_text('Dashboard')

