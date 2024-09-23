from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.locators import FaqPageLocators

class FaqPage(BasePage):
    """Класс для работы со страницей FAQ"""

    URL = "https://qa-scooter.praktikum-services.ru/"

    def open(self):
        """Открыть страницу FAQ"""
        self.open_page(self.URL)

    def click_question(self, question_locator):
        """Кликаем на вопрос, предварительно прокрутив страницу вниз"""
        self.scroll_to_bottom()  # Прокрутка до самого низа страницы
        question_element = self.find_element(question_locator)

        # Используем JavaScript для клика
        self.driver.execute_script("arguments[0].click();", question_element)

    def is_answer_displayed(self, answer_locator, expected_text):
        """Проверяем, что ответ отображается и содержит ожидаемый текст"""
        return self.is_text_present(answer_locator, expected_text)
