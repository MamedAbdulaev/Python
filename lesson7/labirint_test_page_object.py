from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage
from time import sleep

def test_card_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search('java')
   
    result_page= ResultPage(browser)
    to_be = result_page.add_books()
    
    cart_page=CartPage(browser)
    cart_page.get()
    as_is = cart_page.get_counter()

    assert as_is==to_be

    browser.quit()


def test_empty_search_result():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search('ролплорпорпорпороропрпорпо')
    sleep(3)
    result_page=ResultPage(browser)
    result_page.get_empty_result_message()
    browser.quit()