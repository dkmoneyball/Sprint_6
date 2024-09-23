import sys
import os
import pytest
from selenium import webdriver

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def setup():
    driver = webdriver.Firefox()  # Используем Firefox
    driver.maximize_window()
    yield driver
    driver.quit()  # Закрываем браузер после завершения теста
