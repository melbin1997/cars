from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

def p():
	driver = webdriver.Chrome()

	driver.get("https://www.cardekho.com/overview/Maruti_Swift/Maruti_Swift_VDI_BS_IV.htm")

	price = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class = 'priceleft']//span")))
	
	return price[2].text,price[3].text[:-1]
