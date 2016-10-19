from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

q = time.time()
user_input = "Porsche Boxster"
driver = webdriver.Chrome()
driver.get("https://www.cardekho.com/")
car_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cardekhosearchtext")))
car_name.clear()
car_name.send_keys(user_input)
car_name.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.switch_to.default_content()
# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "a[title*='" + user_input + "']"))).click()
driver.find_element_by_css_selector("a[title*='" + user_input + "']").click()

driver.find_element_by_css_selector("a[href*='pictures']").click()


############################################################################################################################

'''
category = {}
keyf_collection = driver.find_elements_by_xpath("//table[@class='keyfeature']/tbody/tr")
key_specs = {}

# Displays key features
for elem in range(len(keyf_collection)):
    td = keyf_collection[elem].find_elements_by_tag_name('td')
    for index, i in enumerate(td):
        # Even numbers are the keys and Odd numbers are the values
        if index % 2 == 1:
            key_specs[td[index - 1].text.encode('UTF8')] = i.text.encode('UTF8')
category.setdefault('Key Specs', []).append(key_specs)


############################################################################################################################'''

# print
# print "Time taken = ",time.time()-q," seconds"

#driver.close()
