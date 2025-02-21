from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get ('https://demoqa.ru/qa-auto/alerts/browser-windows')
driver.find_element(By.CSS_SELECTOR,'.px-4.py-2').click()

sleep(3)
driver.close()
sleep (2)

