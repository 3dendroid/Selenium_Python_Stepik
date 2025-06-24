import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Ivanov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("IvanIvanov@mail.com")

    file_txt = r"C:\Users\SUPERDEN\PycharmProjects\Selenium_Python_Stepik\2.2 work_with_files\file.txt"
    file = browser.find_element(By.ID, "file")
    file.send_keys(file_txt)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
