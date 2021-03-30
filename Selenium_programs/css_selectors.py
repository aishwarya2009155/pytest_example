import time
from selenium import webdriver
f_path = r"C:\Users\Admin\PycharmProjects\TY_project\Drivers\geckodriver.exe"
c_path = r"C:\Users\Admin\PycharmProjects\TY_project\Drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=c_path)

def css_class():
    # driver = webdriver.Firefox(executable_path=f_path)


    driver.get("http://demowebshop.tricentis.com/")
    driver.maximize_window()

    # using attribute
    driver.find_element("css selector", 'input[class="search-box-text ui-autocomplete-input"]').send_keys("electronics")
    time.sleep(2)

    # using id
    element = driver.find_element("css selector", 'input#small-searchterms')
    element.clear()
    time.sleep(2)
    element.send_keys("mobiles")

    # using class name
    driver.find_element("css selector", 'input.button-1.search-box-button').click()


def css_after_class():
    path = r"C:\Users\Admin\PycharmProjects\HTML-files\locator_html\parent_child.html"
    driver.get(path)
    driver.maximize_window()

    # using child
    driver.find_element("css selector", 'div[name="logout"]>input[type="text"]').send_keys("hello world")


css_after_class()