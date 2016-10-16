from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time

driver = webdriver.Firefox()
catg = {}

driver.get("https://www.cardekho.com/new-hatchback+cars")
cars_dict = {}
main = {}
hatch_dict = {}

cars = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cartitle']//a")))
for i in cars:
    cars_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

variants = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='variantsDiv']//div[@class='magna']//a")))
for i in variants:
    hatch_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')
catg["Hatchback"] = hatch_dict
main["Hatchback"] = cars_dict


driver.get("https://www.cardekho.com/new-sedans+cars")
cars_dict = {}
sedan_dict = {}

cars = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cartitle']//a")))
for i in cars:
    cars_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

variants = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='variantsDiv']//div[@class='magna']//a")))
for i in variants:
    sedan_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')
catg["Sedans"] = sedan_dict
main["Sedans"] = cars_dict

driver.get("https://www.cardekho.com/new-muv+cars")
muv_dict = {}
cars_dict = {}

cars = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cartitle']//a")))
for i in cars:
    cars_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

variants = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='variantsDiv']//div[@class='magna']//a")))
for i in variants:
    muv_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')
catg["MUV"] = muv_dict
main["MUV"] = cars_dict

driver.get("https://www.cardekho.com/new-suv+cars")
suv_dict = {}
cars_dict = {}

cars = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cartitle']//a")))
for i in cars:
    cars_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

variants = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='variantsDiv']//div[@class='magna']//a")))
for i in variants:
    suv_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')
catg["SUV"] = suv_dict
main["SUV"] = cars_dict

driver.get("https://www.cardekho.com/new-luxury+cars")
luxury_dict = {}
cars_dict = {}
cars = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cartitle']//a")))
for i in cars:
    cars_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

variants = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='variantsDiv']//div[@class='magna']//a")))
for i in variants:
    luxury_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')
catg["Luxury"] = luxury_dict
main["Luxury"] = cars_dict

driver.get("https://www.cardekho.com/new-hybrids+cars")
hybrid_dict = {}
cars_dict = {}
cars = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cartitle']//a")))
for i in cars:
    cars_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

variants = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='variantsDiv']//div[@class='magna']//a")))
for i in variants:
    hybrid_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')
catg["Hybrid"] = hybrid_dict
main["Hybrid"] = cars_dict

driver.get("https://www.cardekho.com/new-minivans+cars")
mini_dict = {}
cars_dict = {}
cars = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cartitle']//a")))
for i in cars:
    cars_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

variants = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='variantsDiv']//div[@class='magna']//a")))
for i in variants:
    mini_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')
catg["Minivans"] = mini_dict
main["Minivans"] = cars_dict

driver.get("https://www.cardekho.com/new-convertibles+cars")
convert_dict = {}
cars_dict = {}
cars = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cartitle']//a")))
for i in cars:
    cars_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

variants = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='variantsDiv']//div[@class='magna']//a")))
for i in variants:
    convert_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')
catg["Convertibles"] = convert_dict
main["Convertibles"] = cars_dict

driver.get("https://www.cardekho.com/new-coupe+cars")
coupe_dict = {}
cars_dict = {}
cars = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cartitle']//a")))
for i in cars:
    cars_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

variants = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='variantsDiv']//div[@class='magna']//a")))
for i in variants:
    coupe_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')
catg["Coupe"] = coupe_dict
main["Coupe"] = cars_dict

driver.get("https://www.cardekho.com/new-pickup-trucks+cars")
pickup_dict = {}
cars_dict = {}
cars = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cartitle']//a")))
for i in cars:
    cars_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

variants = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='variantsDiv']//div[@class='magna']//a")))
for i in variants:
    pickup_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')
catg["Pickup"] = pickup_dict
main["Pickup"] = cars_dict

sList = [main, catg]

pickle.dump(sList, open( "links.p", "wb" ))
print main
print catg

driver.close()