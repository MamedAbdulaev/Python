from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

def test_card_counter():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    # Перейти на сайт «Лабиринта»
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)
    sleep(5)
    # Найти все книги по слову Python
    # Переключиться на таблицу
    # Добавить все книги в корзину и посчитать
    # Перейти в корзину
    # Проверить счетчик товаров. Должен быть равным числу нажатий
    browser.quit()