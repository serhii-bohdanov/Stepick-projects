from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium import webdriver
import time
from math import log, sin


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

try:
    button = WebDriverWait(browser, 7).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))

    Book = browser.find_element_by_css_selector("#book").click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код)
    browser.find_element_by_id('answer').send_keys(
        str(log(abs(12 * sin(int(browser.find_element_by_id('input_value').text)))))
    )
    browser.find_element(By.CSS_SELECTOR, "[type='Submit']").click()
finally:
    time.sleep(4)
    browser.quit()