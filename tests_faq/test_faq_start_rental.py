from pages.faq_page import FaqPage
from locators.locators import FaqPageLocators

def test_faq_start_rental(setup):
    """Тест на проверку отображения ответа на вопрос о начале аренды"""
    faq_page = FaqPage(setup)
    faq_page.load()  # Загружаем страницу

    # Прокручиваем страницу и кликаем по вопросу про начало аренды
    faq_page.click_question(FaqPageLocators.QUESTION_START_RENTAL)

    # Проверяем, что ответ отображается
    assert faq_page.is_answer_displayed(FaqPageLocators.ANSWER_START_RENTAL,
                                        "Только начиная с завтрашнего дня. Но скоро станем"), \
        "Ответ на вопрос о начале аренды не отображается или неверный"
