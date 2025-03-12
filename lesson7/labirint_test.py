from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

cookie = {'name':'cookie_policy',
          "value":'1'}

def test_card_counter():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)
    
    # Найти все книги по слову Python
    browser.find_element(By.CSS_SELECTOR,'#search-field').send_keys('Python')
    
    # Добавить все книги в корзину и посчитать
    browser.find_element(By.CSS_SELECTOR,'button[type=submit]').click()
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, '._btn.btn-tocart.buy-link')
    counter = 0
    for btn in buy_buttons:
         btn.click()
         counter += 1
    print(counter)    
    
    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart")
    
    # Проверить счетчик товаров. Должен быть равным числу нажатий
    cart_counter = browser.find_element(By.CSS_SELECTOR,'.b-header-b-personal-e-icon-count-m-cart').text

    assert int(cart_counter)==counter
    # print('Счетчик нажатий равен', + counter)
    # print('Счетчик в корзине равен', + cart_counter)
    browser.quit()
    
