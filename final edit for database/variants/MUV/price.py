from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
from bs4 import BeautifulSoup
import urllib
import re

links = ['https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_DI_Non-Ac_9Seater_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_GX_(Diesel)_7_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_V_i-VTEC.htm', 'https://www.cardekho.com/overview/Tata_Aria/Tata_Aria_Pleasure_4x2.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_9_Str_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_GX_(Diesel)_8_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_World_Edition_110PS.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_ZX_Diesel_7_Seater.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_Van_BSIII_Non_AC.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_7_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D2_Maxx_BSIV.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_E_i-VTEC.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D4.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_A_EPS.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D2_BS_IV.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_SD_CRDFi_9Seater_BSIV.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_10_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_S_i-VTEC.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_7_C_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_GX_MT_8S.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_V_Option_i-VTEC.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_GX_MT.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_DI_PS_AC_9Seater_BSIII.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_SHVS_ZDI_Plus.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_RS_Option_i-DTEC.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LT_8.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_SHVS_LDI.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LT_7.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D2_Maxx.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_G_MT.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_GX_MT_8S.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_V_i-DTEC.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_SD_DI_9Seater_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_VX_MT.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_VX_(Diesel)_8_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_S_i-DTEC.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_B_Class/Mercedes-Benz_B_Class_B180_Sport.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_G_MT_8S.htm', 'https://www.cardekho.com/overview/Tata_Aria/Tata_Aria_Pride_4x4.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_VX_MT.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_85PS_Std.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.8_GX_AT_8S.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_Max_10_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LTZ_8.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LS_8.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LS_7.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LTZ_7.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_E_i-DTEC.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_H4_ABS.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_SHVS_ZDI.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_H8.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_H4.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_85PS_RxE_7_Seater.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LT_9_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_GX_MT.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D2_BS_III.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LS_7.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LS_8.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_ZX_MT.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_RS_i-DTEC.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_CRDFi_PS_AC_9Seater_BSIII.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_SD_CRDFi_9Seater_BSIII.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_Style.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_T_Option.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_VD_DI_7Seater_BSIII.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_SHVS_LDI_Option.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_10_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.8_GX_AT.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_CRDFi_AC_M_Stg_9Seater_BSIV.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_LXI_Option.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_VX_MT_8S.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LT_7.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_CRDFi_Non-AC_9Seater_BSIV.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LT_8.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LTZ_7.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LTZ_8.htm', 'https://www.cardekho.com/overview/Tata_Aria/Tata_Aria_Pure_LX_4x2.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_G_(Diesel)_8_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_GX_AT_8S.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_ZX_AT.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_Van_BSIII_AC.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D4_BS_III.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.8_ZX_AT.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_85PS_RxE.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_85PS_RxL.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_World_Edition_85PS.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_Ambulance_DI_Non_AC_BSIII.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_Ambulance_DI_AC_BSIII.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_VD_CRDFi_7Seater_BSIII.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_Max_9_Str_BSIII.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_CRDFi_PS_AC_9Seater_BSIV.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_V_Option_i-DTEC.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_LXI.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_VX_(Diesel)_7_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_T.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_VXI_CNG.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_B_Class/Mercedes-Benz_B_Class_B200_CDI_Sport.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_A.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_D.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_VXI_AT.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_ZXI_Plus.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_9_Str_BSIII.htm', 'https://www.cardekho.com/overview/Tata_Xenon_XT/Tata_Xenon_XT_EX_4X4.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_ZXI.htm', 'https://www.cardekho.com/overview/Tata_Xenon_XT/Tata_Xenon_XT_EX_4X2.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_G_(Diesel)_7_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_VXI.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_GX_AT.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_H8_ABS_with_Airbags.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_VD_CRDFi_7Seater_BSIV.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_SHVS_VDI.htm']
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

pickle.dump(prices, open("price_MUV.p", "wb"))
pickle.dump(failed, open("failed.p", "wb"))
