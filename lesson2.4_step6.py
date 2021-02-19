import time
import math 
import os
import pyperclip
import pyautogui
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/cats.html")

    button = browser.find_element_by_id("button")
    button.click()
    # message = browser.find_element_by_id("verify_message")

    # assert "successful" in message.text
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
    time.sleep(2) 


# не забываем оставить пустую строку в конце файла