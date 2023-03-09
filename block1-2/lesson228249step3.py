from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим элемент
    num1 = browser.find_element(By.ID, 'num1')
    # записываем в переменную число из элемента x
    x = num1.text
    num2 = browser.find_element(By.ID, 'num2')
    y = num2.text
    # переводим в числовой формат
    z = str(str(int(x)+int(y)))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(z)  # ищем элемент с подсчитанной переменной

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()