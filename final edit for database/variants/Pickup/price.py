from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
from bs4 import BeautifulSoup
import urllib
import re

links = ['https://www.cardekho.com/overview/Isuzu_D-Max_V-Cross/Isuzu_D-Max_V-Cross_4X4.htm']
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

pickle.dump(prices, open("price_pickup.p", "wb"))
pickle.dump(failed, open("failed.p", "wb"))
