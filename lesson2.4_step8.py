import time
import math 
import os
import pyperclip
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    # browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$' + str(100))
    )
    
    button = browser.find_element_by_id("book")
    button.click() 
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    
    button2 = browser.find_element_by_xpath('//button[text()="Submit"]')
    button2.click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    answer_for_stepik = alert_text.split(': ')[-1]
    pyperclip.copy(answer_for_stepik)
    time.sleep(1)
    pyautogui.click(x=338, y=750)
    time.sleep(1)
    # text_area_for_answer = browser.find_element_by_class_name('textarea string-quiz__textarea ember-text-area ember-view')
    pyautogui.click(x=466, y=413)
    time.sleep(0.5)
    pyautogui.typewrite(pyperclip.paste(), interval = 0.25)
    time.sleep(0.8)
    pyautogui.click(x=360, y=519)
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
    time.sleep(2)


# не забываем оставить пустую строку в конце файла