from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://www.cardekho.com/pictures/Tata_Nano_XE")

imgs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//img[@class = 'jqlazy']")))
for img in imgs:
    print img.get_attribute("data-original")

driver.close()