import pyperclip as pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element_by_tag_name("button").click()
confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
y = str(math.log(abs(12 * math.sin(int(x)))))
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
button = browser.find_element_by_tag_name("button").click()



alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)