from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # жмем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

  #находим другую вкладку и переходим в нее
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

  # формула
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # вычисление значения
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    # ввести ответ в поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # вывести финальный код в консоль
    print(browser.switch_to.alert.text)

finally:
     # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()