import time
from selenium import webdriver
c_path = r"C:\Users\Admin\PycharmProjects\TY_project\Drivers\chromedriver.exe"
url = "http://demowebshop.tricentis.com/"
driver = webdriver.Chrome(executable_path=c_path)


# launching the url
driver.get(url)

# maximize the window
driver.maximize_window()

# minimize the window
# driver.minimize_window()

# fullscreen
# driver.fullscreen_window()

# driver.back()
# driver.forward()
# driver.refresh()

# pos = driver.get_window_position()    # {x: , y: }
# print(pos)
#
# size = driver.get_window_size()    # {width: , height: }
# print(size)
#
# rect = driver.get_window_rect()     # {x, y, width, height}
# print(rect)
#
# driver.set_window_position(100, 200)
# time.sleep(2)
# driver.set_window_size(3000, 1000)
# time.sleep(2)
# driver.set_window_rect(x=10, y=50, width=400, height=200)

# closing the window
# driver.close()

# print(driver.title)
# print(driver.current_url)
# print(driver.name)
driver.set_page_load_timeout(0.00000001)
print(driver.page_source)
# close all the opened windows
driver.quit()
