from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    input3.send_keys("mail")

    # Находим место для загрузки файла
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    # создаем файл для загрузки
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file

        current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
        element.send_keys(file_path)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()


finally:
     # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


