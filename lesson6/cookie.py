from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
my_cookie = {'name': 'cookie_policy',
          'value': '1'}
driver.get('https://labirint.ru')
driver.add_cookie(my_cookie)
cookie=driver.get_cookie('begintimed')
# driver.refresh ()
# driver.delete_cookie ('cookie_policy')
# driver.refresh ()
print(cookie)
sleep (5)
driver.quit()