from selenium.webdriver.common.by import By

class MainPageLocators:
    SCOOTER_BUTTON = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_BUTTON = (By.XPATH, "//img[@alt='Yandex']")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav__AGCXC')]//button[contains(@class, 'Button_Button__ra12g')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM')]")
    COOKIE_CONSENT_BUTTON = (By.ID, "rcc-confirm-button")
