from pages.base_page import BasePage
from locators.scooter_order_locators import ScooterOrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ScooterOrderPage(BasePage):


    URL = "https://qa-scooter.praktikum-services.ru/"

    def open_main_page(self):
        self.open_page(self.URL)

    def fill_order_form(self, first_name, last_name, address, metro_station, phone_number):
        # Используем методы BasePage для взаимодействия с элементами
        self.fill_input(ScooterOrderPageLocators.INPUT_FIRST_NAME, first_name)
        self.fill_input(ScooterOrderPageLocators.INPUT_LAST_NAME, last_name)
        self.fill_input(ScooterOrderPageLocators.INPUT_ADDRESS, address)

        # Заполнение станции метро с выбором из выпадающего списка
        self.fill_input(ScooterOrderPageLocators.INPUT_METRO, metro_station)
        metro_option_locator = (
        By.XPATH, f"//div[contains(@class, 'select-search__select')]//*[text()='{metro_station}']")
        self.click_element(metro_option_locator)

        # Вводим номер телефона
        self.fill_input(ScooterOrderPageLocators.INPUT_PHONE, phone_number)

        # Нажимаем кнопку "Далее"
        self.click_element(ScooterOrderPageLocators.BUTTON_NEXT)

    def fill_rent_form(self, delivery_date, rental_duration):
        # Вводим дату доставки
        self.fill_input(ScooterOrderPageLocators.INPUT_DELIVERY_DATE, delivery_date)

        # Закрываем календарь
        self.click_element(ScooterOrderPageLocators.BUTTON_ORDER)

        # Открываем список сроков аренды и выбираем нужный срок
        self.click_element(ScooterOrderPageLocators.RENTAL_DURATION_DROPDOWN)
        rental_option_locator = (By.XPATH, f"//div[contains(text(),'{rental_duration}')]")
        self.click_element(rental_option_locator)

        # Выбираем цвет самоката
        self.click_element(ScooterOrderPageLocators.SCOOTER_COLOR_BLACK)

        # Нажимаем кнопку "Заказать"
        self.click_element(ScooterOrderPageLocators.BUTTON_ORDER)

    def confirm_order(self):
        self.click_element(ScooterOrderPageLocators.BUTTON_CONFIRM_ORDER)

    def check_order_status(self):
        """Проверка наличия кнопки 'Посмотреть статус'."""
        return self.is_element_present(ScooterOrderPageLocators.BUTTON_VIEW_STATUS)
