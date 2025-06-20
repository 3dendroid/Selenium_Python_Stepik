import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element(By.ID, "num1")
    num_2 = browser.find_element(By.ID, "num2")
    sum = int(num_1.text) + int(num_2.text)

    dropdown = Select(browser.find_element(By.ID, "dropdown"))
    dropdown.select_by_value(str(sum))

    submit_button = browser.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
