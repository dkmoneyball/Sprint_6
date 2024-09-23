from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, time=10):
        element = self.find_element(locator, time)
        element.click()

    def is_text_present(self, locator, expected_text, time=10):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return expected_text in element.text

    def fill_input(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.clear()  # Очистить поле перед вводом, если это необходимо
        element.send_keys(text)

    def is_element_present(self, locator, time=10):
        """Проверяет наличие элемента на странице."""
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

