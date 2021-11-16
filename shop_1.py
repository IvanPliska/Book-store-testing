import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(1)
My_Account = driver.find_element_by_link_text("My Account").click()
time.sleep(1)
Email_address = driver.find_element_by_id("username").send_keys("plis_in@mail.ru")
time.sleep(1)
Password_in = driver.find_element_by_id("password").send_keys("123Qaz456!@#$<>?")
time.sleep(1)
Remember_me = driver.find_element_by_id("rememberme").click()
time.sleep(1)
Register = driver.find_element_by_xpath("//input[@value='Login']").click()
time.sleep(2)
Shop = driver.find_element_by_css_selector("#menu-item-40 > a").click()
time.sleep(1)
HTML5_Forms = driver.find_element_by_xpath("//img[@title='Mastering HTML5 Forms']").click()
time.sleep(3)
Title_HTML5 = driver.find_element_by_css_selector(".product_title.entry-title")
Title_HTML5_get_text = Title_HTML5.text
assert Title_HTML5_get_text == "HTML5 Forms"
time.sleep(2)
driver.quit()