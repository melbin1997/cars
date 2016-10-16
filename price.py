from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

driver = webdriver.Chrome()

driver.get("https://www.cardekho.com/overview/Jeep_Grand_Cherokee/Jeep_Grand_Cherokee_Summit_4X4.htm")

price = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class = 'priceleft']//span")))
print price[2].text,price[3].text[:-1]

driver.close()