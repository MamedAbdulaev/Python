# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
# Пять раз кликните на кнопку Add Element
# Соберите со страницы список кнопок Delete
# Выведите на экран размер списка.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
add_element = '[onclick="addElement()"]'
driver.find_element(By.CSS_SELECTOR, add_element).click()
driver.find_element(By.CSS_SELECTOR, add_element).click()
driver.find_element(By.CSS_SELECTOR, add_element).click()
driver.find_element(By.CSS_SELECTOR, add_element).click()
driver.find_element(By.CSS_SELECTOR, add_element).click()

delete = driver.find_elements(By.CSS_SELECTOR, '.added-manually')
print("Кол-во кнопок Delete", + len(delete))
