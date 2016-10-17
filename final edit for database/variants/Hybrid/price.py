from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
from bs4 import BeautifulSoup
import urllib
import re

links = ['https://www.cardekho.com/overview/BMW_i8/BMW_i8_Hybrid.htm', 'https://www.cardekho.com/overview/Volvo_XC_90/Volvo_XC_90_D5_Momentum.htm', 'https://www.cardekho.com/overview/Volvo_XC_90/Volvo_XC_90_T8_Excellence.htm', 'https://www.cardekho.com/overview/Volvo_XC_90/Volvo_XC_90_D5_Inscription.htm', 'https://www.cardekho.com/overview/Toyota_Camry/Toyota_Camry_Hybrid.htm', 'https://www.cardekho.com/overview/Toyota_Camry/Toyota_Camry_2.5_G.htm', 'https://www.cardekho.com/overview/Toyota_Prius/Toyota_Prius_Z6.htm', 'https://www.cardekho.com/overview/Toyota_Prius/Toyota_Prius_Z5.htm']
prices = {}
failed = []

for url in links:
	try:
		page = urllib.urlopen(url)
		soup = BeautifulSoup(page.read())
		soup=soup.find("div", {"class": "priceleft"})
		soup = ''.join(soup.findAll('span')[0].findAll(text=True)[2:4])
		print url,'-->',soup
		prices[url] = soup
	except Exception as e:
		print url
		failed.append(url)

pickle.dump(prices, open("price_hybrid.p", "wb"))
pickle.dump(failed, open("failed.p", "wb"))
