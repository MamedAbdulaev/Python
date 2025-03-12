from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

cookie = {'name':'cookie_policy',
          "value":'1'}
browser = None
def open_labirint ():
    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)
   


def add_books():
        # Добавить все книги в корзину и посчитать
        buy_buttons = browser.find_elements(By.CSS_SELECTOR, '._btn.btn-tocart.buy-link')
        counter = 0
        for btn in buy_buttons:
         btn.click()
         counter += 1
        print(counter)    
        return counter

def go_to_cart():
    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart")
    
def get_cart_counter():
    # Проверить счетчик товаров. Должен быть равным числу нажатий
    txt = browser.find_element(By.CSS_SELECTOR,'.b-header-b-personal-e-icon-count-m-cart').text
    return int(txt)

def close_driver():
    # Закрытие браузера
    browser.quit()

def test_card_counter():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    open_labirint()
    search('python')
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver()
    assert added==cart_counter

def test_empty_search():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    open_labirint()
    search('no book search term')
    txt = get_title() 
    assert txt=='Пока не нашли для себя ничего в Лабиринте?'

    # assert int(cart_counter)==counter
    # print('Счетчик нажатий равен', + counter)
    # print('Счетчик в корзине равен', + cart_counter)
