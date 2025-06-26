import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x = int(browser.find_element(By.ID, "input_value").text)
    y = math.log(abs(12 * math.sin(x)))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(str(y))

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
