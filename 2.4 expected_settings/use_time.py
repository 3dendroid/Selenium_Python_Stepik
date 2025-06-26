import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
try:
    time.sleep(2)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(2)
    browser.quit()
