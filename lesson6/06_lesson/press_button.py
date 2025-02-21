from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/ajax')
ajax = driver.find_element(By.CSS_SELECTOR, '#ajaxButton')
ajax.click()
driver.implicitly_wait(20)
data = driver.find_element(By.CSS_SELECTOR, '.bg-success').text
print(data)
driver.quit()
