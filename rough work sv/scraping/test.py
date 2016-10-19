from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def search(s):
    elem = driver.find_elements_by_id("homeSearch")
    elem.send_keys(s)
    elem.send_keys(Keys.ENTER)

print"Enter what you want to search: "
s = raw_input()
driver = webdriver.Firefox()
driver.get("http://zigwheels.com/")
search(s)
time.sleep(10)
driver.close()