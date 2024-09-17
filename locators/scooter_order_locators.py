from selenium.webdriver.common.by import By


class ScooterOrderPageLocators:
    """Локаторы для страницы заказа самоката"""
    INPUT_FIRST_NAME = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/input[1]")
    INPUT_LAST_NAME = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/input[1]")
    INPUT_ADDRESS = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[3]/input[1]")
    METRO_STATION_INPUT = (By.XPATH, "//input[@class='select-search__input']")  # локатор поля ввода станции метро
    METRO_STATION_OPTION = (By.XPATH, f"//*[contains(@class, 'select-search__select')]//*[text()='{{}}']")
    INPUT_PHONE = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[5]/input[1]")
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(),'Далее')]")

    # Локаторы для второй страницы
    INPUT_DELIVERY_DATE = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]")
    RENTAL_DURATION_DROPDOWN = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
    RENTAL_DURATION_OPTION = (
    By.XPATH, "//div[contains(text(),'{}')]")  # Здесь укажите нужную опцию (например, 'сутки' или 'трое суток')
    SCOOTER_COLOR_BLACK = (By.XPATH, "//input[@id='black']")
    SCOOTER_COLOR_GREY = (By.XPATH, "//input[@id='grey']")
    BUTTON_ORDER = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]/button[2]")
    BUTTON_CONFIRM_ORDER = (By.XPATH, "//button[contains(text(),'Да')]")
    BUTTON_VIEW_STATUS = (By.XPATH, "/html/body/div[1]/div/div[2]/div[5]/div[2]/button")
