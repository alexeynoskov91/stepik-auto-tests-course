from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id('num1')
    x = x_element.text    
    y_element = browser.find_element_by_id('num2')
    y = y_element.text
    print(int(x)+int(y))
    
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(int(x) + int(y))) 
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
 
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    time.sleep(2)


# не забываем оставить пустую строку в конце файла