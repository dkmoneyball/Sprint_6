import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    """Инициализация WebDriver и его закрытие после теста"""
    driver = webdriver.Firefox()  # Инициализация Firefox WebDriver
    driver.maximize_window()
    yield driver  # Возвращаем драйвер для использования в тестах
    driver.quit()  # Закрываем браузер после теста
