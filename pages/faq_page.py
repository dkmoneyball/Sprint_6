from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import FaqPageLocators


class FaqPage:
    """Класс для работы со страницей FAQ, использующий локаторы из locators.py"""

    def __init__(self, driver):
        self.driver = driver

    def click_question(self):
        """Метод для клика по вопросу 'Сколько это стоит? И как оплатить?'"""
        question_element = self.driver.find_element(*FaqPageLocators.QUESTION_COST_PAYMENT)
        question_element.click()

    def is_answer_displayed(self):
        """Метод для проверки, отображается ли ответ"""
        wait = WebDriverWait(self.driver, 10)
        answer_element = wait.until(EC.visibility_of_element_located(FaqPageLocators.ANSWER_COST_PAYMENT))
        return "Сутки — 400 рублей. Оплата курьеру — наличными или картой." in answer_element.text
