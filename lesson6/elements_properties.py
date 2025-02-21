from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get('https://ya.ru')
# txt=driver.find_element (By.CSS_SELECTOR, '.Text_typography_control-xxs').text
# tag=driver.find_element (By.CSS_SELECTOR, '.Text_typography_control-xxs').tag_name
# id= driver.find_element (By.CSS_SELECTOR, '.Text_typography_control-xxs').id
# ff=driver.find_element (By.CSS_SELECTOR, '.Text_typography_control-xxs').value_of_css_property ('color')
# print (txt)
# print (tag)
# print (id)
# print (ff)

# driver.get ('http://uitestingplayground.com/visibility')
# is_displayed=driver.find_element(By.CSS_SELECTOR,'#transparentButton').is_displayed()
# print(is_displayed)

# is_displayed=driver.find_element(By.CSS_SELECTOR,'#hideButton').click()
# sleep(2)
# is_displayed=driver.find_element(By.CSS_SELECTOR,'#transparentButton').is_displayed()
# print(is_displayed)
# sleep(2)

driver.get ('https://the-internet.herokuapp.com/checkboxes')
# is_selected=driver.find_element(By.CSS_SELECTOR,'[type=checkbox]')
# ch=is_selected.is_selected()
# print (ch)
# sleep (1)
# is_selected.click()
# is_selected=driver.find_element(By.CSS_SELECTOR,'[type=checkbox]')
# ch=is_selected.is_selected()
# print (ch)
# sleep (1)
# div=driver.find_element(By.CSS_SELECTOR, '#page-footer')
# a=div.find_element(By.CSS_SELECTOR, 'a')
# print (a.get_attribute('href'))
divs=driver.find_elements(By.CSS_SELECTOR,'div')
# l = len(divs)
# print(l)
div = divs [6]
css_class=div.get_attribute('class')
print(css_class)
driver.quit()