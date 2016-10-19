from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com/")
#assert "Python" in driver.title

elem = driver.find_element_by_id("lst-ib")
elem.clear()
elem.send_keys("Swift Dzire")
link=driver.find_elements_by_id()
link.click()