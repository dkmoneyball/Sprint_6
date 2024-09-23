import pytest
from pages.main_page import MainPage

def test_scooter_button(setup):
    main_page = MainPage(setup)
    main_page.load()

    main_page.click_scooter_button()

    assert "qa-scooter.praktikum-services.ru" in setup.current_url, "Не произошёл переход на главную страницу самокатов"
