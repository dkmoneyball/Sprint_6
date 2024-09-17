from pages.faq_page import FaqPage
from locators.locators import FaqPageLocators

def test_faq_delivery_to_moscow(setup):
    """Тест на проверку отображения ответа на вопрос о доставке в Москву"""
    faq_page = FaqPage(setup)
    faq_page.load()  # Загружаем страницу

    # Прокручиваем страницу и кликаем по вопросу про доставку в Москву
    faq_page.click_question(FaqPageLocators.QUESTION_DELIVERY_TO_MOSCOW)

    # Проверяем, что ответ отображается
    assert faq_page.is_answer_displayed(FaqPageLocators.ANSWER_DELIVERY_TO_MOSCOW,
                                        "Да, обязательно. Всем самокатов! И Москве, и Моско"), \
        "Ответ на вопрос о доставке в Москву не отображается или неверный"
