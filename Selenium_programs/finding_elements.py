# find_element(loc_type, loc_value) , find_elements(loc_type, loc_value)
from selenium import webdriver
from selenium.webdriver.common.by import By

c_path = r"C:\Users\Admin\PycharmProjects\TY_project\Drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=c_path)


url = "http://demowebshop.tricentis.com/"
driver.get(url)

# id locator
element = driver.find_element("id", "small-searchterms")
# print(element)
# print(type(element))
element.click()
element.send_keys("mobiles")

# class locator
driver.find_element("class name", "ico-register").click()
# driver.find_element_by_class_name("ico-register")
# driver.find_element(By.CLASS_NAME, "ico-register")

# name locator
element = driver.find_element("name", "q")
element.clear()
element.send_keys("books")

# link text locator
# driver.find_element("link text", "Register").click()

# partial link text locator
driver.find_element("partial link text", "Reg").click()
