#Gather failed car data (Try 4,5)

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
links = {'Maruti S-Cross':"https://www.cardekho.com/carmodels/Maruti/Maruti_SX4_S_Cross",
         'Volvo S80':"https://www.cardekho.com/carmodels/Volvo/Volvo_S_80",
         'Volvo XC90':"https://www.cardekho.com/carmodels/Volvo/Volvo_XC_90",
         'Mercedes-Benz GLA 45 AMG':"https://www.cardekho.com/carmodels/Mercedes-Benz/Mercedes-Benz_GLA",
         'Mercedes-Benz GLC':"https://www.cardekho.com/mercedes-benz/glc-class",
         'Mercedes-Benz GLE':"https://www.cardekho.com/carmodels/Mercedes-Benz/Mercedes-Benz_GLE_Class",
         'Mercedes-Benz GLS':"https://www.cardekho.com/carmodels/Mercedes-Benz/Mercedes-Benz_GL-Class",
         'Toyota Platinum Etios':"https://www.cardekho.com/carmodels/Toyota/Toyota_Etios",
         'Force One SUV': "https://www.cardekho.com/carmodels/Force/Force_One",
         'Ford Aspire':"https://www.cardekho.com/carmodels/Ford/Ford_Figo_Aspire",
         'Audi RS6 Avant':"https://www.cardekho.com/carmodels/Audi/Audi_RS6"
         }

#No review : rolls-royce , aston martin,

for index, car in enumerate(cars):
    try:

        driver.get(links[car])
        driver.switch_to.default_content()
        print "Review for", car
        review_mat = ''
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='tabDetails jqlazy']//p")))

        for k in driver.find_elements_by_xpath("//div[@class='tabDetails jqlazy']//p"):
            review_mat += k.text

        review[car] = review_mat.encode('UTF8')
        print review_mat
    except Exception as e:
        print car ,"failed due to", e
        failed.append(car)

pickle.dump(review, open("review5.p", "wb"))
pickle.dump(failed, open("failed.p", "wb"))

driver.close()
