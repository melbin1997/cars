from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.cardekho.com/")
driver.find_element_by_id("searchNewCarByBrandInputDiv").click()
s = driver.find_element_by_id("newCarBrandSelect")
print s.text
