from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input
from elements.text import Text


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.email_input = Input(page, 'registration-form-email-input', 'Email_')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')
        self.username_input = Input(page, 'registration-form-username-input', 'Username_')

    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.username_input.fill(username)

    def check_visible(self, email:str, username: str, password:str):
        self.email_input.check_have_value(email)
        self.password_input.check_have_value(password)
        self.username_input.check_have_value(username)