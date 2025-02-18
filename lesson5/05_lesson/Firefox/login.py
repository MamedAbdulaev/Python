# Откройте страницу http://the-internet.herokuapp.com/login.
# В поле username введите значение tomsmith
# В поле password введите значение  SuperSecretPassword!
# Нажмите кнопку Login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
driver.find_element(By.CSS_SELECTOR, '#username').send_keys("tomsmith")
driver.find_element(By.CSS_SELECTOR, '#password').send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, 'i').click()
