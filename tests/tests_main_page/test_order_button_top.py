import pytest
from pages.main_page import MainPage

def test_order_button_top(setup):
    main_page = MainPage(setup)
    main_page.load()

    main_page.close_cookie_consent()
    main_page.click_order_button_top()

    assert "order" in setup.current_url, "Не произошёл переход на страницу заказа"
