import time
import math 
import os
import pyperclip
import pyautogui
# print(pyautogui.position())
from selenium import webdriver


link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath('//button[text()="I want to go on a magical journey!"]')
    button.click()
    time.sleep(1)
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # confirm = browser.switch_to.alert
    # confirm.accept()
    # time.sleep(1)
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    time.sleep(1)

    button2 = browser.find_element_by_xpath('//button[text()="Submit"]')
    button2.click()
    time.sleep(1)
    
    # alert = browser.switch_to.alert 
    # alert_text = alert.text
    # answer_for_stepik = alert_text.split(': ')[-1]
    # pyperclip.copy(answer_for_stepik)
    # time.sleep(1)
    # pyautogui.click(x=338, y=750)
    # time.sleep(1)
    # text_area_for_answer = browser.find_element_by_class_name('textarea string-quiz__textarea ember-text-area ember-view')
    # pyautogui.click(x=466, y=413)
    # time.sleep(0.5)
    # pyautogui.typewrite(pyperclip.paste(), interval = 0.25)
    # time.sleep(0.8)
    # pyautogui.click(x=360, y=519)
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
    time.sleep(2)


# не забываем оставить пустую строку в конце файла