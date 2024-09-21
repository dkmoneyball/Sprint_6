import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

def test_yandex_button(setup):
    main_page = MainPage(setup)
    main_page.load()

    main_page.click_yandex_button()

    setup.switch_to.window(setup.window_handles[-1])

    # Ждём, пока загрузится нужный URL
    WebDriverWait(setup, 10).until(EC.url_contains("https://dzen.ru/?yredirect=true"))

    # Проверяем URL
    assert "https://dzen.ru/?yredirect=true" in setup.current_url, "Не произошёл переход на Яндекс"
