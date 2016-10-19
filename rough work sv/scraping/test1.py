from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.carwale.com/new/")
#assert "Python" in driver.title

link = driver.find_elements_by_id("btnYes")
link.click()
elem = driver.find_element_by_id("globalSearch")
elem.clear()
elem.send_keys("Swift Dzire")
elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()