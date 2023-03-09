from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # формула
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # взять у картинку значение
    treasure = browser.find_element(By.ID, 'treasure')
    # взять у значения атрибут
    x_element = treasure.get_attribute('valuex')
    x = x_element
    y = calc(x)

    # ввести ответ в поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
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