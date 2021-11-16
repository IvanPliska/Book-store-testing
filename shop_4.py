import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
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
Android_Quick_Start_Guide = driver.find_element_by_xpath("//img[@alt='Android Quick Start Guide']").click()
Old_price = driver.find_element_by_css_selector(".price>del>span")
Old_price_get_text = Old_price.text
assert "₹600.00" in Old_price_get_text
New_price = driver.find_element_by_css_selector(".price>ins>span")
New_price_get_text = New_price.text
assert "₹450.00" in New_price_get_text
time.sleep(2)
Android_img = WebDriverWait (driver, 10).until(EC.element_to_be_clickable((By.XPATH , "//img[@alt='Android Quick Start Guide']")))
Android_img_btn = driver.find_element_by_xpath("//img[@alt='Android Quick Start Guide']").click
Android_img_close = WebDriverWait (driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
Android_img_close_btn = driver.find_element_by_css_selector(".pp_close").click
time.sleep(1)
driver.quit()