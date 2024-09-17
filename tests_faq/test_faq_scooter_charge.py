from pages.faq_page import FaqPage
from locators.locators import FaqPageLocators

def test_faq_scooter_charge(setup):
    """Тест на проверку отображения ответа на вопрос о зарядке самоката"""
    faq_page = FaqPage(setup)
    faq_page.load()  # Загружаем страницу

    # Прокручиваем страницу и кликаем по вопросу про зарядку самоката
    faq_page.click_question(FaqPageLocators.QUESTION_SCOOTER_CHARGE)

    # Проверяем, что ответ отображается
    assert faq_page.is_answer_displayed(FaqPageLocators.ANSWER_SCOOTER_CHARGE,
                                        "Самокат приезжает к вам с полной зарядкой. Этого х"), \
        "Ответ на вопрос о зарядке самоката не отображается или неверный"
