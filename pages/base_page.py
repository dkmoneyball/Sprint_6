from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        """Поиск элемента с ожиданием до его появления"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        """Поиск нескольких элементов с ожиданием до их появления"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator, time=10):
        """Клик по элементу после его появления"""
        element = self.find_element(locator, time)
        element.click()

    def wait_for_element(self, locator, time=10):
        """Ожидание видимости элемента"""
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def is_element_visible(self, locator, time=10):
        """Проверка видимости элемента"""
        try:
            self.wait_for_element(locator, time)
            return True
        except:
            return False
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        """Поиск элемента с ожиданием до его появления"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        """Поиск нескольких элементов с ожиданием до их появления"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator, time=10):
        """Клик по элементу после его появления"""
        element = self.find_element(locator, time)
        element.click()

    def wait_for_element(self, locator, time=10):
        """Ожидание видимости элемента"""
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def is_element_visible(self, locator, time=10):
        """Проверка видимости элемента"""
        try:
            self.wait_for_element(locator, time)
            return True
        except:
            return False
