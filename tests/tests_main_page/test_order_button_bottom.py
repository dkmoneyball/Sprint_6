import pytest
from pages.main_page import MainPage

def test_order_button_bottom(setup):
    main_page = MainPage(setup)
    main_page.load()

    # Закрываем уведомление с куками
    main_page.close_cookie_consent()

    # Нажимаем на нижнюю кнопку 'Заказать'
    main_page.click_order_button_bottom()

    # Проверяем, что произошёл переход на страницу заказа
    assert "order" in setup.current_url, "Не произошёл переход на страницу заказа"
