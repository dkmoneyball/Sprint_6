import pytest
from locators.locators import FaqPageLocators
from pages.faq_page import FaqPage

@pytest.mark.parametrize("question_locator, answer_locator, expected_text", [
    (FaqPageLocators.QUESTION_COST_PAYMENT, FaqPageLocators.ANSWER_COST_PAYMENT, "Сутки — 400 рублей. Оплата курьеру — наличными или"),
    (FaqPageLocators.QUESTION_SCOOTER_AVAILABILITY, FaqPageLocators.ANSWER_SCOOTER_AVAILABILITY, "Пока что у нас так: один заказ — один самокат."),
    (FaqPageLocators.QUESTION_DELIVERY_DATE, FaqPageLocators.ANSWER_DELIVERY_DATE, "Допустим, вы оформляете заказ на 8 мая."),
    (FaqPageLocators.QUESTION_START_RENTAL, FaqPageLocators.ANSWER_START_RENTAL, "Только начиная с завтрашнего дня."),
    (FaqPageLocators.QUESTION_PHONE_CONTACT, FaqPageLocators.ANSWER_PHONE_CONTACT, "Пока что нет! Но если что-то срочное"),
    (FaqPageLocators.QUESTION_SCOOTER_CHARGE, FaqPageLocators.ANSWER_SCOOTER_CHARGE, "Самокат приезжает к вам с полной зарядкой."),
    (FaqPageLocators.QUESTION_CANCEL_ORDER, FaqPageLocators.ANSWER_CANCEL_ORDER, "Да, пока самокат не привезли."),
    (FaqPageLocators.QUESTION_DELIVERY_TO_MOSCOW, FaqPageLocators.ANSWER_DELIVERY_TO_MOSCOW, "Да, обязательно. Всем самокатов!")
])
def test_faq_answers(setup, question_locator, answer_locator, expected_text):
    """Тест для проверки отображения ответов на вопросы FAQ"""
    faq_page = FaqPage(setup)

    faq_page.open()

    # Кликаем на вопрос
    faq_page.click_question(question_locator)

    # Проверяем, что ответ отображается и содержит ожидаемый текст
    assert faq_page.is_answer_displayed(answer_locator, expected_text), f"Ответ для {question_locator} не отображается или текст не совпадает!"
