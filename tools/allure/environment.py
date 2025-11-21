import platform
import sys
from config import settings
from tools.logger import get_logger

logger = get_logger('create_allure_environment_file')

def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Записываем переменные в файл
        file.write(f'\nos_info = {platform.system()} = {platform.release()}')
        file.write(f'\npython_version = {sys.version}')
        logger.info(f'Создали файл environment.properties')
