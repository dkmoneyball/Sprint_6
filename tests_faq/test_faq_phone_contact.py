from pages.faq_page import FaqPage
from locators.locators import FaqPageLocators

def test_faq_phone_contact(setup):
    """Тест на проверку отображения ответа на вопрос о телефонном контакте"""
    faq_page = FaqPage(setup)
    faq_page.load()  # Загружаем страницу

    # Прокручиваем страницу и кликаем по вопросу про телефонный контакт
    faq_page.click_question(FaqPageLocators.QUESTION_PHONE_CONTACT)

    # Проверяем, что ответ отображается
    assert faq_page.is_answer_displayed(FaqPageLocators.ANSWER_PHONE_CONTACT,
                                        "Пока что нет! Но если что-то срочное — всегда можн"), \
        "Ответ на вопрос о телефонном контакте не отображается или неверный"
