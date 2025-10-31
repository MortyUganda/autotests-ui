import pytest
# ---------------------------------Фикстуры помогают--------------------------------
# Инициализировать окружение.
# Подготавливать тестовые данные.
# Устанавливать соединения с базами данных.
# Изолировать тесты от изменений в глобальном состоянии.

# --------------------Фикстуры обладают следующими свойствами---------------------------

# Повторное использование: можно определить фикстуру один раз и использовать её в разных тестах.
# Изоляция тестов: фикстуры изолируют состояние тестов, избегая побочных эффектов между ними.
# Гибкость: фикстуры могут быть настроены для работы с разными уровнями выполнения (например, на уровне теста, модуля или сессии).

# !!!!!!!!!!!!!!Определение фикстуры!!!!!!!!!!!!!!!!!!
@pytest.fixture
def sample_fixture():
    return {"key": "value"}

# !!!!!!!!!!!!!!Использование фикстуры в тесте!!!!!!!!!!!!!!!!!!
def test_using_fixture(sample_fixture):
    assert sample_fixture["key"] == "value"


@pytest.fixture(autouse=True)                                               
def send_analytics():
    print('[AUTOUSE] Отправляем данные в сервис аналитики') #для выполнения действий автоматически


@pytest.fixture(scope='function') # фикстура function может инициализировать, открывать браузер на каждый автотест
def function_browser():
    print("[function] Данная фикстура будет запущена на каждый автотест")

@pytest.fixture(scope="class") #фикстура class можем готовить данные перед тестом, передавать их, а после завершения удалять
def class_browser():
    print("[CLASS] Данная фикстура будет запущена на каждый тестовый класс") 

@pytest.fixture(scope="module")
def module_browser():
    print("[MODULE] Данная фикстура будет запущена на каждый модуль python") #

@pytest.fixture(scope="session")
def session_browser():
    print("[SESSION] Данная фикстура будет запущена один раз на всю тестовую сессию") #можем заранее подготавливать данные, не внутри, а прямо в фикстуре


class TestUserFLow:
    def test_user_can_login(self, session_browser, function_browser, class_browser):
        ...
    def test_user_can_create_course(self, class_browser):
        ...


class TestAccountFlow:
    def test_user_account(self, module_browser, class_browser):
        ...