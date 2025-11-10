import pytest

@pytest.fixture
def setup_teardown():
    # Это часть Setup — код, который выполняется перед тестом
    print("Setup: Инициализация данных или окружения")
    test_data = {"user": "testuser", "password": "testpass"}

    # Это часть Teardown — код, который выполняется после теста
    yield test_data  # Здесь возвращаем данные для теста

    print("Teardown: Очистка данных или окружения")
    # Здесь можно закрыть соединения, удалить временные файлы и т.д.
    # Например, удалить созданные записи в базе данных, если таковые были.

def test_login(setup_teardown):
    # Здесь setup_teardown будет содержать возвращённые данные из фикстуры
    assert setup_teardown["user"] == "testuser"
    assert setup_teardown["password"] == "testpass"