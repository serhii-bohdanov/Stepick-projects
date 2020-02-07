from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

try:
 x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
 y = str(math.log(abs(12 * math.sin(int(x)))))
 browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
 browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
 browser.execute_script("window.scrollBy(0, 300);")
 browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
 button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(4)
    browser.quit()