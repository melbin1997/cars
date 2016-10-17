from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
from bs4 import BeautifulSoup
import urllib
import re

links = ['https://www.cardekho.com/overview/Mahindra_Supro/Mahindra_Supro_VX_5_Str_BSIII.htm', 'https://www.cardekho.com/overview/Maruti_Eeco/Maruti_Eeco_7_Seater_Standard.htm', 'https://www.cardekho.com/overview/Maruti_Omni/Maruti_Omni_E_MPI_STD_BSIV.htm', 'https://www.cardekho.com/overview/Maruti_Eeco/Maruti_Eeco_5_Seater_Standard.htm', 'https://www.cardekho.com/overview/Mahindra_Supro/Mahindra_Supro_VX_8_Str.htm', 'https://www.cardekho.com/overview/Mahindra_Supro/Mahindra_Supro_ZX_5_Str.htm', 'https://www.cardekho.com/overview/Mahindra_Supro/Mahindra_Supro_LX_8_Str_BSIII.htm', 'https://www.cardekho.com/overview/Maruti_Omni/Maruti_Omni_MPI_CARGO_BSIV.htm', 'https://www.cardekho.com/overview/Mahindra_Supro/Mahindra_Supro_LX_8_Str.htm', 'https://www.cardekho.com/overview/Maruti_Omni/Maruti_Omni_MPI_Ambulance_BSIV.htm', 'https://www.cardekho.com/overview/Maruti_Eeco/Maruti_Eeco_CNG_HTR_5-STR.htm', 'https://www.cardekho.com/overview/Maruti_Eeco/Maruti_Eeco_CNG_5_Seater_AC.htm', 'https://www.cardekho.com/overview/Maruti_Eeco/Maruti_Eeco_5_Seater_AC.htm', 'https://www.cardekho.com/overview/Maruti_Eeco/Maruti_Eeco_Ambulance_Petrol_AC_Plus_HTR.htm', 'https://www.cardekho.com/overview/Maruti_Eeco/Maruti_Eeco_Flexi_Green.htm', 'https://www.cardekho.com/overview/Maruti_Omni/Maruti_Omni_MPI_STD_BSIV.htm', 'https://www.cardekho.com/overview/Mahindra_Supro/Mahindra_Supro_VX_8_Str_BSIII.htm', 'https://www.cardekho.com/overview/Mahindra_Supro/Mahindra_Supro_VX_5_Str.htm', 'https://www.cardekho.com/overview/Mahindra_Supro/Mahindra_Supro_ZX_5_Str_BSIII.htm']
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

pickle.dump(prices, open("price_minivans.p", "wb"))
pickle.dump(failed, open("failed.p", "wb"))
