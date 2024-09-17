from pages.faq_page import FaqPage
from locators.locators import FaqPageLocators

def test_faq_scooter_availability(setup):
    """Тест на проверку отображения ответа на вопрос 'Сколько самокатов можно заказать?'"""
    faq_page = FaqPage(setup)
    faq_page.load()  # Загружаем страницу

    # Прокручиваем страницу и кликаем по вопросу про доступность самокатов
    faq_page.click_question(FaqPageLocators.QUESTION_SCOOTER_AVAILABILITY)

    # Проверяем, что ответ отображается
    assert faq_page.is_answer_displayed(FaqPageLocators.ANSWER_SCOOTER_AVAILABILITY,
                                        "Пока что у нас так: один заказ — один самокат. Есл"), \
        "Ответ на вопрос не отображается или неверный"
