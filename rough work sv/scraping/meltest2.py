import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

p=time.time()


driver = webdriver.Chrome()
user_input = "Bentley Bentayga"
driver.get("https://www.cardekho.com/")
car_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cardekhosearchtext")))
car_name.clear()
car_name.send_keys(user_input)
car_name.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.switch_to.default_content()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title*='" + user_input + "']")))
driver.find_element_by_css_selector("a[title*='" + user_input + "']").click()

#######################################################################################################################

'''g1=[user_input]
driver.find_element_by_css_selector("a[title*='Specs']").click()
keyf_collection = driver.find_elements_by_xpath("//table[@class='keyfeature']/tbody/tr")
#Displays key features
for elem in range(len(keyf_collection)):
    td = keyf_collection[elem].find_elements_by_tag_name('td')
    for i in td:
        if(i.get_attribute('class') == 'lefttd' or i.get_attribute('class') == 'righttd'):
            g1.append(i.text)
            #1print i.text,
    #2print
g2=[]
g3=0
while g3<len(g1):
    g2.append(g1[g3].encode('UTF8'))
    g3+=1
g2=[g2]
print g2'''

#######################################################################################################################

g4=[]           #!!!!!!!!!!!!g4 ni sheri akk.........

techf_collection = driver.find_elements_by_xpath("//div[@class='specinner']/div/table")
#Displays technical specs
for li in range(len(techf_collection)):
    print techf_collection[li].find_elements_by_xpath("//div[@class='specinner']/div/table//th")[li].get_attribute('title')
    tr = techf_collection[li].find_elements_by_tag_name('tr')
    for i in range(len(tr)):
        td = tr[i].find_elements_by_tag_name('td')
        for j in td:
            if(j.text.encode('UTF8')!=''):
                g4.append((j.text).encode('UTF8'))
            #prindt g4
            #print j.text,
            if('has not' in j.get_attribute('title')):
                #print "False",
                g4.append('False')
            elif('has' in j.get_attribute('title')):
                #print "True",
                g4.append('True')
    #time.sleep(10)

    



#driver.close()
print "Time taken= ",time.time()-p," seconds"
