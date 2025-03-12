from selenium.webdriver.common.by import By
from time import sleep

class ResultPage:
    def __init__(self,browser):
        self._driver=browser
    
    def add_books(self):
        # Добавить все книги в корзину и посчитать
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, '._btn.btn-tocart.buy-link')
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1
            
        return counter
    
    def get_empty_result_message(self):
        self._driver.find_element(By.CSS_SELECTOR,'.navisort-group-flg').click()
        sleep (3)
        res=self._driver.find_element(By.CSS_SELECTOR,'.b-stab-e-slider-item-e-txt-m-small.js-search-tab-count').text
        assert res ==''