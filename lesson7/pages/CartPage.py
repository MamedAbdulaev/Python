from selenium.webdriver.common.by import By
class CartPage:
    def __init__(self,browser):
        self._driver=browser

    def get(self):
        self._driver.get('https://www.labirint.ru/cart/')

    def get_counter(self):
        txt=self._driver.find_element(By.CSS_SELECTOR,'.b-header-b-personal-e-icon-count-m-cart').text
        return int(txt)
