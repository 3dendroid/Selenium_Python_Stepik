import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/cats.html")
try:
    browser.find_element(By.ID, "button")

finally:
    time.sleep(2)
    browser.quit()
