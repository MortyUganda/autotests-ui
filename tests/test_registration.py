import pytest
from pages.registration_page import RegistrationPage


@pytest.mark.registration 
@pytest.mark.regression
@pytest.mark.parametrize(
        'email, username, password, ', 
        [
        ("user@gmail.com", '123', "password"),
        ('123@mail.ru', '123', '123'),
        ]
)

def test_successful_registration(registration_page: RegistrationPage, email: str, username: str, password: str):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.fill_registration_form_input(email=email, password=password, username=username)
        registration_page.click_registration_button()
        registration_page.check_course_title()