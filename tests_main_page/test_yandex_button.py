from pages.main_page import MainPage


def test_order_buttons(setup):
    """Тест на проверку кнопок 'Заказать' и 'Самокат' на главной странице"""
    main_page = MainPage(setup)
    main_page.load()  # Загружаем главную страницу

    # Нажимаем на верхнюю кнопку 'Заказать'
    main_page.click_order_button_top()
    assert "order" in setup.current_url, "Не произошёл переход на страницу заказа после нажатия на верхнюю кнопку"

    # Переходим назад и проверяем кнопку 'Самокат'
    setup.back()
    main_page.click_scooter_button()
    assert "qa-scooter.praktikum-services.ru" in setup.current_url, "Не произошёл переход на главную страницу самокатов"


def test_yandex_button(setup):
    """Тест на проверку кнопки 'Яндекс'"""
    main_page = MainPage(setup)
    main_page.load()  # Загружаем главную страницу

    # Нажимаем на кнопку 'Яндекс'
    main_page.click_yandex_button()
    assert "dzen.ru" in setup.current_url, "Не произошёл переход на Яндекс"


def test_scroll_to_bottom_and_click_order(setup):
    """Тест на прокрутку до нижней кнопки 'Заказать' и переход на страницу заказа"""
    main_page = MainPage(setup)
    main_page.load()  # Загружаем главную страницу

    # Прокручиваем страницу до конца и нажимаем на нижнюю кнопку 'Заказать'
    main_page.scroll_to_bottom_and_click_order()
    assert "order" in setup.current_url, "Не произошёл переход на страницу заказа после нажатия на нижнюю кнопку"
