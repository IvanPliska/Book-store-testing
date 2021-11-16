import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
My_Account = driver.find_element_by_link_text("My Account").click()
time.sleep(3)
Email_address = driver.find_element_by_id("username").send_keys("plis_in@mail.ru")
time.sleep(3)
Password_in = driver.find_element_by_id("password").send_keys("123Qaz456!@#$<>?")
time.sleep(3)
Remember_me = driver.find_element_by_id("rememberme").click()
time.sleep(3)
Register = driver.find_element_by_xpath("//input[@value='Login']").click()
time.sleep(2)
Logout = driver.find_element_by_link_text("Logout")
if Logout is not None:
    print("Присутствует элемент Logout!")
else:
    print("Отсутствует элемент Logout!")
time.sleep(2)
driver.quit()