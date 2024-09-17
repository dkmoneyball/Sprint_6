from pages.faq_page import FaqPage
from locators.locators import FaqPageLocators

def test_faq_cancel_order(setup):
    """Тест на проверку отображения ответа на вопрос об отмене заказа"""
    faq_page = FaqPage(setup)
    faq_page.load()  # Загружаем страницу

    # Прокручиваем страницу и кликаем по вопросу про отмену заказа
    faq_page.click_question(FaqPageLocators.QUESTION_CANCEL_ORDER)

    # Проверяем, что ответ отображается
    assert faq_page.is_answer_displayed(FaqPageLocators.ANSWER_CANCEL_ORDER,
                                        "Да, пока самокат не привезли. Штрафа не будет, объ"), \
        "Ответ на вопрос об отмене заказа не отображается или неверный"
