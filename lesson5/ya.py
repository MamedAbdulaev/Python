from selenium import webdriver
from time import sleep
driver = webdriver.Chrome ()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get ("https://ya.ru")
driver.get ("https://vk.com")

driver.back ()
driver.forward ()
sleep (2)
driver.refresh ()
driver.set_window_size (640,480)
sleep (2)
driver.maximize_window ()
sleep (2)
driver.fullscreen_window ()
sleep (2)
driver.get_screenshot_as_file ("qqqqqq,jpg")
