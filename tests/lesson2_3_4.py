from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element_by_class_name("btn").click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    y = calc(x)

    input = browser.find_element_by_id("answer").send_keys(y)

    button = browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(5)
    browser.quit()
