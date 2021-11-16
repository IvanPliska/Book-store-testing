import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
My_Account = driver.find_element_by_link_text("My Account").click()
time.sleep(3)
Email = driver.find_element_by_id("reg_email").send_keys("plis_in@mail.ru")
time.sleep(3)
Password = driver.find_element_by_id("reg_password").send_keys("123Qaz456!@#$<>?")
time.sleep(3)
Register = driver.find_element_by_xpath("//input[@value='Register']").click()
time.sleep(3)
driver.quit()