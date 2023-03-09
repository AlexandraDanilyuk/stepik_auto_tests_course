from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # формула
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # вычисление значения
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    # вставляем результат
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Выбираем радиобатон и чек-бокс
    option1 = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
    option1.click()

    option1 = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
