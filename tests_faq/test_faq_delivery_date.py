from pages.faq_page import FaqPage
from locators.locators import FaqPageLocators

def test_faq_delivery_date(setup):
    """Тест на проверку отображения ответа на вопрос о доставке"""
    faq_page = FaqPage(setup)
    faq_page.load()  # Загружаем страницу

    # Прокручиваем страницу и кликаем по вопросу про дату доставки
    faq_page.click_question(FaqPageLocators.QUESTION_DELIVERY_DATE)

    # Проверяем, что ответ отображается
    assert faq_page.is_answer_displayed(FaqPageLocators.ANSWER_DELIVERY_DATE,
                                        "Допустим, вы оформляете заказ на 8 мая. Мы привози"), \
        "Ответ на вопрос о доставке не отображается или неверный"
