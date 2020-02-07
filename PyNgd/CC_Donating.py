from lib2to3.pgen2 import driver

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
link = "https://dev4donate.lls.org/lls/donate"
browser = webdriver.Chrome()
browser.get(link)

try:
    Donate_amount_btn = browser.find_element(By.CSS_SELECTOR, "#amount5usd").click()
    first_name = browser.find_element(By.CSS_SELECTOR, "#firstName").send_keys("Oleg")
    last_name = browser.find_element(By.CSS_SELECTOR, "#lastName").send_keys("Merdsa")
    email = browser.find_element(By.CSS_SELECTOR, "#email").send_keys("dev4_qauser30@lls.org")
    """-------------------------------------------------------------------""" # Go To Frame
    time.sleep(3)
    browser.switch_to.frame(browser.find_element(By.CSS_SELECTOR, "#iframe_hosted"))
    Card_Name = browser.find_element(By.CSS_SELECTOR, "#cardHolderName").send_keys("Ivan")
    browser.switch_to.frame(browser.find_element(By.CSS_SELECTOR, "#braintree-hosted-field-number"))
    time.sleep(3)
    Numb_CC_Card = browser.find_element(By.ID, "credit-card-number").send_keys("4111111111")

    browser.switch_to.default_content()
    """-------------------------------------------------------------------"""

    #Address1 = browser.find_element(By.CSS_SELECTOR, "#ccAddress1").send_keys("Address")
    #Country = browser.find_element(by.CSS_SELECTOR, "#ccCountry").find_element(By.NAME, "United States of America").click()



    #PostalCode = browser.find_element(by.CSS_SELECTOR, "#ccPostalCode").send_keys("35007")
    #Captcha = browser.find_element(by.XPATH,"/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]")
    #time.sleep(5)


finally:
    time.sleep(3)
    #DONATE_NOW = browser.find_element(by.CSS_SELECTOR, "#formSubmitButton").click()
   # browser.quit()




   #https://selenium-python.readthedocs.io/locating-elements.html