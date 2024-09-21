import pytest
from pages.main_page import MainPage
from pages.scooter_order_page import ScooterOrderPage

# Параметризация теста с двумя наборами данных
@pytest.mark.parametrize("first_name, last_name, address, metro_station, phone_number, delivery_date, rental_duration", [
    ("Иван", "Иванов", "ул. Пушкина, д. 1", "Ботанический сад", "89999999999", "26.09.2024", "сутки"),
    ("Мария", "Сидорова", "ул. Ленина, д. 2", "Проспект Мира", "89888888888", "30.09.2024", "трое суток")
])
def test_order_scooter(setup, first_name, last_name, address, metro_station, phone_number, delivery_date, rental_duration):
    main_page = MainPage(setup)
    scooter_page = ScooterOrderPage(setup)

    # Открываем главную страницу
    main_page.load()

    # Закрываем уведомление с куками, если оно есть
    main_page.close_cookie_consent()

    # Нажимаем на кнопку "Заказать" вверху страницы
    main_page.click_order_button_top()

    # Заполняем первую страницу заказа
    scooter_page.fill_order_form(first_name, last_name, address, metro_station, phone_number)

    # Заполняем вторую страницу заказа
    scooter_page.fill_rent_form(delivery_date, rental_duration)

    # Подтверждаем заказ
    scooter_page.confirm_order()

    # Проверяем статус заказа
    scooter_page.check_order_status()
