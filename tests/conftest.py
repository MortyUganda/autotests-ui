import pytest  # Импортируем pytest
from playwright.sync_api import Page, Playwright, sync_playwright
from collections.abc import Generator 

@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright: Playwright) -> Generator[Page]:  # Аннотируем возвращаемое фикстурой значение
    
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)

    # Передаем страницу для использования в тесте
    yield browser.new_page()

    # Закрываем браузер после выполнения тестов
    browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state():
    with sync_playwright() as playwright:
        # Запускаем Chromium браузер в обычном режиме (не headless)
        browser = playwright.chromium.launch(headless=False)
        # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
        context = browser.new_context()
        # Открываем новую страницу в рамках контекста
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
        context.storage_state(path="browser-state.json")


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    # Передаем страницу для использования в тесте
    yield page

    # Закрываем браузер после выполнения тестов
    browser.close()
