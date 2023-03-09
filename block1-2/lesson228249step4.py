from selenium import webdriver
browser = webdriver.Chrome()
import time

link = "https://suninjuly.github.io/selects2.html"

browser.execute_script("alert('Robots at work');")

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()