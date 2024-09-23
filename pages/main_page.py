from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    URL = "https://qa-scooter.praktikum-services.ru/"

    def load(self):
        self.open_page(self.URL)

    def click_scooter_button(self):
        scooter_button = self.driver.find_element(*MainPageLocators.SCOOTER_BUTTON)
        scooter_button.click()

    def click_yandex_button(self):
        yandex_button = self.driver.find_element(*MainPageLocators.YANDEX_BUTTON)
        yandex_button.click()

    def click_order_button_top(self):
        order_button_top = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_TOP)
        order_button_top.click()

    def click_order_button_bottom(self):
        order_button_bottom = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button_bottom)
        # Используем JavaScript для клика
        self.driver.execute_script("arguments[0].click();", order_button_bottom)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def close_cookie_consent(self):
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_CONSENT_BUTTON)
            )
            cookie_button.click()
        except:
            pass
