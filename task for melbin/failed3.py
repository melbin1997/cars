#Gather failed car data (Try 3)

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

for index, car in enumerate(cars):
    try:

        link_car = car.split(" ")
        model = link_car[0]
        link_car = '_'.join(link_car)
        print "%d/%d" %(index+1, len(cars))
        print "Model : ", model, "\nCar : ", link_car
        link = "https://www.cardekho.com/carmodels/"+model+"/"+link_car
        print link
        driver.get(link)
        driver.switch_to.default_content()
        print "Review for", car
        review_mat = ''
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'introduction paddingtop0']//p")))

        for k in driver.find_elements_by_xpath("//div[@class = 'introduction paddingtop0']//p"):
            review_mat += k.text

        review[car] = review_mat.encode('UTF8')
        print review_mat
    except Exception as e:
        print car ,"failed due to", e
        failed.append(car)

pickle.dump(review, open("review3.p", "wb"))
pickle.dump(failed, open("failed.p", "wb"))

driver.close()
