# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
# Пять раз кликните на кнопку Add Element
# Соберите со страницы список кнопок Delete
# Выведите на экран размер списка.
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get ("http://the-internet.herokuapp.com/add_remove_elements/")
driver.find_element (By.CSS_SELECTOR,'[onclick="addElement()"]' ).click
driver.find_element (By.CSS_SELECTOR,'[onclick="addElement()"]' ).click
driver.find_element (By.CSS_SELECTOR,'[onclick="addElement()"]' ).click
sleep (2)


