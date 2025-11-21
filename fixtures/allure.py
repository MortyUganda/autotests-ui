import pytest

from tools.allure.environment import create_allure_environment_file
from tools.logger import get_logger
logger = get_logger('save_allure_environment_file')

@pytest.fixture(scope='session', autouse=True)
def save_allure_environment_file():
    # До начала автотестов ничего не делаем
    yield  # Запукаются автотесты...
    logger.info(f'Создаем файл environment.properties')
    # После завершения автотестов создаем файл environment.properties
    create_allure_environment_file()