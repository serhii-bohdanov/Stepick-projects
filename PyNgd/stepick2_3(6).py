from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)


browser.find_element(By.TAG_NAME, "button").click()


new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
y = str(math.log(abs(12 * math.sin(int(x)))))
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
browser.find_element(By.TAG_NAME, "button").click()
