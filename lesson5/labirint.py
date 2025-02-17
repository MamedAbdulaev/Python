from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Зайти на лабиринт:
driver.get ("https://labirint.ru")
# В поиск вбить "Python" и нажать enter:
search_input=driver.find_element (By.CSS_SELECTOR, '#search-field')
search_input.send_keys ('Python', Keys.ENTER)

# Собрать карточки товаров
book_locator = 'div.product-card'
books= driver.find_elements (By.CSS_SELECTOR, 'div.product-card')
# Вывести в консоль инфо о книгах
for book in books:
    title = book.find_element (By.CSS_SELECTOR, 'a.product-card__name').text
    author=book.find_element (By.CSS_SELECTOR, 'div.product-card__author').text
    price = book.find_element (By.CSS_SELECTOR, '.product-card__price-current').text
    print (author + "\t" + title + "\t" + price)





