import pickle
from bs4 import BeautifulSoup
import urllib
import re

links = ['https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E350_Edition_E.htm', 'https://www.cardekho.com/overview/Bugatti_Veyron/Bugatti_Veyron_16.4_Grand_Sport.htm', 'https://www.cardekho.com/overview/Jaguar_F_Type/Jaguar_F_Type_S_Coupe.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Phantom.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E400_Cabriolet.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Extended_Wheelbase.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_V8_S_Convertible.htm', 'https://www.cardekho.com/overview/Jaguar_F_Type/Jaguar_F_Type_Coupe.htm', 'https://www.cardekho.com/overview/Audi_A3_cabriolet/Audi_A3_cabriolet_40_TFSI_Premium_Plus.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Carrera_S.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Turbo.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_SLC/Mercedes-Benz_SLC_43_AMG.htm', 'https://www.cardekho.com/overview/Jaguar_F_Type/Jaguar_F_Type_3.0_V6_S.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E350_CDI_Avantgrade.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Turbo_S_Cabriolet.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_V8_Convertible.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E_63_AMG.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E_200_CGI.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Dawn/Rolls-Royce_Dawn_Convertible.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E200_Edition_E.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_V8.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E250_CDI_Avantgarde.htm', 'https://www.cardekho.com/overview/Jaguar_F_Type/Jaguar_F_Type_R_Coupe.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E250_Edition_E.htm', 'https://www.cardekho.com/overview/BMW_Z4/BMW_Z4_35i_DPT.htm', 'https://www.cardekho.com/overview/BMW_Z4/BMW_Z4_35i.htm', 'https://www.cardekho.com/overview/Jaguar_F_Type/Jaguar_F_Type_5.0_V8_S.htm', 'https://www.cardekho.com/overview/Maserati_Gran_Cabrio/Maserati_Gran_Cabrio_4.7_V8.htm', 'https://www.cardekho.com/overview/Lamborghini_Aventador/Lamborghini_Aventador_Roadster_LP_700_4.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Carrera_Cabriolet.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Carrera.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_Speed_Convertible.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GTC.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Drophead_Coupe.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Turbo_S.htm', 'https://www.cardekho.com/overview/Porsche_Boxster/Porsche_Boxster_S.htm', 'https://www.cardekho.com/overview/Mini_Cooper_Convertible/Mini_Cooper_Convertible_S.htm', 'https://www.cardekho.com/overview/Porsche_Boxster/Porsche_Boxster_GTS.htm', 'https://www.cardekho.com/overview/Ferrari_California/Ferrari_California_T.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT.htm', 'https://www.cardekho.com/overview/Lamborghini_Aventador/Lamborghini_Aventador_LP700_4.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_Speed.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_V8_S.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Coupe.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Carrera_S_Cabriolet.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Turbo_Cabriolet.htm']
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

pickle.dump(prices, open("price_convert.p", "wb"))
pickle.dump(failed, open("failed.p", "wb"))
