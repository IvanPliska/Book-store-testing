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
Shop = driver.find_element_by_css_selector("#menu-item-40 > a").click()
time.sleep(1)
Add_to_basket = driver.find_element_by_xpath("//a[@data-product_id='182']").click()
time.sleep(3)
Cartcontents = driver.find_element_by_class_name("cartcontents")
Cartcontents_get_text = Cartcontents.text
assert Cartcontents_get_text == "1 Item"
Amount = driver.find_element_by_xpath("//span[@class='amount']")
Amount_get_text = Amount.text
assert Amount_get_text == "₹180.00"
Busket = driver.find_element_by_class_name("wpmenucart-contents").click()
Total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cart_item .product-subtotal"), "₹180.00"))
Subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cart-subtotal .woocommerce-Price-amount"),"₹180.00"))
time.sleep(1)
driver.quit()