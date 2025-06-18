import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")
    treasure_value = treasure.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(treasure_value)

    answer = browser.find_element(By.XPATH, "//input[@id='answer']")
    answer.send_keys(y)

    checkbox = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    radiobutton.click()

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
