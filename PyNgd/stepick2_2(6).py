from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    elements = browser.find_elements(By.CSS_SELECTOR, ".form-control")
    for element in elements:
        element.send_keys("Test")

    import os

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    browser.find_element_by_css_selector("#file").send_keys(file_path)
    button = browser.find_element_by_tag_name("button").click()


finally:
    time.sleap(4)
    browser.quit()