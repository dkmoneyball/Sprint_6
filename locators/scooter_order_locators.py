from selenium.webdriver.common.by import By

class ScooterOrderPageLocators:
    # Локаторы для первой страницы заказа
    INPUT_FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    # Локаторы для второй страницы заказа
    INPUT_DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_DURATION_DROPDOWN = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
    SCOOTER_COLOR_BLACK = (By.ID, "black")
    SCOOTER_COLOR_GREY = (By.ID, "grey")
    BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[contains(text(), 'Заказать')]")
    BUTTON_CONFIRM_ORDER = (By.XPATH, "//button[text()='Да']")
    BUTTON_VIEW_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")
