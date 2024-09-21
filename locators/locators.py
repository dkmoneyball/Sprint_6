from selenium.webdriver.common.by import By

class FaqPageLocators:
    QUESTION_COST_PAYMENT = (By.XPATH, "//div[@id='accordion__heading-0']")
    ANSWER_COST_PAYMENT = (By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или')]")

    QUESTION_SCOOTER_AVAILABILITY = (By.XPATH, "//div[@id='accordion__heading-1']")
    ANSWER_SCOOTER_AVAILABILITY = (By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Есл')]")

    QUESTION_DELIVERY_DATE = (By.XPATH, "//div[@id='accordion__heading-2']")
    ANSWER_DELIVERY_DATE = (By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привози')]")

    QUESTION_START_RENTAL = (By.XPATH, "//div[@id='accordion__heading-3']")
    ANSWER_START_RENTAL = (By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем')]")

    QUESTION_PHONE_CONTACT = (By.XPATH, "//div[@id='accordion__heading-4']")
    ANSWER_PHONE_CONTACT = (By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можн')]")

    QUESTION_SCOOTER_CHARGE = (By.XPATH, "//div[@id='accordion__heading-5']")
    ANSWER_SCOOTER_CHARGE = (By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого х')]")

    QUESTION_CANCEL_ORDER = (By.XPATH, "//div[@id='accordion__heading-6']")
    ANSWER_CANCEL_ORDER = (By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, объ')]")

    # Новый вопрос и ответ
    QUESTION_DELIVERY_TO_MOSCOW = (By.XPATH, "//div[@id='accordion__heading-7']")
    ANSWER_DELIVERY_TO_MOSCOW = (By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Моско')]")
