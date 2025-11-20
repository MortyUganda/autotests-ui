# config.py
from enum import Enum
from genericpath import exists

import allure
from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, Field, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict  # type: ignore


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath
    allure_results_dir: DirectoryPath

    # Добавили метод get_base_url
    def get_base_url(self) -> str:
        return f"{self.app_url}/"
    
    @classmethod
    def initialize(cls):
        # Указываем пути
        videos_dir = DirectoryPath("./videos") # type: ignore
        tracing_dir = DirectoryPath("./tracing") # type: ignore
        browser_state_file = FilePath("browser-state.json") # type: ignore
        allure_results_dir = DirectoryPath("./allure_results") # type: ignore
         
        # Создаем директории, если они не существуют
        allure_results_dir.mkdir(exist_ok=True)
        videos_dir.mkdir(exist_ok=True)  # Если директория сещуствует, то игнорируем ошибку
        tracing_dir.mkdir(exist_ok=True)
        # Создаем файл состояния браузера, если его нет
        browser_state_file.touch(exist_ok=True) # Если файл сещуствует, то игнорируем ошибку
        
        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file,
    )


settings = Settings.initialize()
