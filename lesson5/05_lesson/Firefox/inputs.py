from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
driver.find_element(By.CSS_SELECTOR, 'input').send_keys("1000")
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input').clear()
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input').send_keys('999')
