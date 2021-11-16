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
Orderby_1 = driver.find_element_by_xpath("//option[@value='menu_order']")
Orderby_check = Orderby_1.get_attribute("value")
if Orderby_check =="menu_order":
    print("Выбрана сортировка по умолчанию")
else:
    print("Сортировка по умолчанию не выбрана")
Orderby_2 = driver.find_element_by_css_selector(".woocommerce-ordering>select")
Orderby_select = Select(Orderby_2)
Orderby_select.select_by_value("price-desc")
time.sleep(2)
Orderby_3 = driver.find_element_by_xpath("//option[@value='price-desc']")
Orderby_check = Orderby_3.get_attribute("value")
if Orderby_check =="price-desc":
    print("Выбрана сортировка от большего к меньшему")
else:
    print("Сортировка от большего к меньшему не выбрана")