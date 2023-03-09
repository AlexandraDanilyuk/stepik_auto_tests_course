from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://SunInJuly.github.io/execute_script.html"
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
    # просим проскроллить страницу пока аргумент не станет виден
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

    # Выбираем радиобатон и чек-бокс
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


