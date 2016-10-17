from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
from bs4 import BeautifulSoup
import urllib
import re

links = ['https://www.cardekho.com/overview/Aston_Martin_Rapide/Aston_Martin_Rapide_S_V12.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_Maybach_S600.htm', 'https://www.cardekho.com/overview/Maserati_Ghibli/Maserati_Ghibli_Diesel.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320d_Luxury_Line.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320i_Prestige.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_4.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E350_CDI_Avantgrade.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_X6_M.htm', 'https://www.cardekho.com/overview/Maserati_Quattroporte/Maserati_Quattroporte_Diesel.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_Turbo.htm', 'https://www.cardekho.com/overview/BMW_7_Series/BMW_7_Series_750Li_M_Sport_CBU.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_CLS-Class/Mercedes-Benz_CLS-Class_250_CDI.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_W12_quattro.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E_200_CGI.htm', 'https://www.cardekho.com/overview/Audi_A6/Audi_A6_35_TFSI.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E250_CDI_Avantgarde.htm', 'https://www.cardekho.com/overview/BMW_7_Series/BMW_7_Series_730Ld_Design_Pure_Excellence_CBU.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_60_TDI_Quattro.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_2.0_Petrol_Portfolio.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_Security.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_2.0_Diesel_Prestige.htm', 'https://www.cardekho.com/overview/Audi_A4/Audi_A4_30_TFSI_Premium_Plus.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_220_CDI_Avantgarde.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_Maybach_S500.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_2.0_Petrol_Prestige.htm', 'https://www.cardekho.com/overview/Audi_A4/Audi_A4_30_TFSI_Technology.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_GTS.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_Diesel.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_D4_Momentum.htm', 'https://www.cardekho.com/overview/Audi_RS7/Audi_RS7_Sportback.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320i_Luxury_Line.htm', 'https://www.cardekho.com/overview/BMW_5_Series/BMW_5_Series_520i_Luxury_Line.htm', 'https://www.cardekho.com/overview/BMW_5_Series/BMW_5_Series_520d_M_Sport.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_D4_KINETIC.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_220_CDI_Style.htm', 'https://www.cardekho.com/overview/BMW_7_Series/BMW_7_Series_730Ld_Design_Pure_Excellence.htm', 'https://www.cardekho.com/overview/Audi_A6/Audi_A6_35_TDI.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_60_TFSI_Quattro.htm', 'https://www.cardekho.com/overview/BMW_7_Series/BMW_7_Series_750Li_Design_Pure_Excellence_CBU.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E250_Edition_E.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Ghost/Rolls-Royce_Ghost_Series_II_Standard.htm', 'https://www.cardekho.com/overview/Volvo_S60_Cross_Country/Volvo_S60_Cross_Country_D4_AWD.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320d.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S400.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Drophead_Coupe.htm', 'https://www.cardekho.com/overview/Audi_RS6/Audi_RS6_4.0_TFSI.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M4_Coupe.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320d_M_Sport.htm', 'https://www.cardekho.com/overview/Jaguar_XE/Jaguar_XE_Prestige.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_50_TDI_Quattro.htm', 'https://www.cardekho.com/overview/BMW_5_Series/BMW_5_Series_520d_Luxury_Line.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E350_Edition_E.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M6_Gran_Coupe.htm', 'https://www.cardekho.com/overview/Bentley_Flying_Spur/Bentley_Flying_Spur_W12.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_Turbo_S.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Extended_Wheelbase.htm', 'https://www.cardekho.com/overview/BMW_6_Series/BMW_6_Series_640d_Design_Pure_Experience.htm', 'https://www.cardekho.com/overview/Volvo_S_80/Volvo_S_80_D5.htm', 'https://www.cardekho.com/overview/Volvo_S_80/Volvo_S_80_D4.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_200_CGI.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_D5_Inscription.htm', 'https://www.cardekho.com/overview/BMW_7_Series/BMW_7_Series_730Ld_M_Sport.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E_63_AMG.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_350_CDI.htm', 'https://www.cardekho.com/overview/Jaguar_XJ/Jaguar_XJ_3.0L_Premium_Luxury.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_Diesel_250hp.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E200_Edition_E.htm', 'https://www.cardekho.com/overview/BMW_5_Series/BMW_5_Series_530d_M_Sport.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_Guard.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320d_Sport.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_500_Coupe.htm', 'https://www.cardekho.com/overview/Jaguar_XE/Jaguar_XE_Pure.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_R_Supercharged_5.0_Litre_V8_Petrol.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_2.0_Diesel_Pure.htm', 'https://www.cardekho.com/overview/BMW_5_Series/BMW_5_Series_520d_Prestige_Plus.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_Maybach_S600_Guard.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M3_Sedan.htm', 'https://www.cardekho.com/overview/BMW_6_Series/BMW_6_Series_640d_Eminence.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M5_Sedan.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_2.0_Diesel_Portfolio.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Phantom.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Ghost/Rolls-Royce_Ghost_Series_II_Extended_Wheelbase.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E400_Cabriolet.htm', 'https://www.cardekho.com/overview/Maserati_Quattroporte/Maserati_Quattroporte_GTS.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_50_TDI_Quattro_Premium_Plus.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_63_AMG.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_63_S_AMG.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_X5_M.htm', 'https://www.cardekho.com/overview/Audi_S5/Audi_S5_Sportback.htm', 'https://www.cardekho.com/overview/Jaguar_XJ/Jaguar_XJ_2.0L_Portfolio.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_T6.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_Base.htm', 'https://www.cardekho.com/overview/Bentley_Flying_Spur/Bentley_Flying_Spur_V8.htm', 'https://www.cardekho.com/overview/Bentley_Mulsanne/Bentley_Mulsanne_6.8.htm', 'https://www.cardekho.com/overview/Jaguar_XJ/Jaguar_XJ_3.0L_Portfolio.htm', 'https://www.cardekho.com/overview/Jaguar_XE/Jaguar_XE_Portfolio.htm', 'https://www.cardekho.com/overview/Audi_A6/Audi_A6_35_TFSI_Matrix.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_63_AMG_Coupe.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Coupe.htm']
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

pickle.dump(prices, open("price_luxury.p", "wb"))
pickle.dump(failed, open("failed.p", "wb"))
