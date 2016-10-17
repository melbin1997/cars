#Gather failed car data (Try 6,7)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import datetime

with open("failed.p", 'rb') as fp:
    cars = pickle.load(fp)

review = {}
failed = []
driver = webdriver.Chrome()
links = {'Hyundai Creta':"https://www.cardekho.com/hyundai-cars/creta"
         }

#No review : rolls-royce , aston martin,

for index, car in enumerate(cars):
    try:

        driver.get(links[car])
        driver.switch_to.default_content()
        print "Review for", car
        review_mat = ''
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id = 'reviewSection']//p")))

        for k in driver.find_elements_by_xpath("//div[@id = 'reviewSection']//p"):
            review_mat += k.text

        review[car] = review_mat.encode('UTF8')
        print review_mat
    except Exception as e:
        print car ,"failed due to", e
        failed.append(car)

pickle.dump(review, open("review7.p", "wb"))
pickle.dump(failed, open("failed.p", "wb"))

driver.close()