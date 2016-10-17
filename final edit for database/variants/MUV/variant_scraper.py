from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import datetime

print datetime.datetime.now()

###################################################################
pickle.dump({1: 2},open("variant_muv_output.p","wb"))##################
###################################################################

g=pickle.load(open("variant_muv_output.p","rb"))
fail=[]
#################################################################################################


variants_dict = ['https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_DI_Non-Ac_9Seater_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_GX_(Diesel)_7_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_V_i-VTEC.htm', 'https://www.cardekho.com/overview/Tata_Aria/Tata_Aria_Pleasure_4x2.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_9_Str_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_GX_(Diesel)_8_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_World_Edition_110PS.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_ZX_Diesel_7_Seater.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_Van_BSIII_Non_AC.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_7_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D2_Maxx_BSIV.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_E_i-VTEC.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D4.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_A_EPS.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D2_BS_IV.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_SD_CRDFi_9Seater_BSIV.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_10_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_S_i-VTEC.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_7_C_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_GX_MT_8S.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_V_Option_i-VTEC.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_GX_MT.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_DI_PS_AC_9Seater_BSIII.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_SHVS_ZDI_Plus.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_RS_Option_i-DTEC.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LT_8.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_SHVS_LDI.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LT_7.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D2_Maxx.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_G_MT.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_GX_MT_8S.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_V_i-DTEC.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_SD_DI_9Seater_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_VX_MT.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_VX_(Diesel)_8_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_S_i-DTEC.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_B_Class/Mercedes-Benz_B_Class_B180_Sport.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_G_MT_8S.htm', 'https://www.cardekho.com/overview/Tata_Aria/Tata_Aria_Pride_4x4.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_VX_MT.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_85PS_Std.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.8_GX_AT_8S.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_Max_10_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LTZ_8.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LS_8.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LS_7.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LTZ_7.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_E_i-DTEC.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_H4_ABS.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_SHVS_ZDI.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_H8.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_H4.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_85PS_RxE_7_Seater.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LT_9_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_GX_MT.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D2_BS_III.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LS_7.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LS_8.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_ZX_MT.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_RS_i-DTEC.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_CRDFi_PS_AC_9Seater_BSIII.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_SD_CRDFi_9Seater_BSIII.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_Style.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_T_Option.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_VD_DI_7Seater_BSIII.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_SHVS_LDI_Option.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_LS_10_Seats_BSIII.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.8_GX_AT.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_CRDFi_AC_M_Stg_9Seater_BSIV.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_LXI_Option.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.4_VX_MT_8S.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LT_7.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_CRDFi_Non-AC_9Seater_BSIV.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.3_TCDi_LT_8.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LTZ_7.htm', 'https://www.cardekho.com/overview/Chevrolet_Enjoy/Chevrolet_Enjoy_1.4_LTZ_8.htm', 'https://www.cardekho.com/overview/Tata_Aria/Tata_Aria_Pure_LX_4x2.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_G_(Diesel)_8_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_GX_AT_8S.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_ZX_AT.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_Van_BSIII_AC.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_D4_BS_III.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.8_ZX_AT.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_85PS_RxE.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_85PS_RxL.htm', 'https://www.cardekho.com/overview/Renault_Lodgy/Renault_Lodgy_World_Edition_85PS.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_Ambulance_DI_Non_AC_BSIII.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_Ambulance_DI_AC_BSIII.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_VD_CRDFi_7Seater_BSIII.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_Max_9_Str_BSIII.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_LD_CRDFi_PS_AC_9Seater_BSIV.htm', 'https://www.cardekho.com/overview/Honda_Mobilio/Honda_Mobilio_V_Option_i-DTEC.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_LXI.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_VX_(Diesel)_7_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_T.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_VXI_CNG.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_B_Class/Mercedes-Benz_B_Class_B200_CDI_Sport.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_A.htm', 'https://www.cardekho.com/overview/Datsun_GO_Plus/Datsun_GO_Plus_D.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_VXI_AT.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_ZXI_Plus.htm', 'https://www.cardekho.com/overview/Chevrolet_Tavera/Chevrolet_Tavera_Neo_3_9_Str_BSIII.htm', 'https://www.cardekho.com/overview/Tata_Xenon_XT/Tata_Xenon_XT_EX_4X4.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_ZXI.htm', 'https://www.cardekho.com/overview/Tata_Xenon_XT/Tata_Xenon_XT_EX_4X2.htm', 'https://www.cardekho.com/overview/Toyota_Innova/Toyota_Innova_2.5_G_(Diesel)_7_Seater_BS_IV.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_VXI.htm', 'https://www.cardekho.com/overview/Toyota_Innova_Crysta/Toyota_Innova_Crysta_2.7_GX_AT.htm', 'https://www.cardekho.com/overview/Mahindra_Xylo/Mahindra_Xylo_H8_ABS_with_Airbags.htm', 'https://www.cardekho.com/overview/ICML_Extreme/ICML_Extreme_VD_CRDFi_7Seater_BSIV.htm', 'https://www.cardekho.com/overview/Maruti_Ertiga/Maruti_Ertiga_SHVS_VDI.htm']
driver = webdriver.Chrome()
flag=0
for link in variants_dict:	
	try:
		q=time.time()
		output={}
		glink=link
		if(len(fail)>0):
			print "Couldnot obtain the details of ",len(fail)," cars"
		print ""
		print "Fetching the details of ",glink.split('/')[5].replace('_',' ').replace('.htm','')
		a=[]
		driver.get(link)

		#!!!!!print "Review"
		#!!!!!print link


		output['Review_link']=link
		

		WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//section[@id='variantwrap']")))

		for k in  driver.find_elements_by_xpath("//section[@id='variantwrap']"):
			#!!!!!print k.text
			a.append(k.text)


		output['Review']=a


		original = link
		s = link.split("/")
		s[3] = 'specs'
		link = '/'.join(s)
		link = link[:-4] + "-specification.htm"
		#!!!!!print "####################################################################################"
		#!!!!!print link
		

		output['Specs_link']=link


		driver.get(link)
	  #driver.switch_to.default_content()
		# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "a[title*='" + user_input + "']"))).click()



		############################################################################################################################

		#category = {}
		#techf_collection = driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//h3")
		#details = driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li")

		'''for count, i1 in enumerate(techf_collection):
			i1.text
		print "END"'''


		'''# Displays technical specs
		for count, i1 in enumerate(techf_collection):
			try:
				catg = i1.get_attribute('title').encode('UTF8')
				print 'catg', catg
			except Exception as e:
				pass
			#tr = techf_collection[li].find_elements_by_tag_name('tr')'''

		#IMPLICIT WAIT !!
		#driver.implicitly_wait(10)
		specs = {}


		#details_specs = driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li")

		WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li")))

		for i,j in zip(driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li//div[@class='compareleft textalignunset']"),driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li//div[contains(@class,'compareright')]")):
			if(j.text != '-'):
				#!!!!!!!!georgyprint i.text, '-->', j.text
				#category.setdefault(i.text.encode('UTF8')).append(j.text.encode('UTF8'))
				specs[i.text.encode('UTF8')] = j.text.encode('UTF8')
		'''if(i.get_attribute('title') != ''):
				print i.get_attribute('title')
			if(i.text != ''):
				print i.text, j.text
			'''

			#category.setdefault(catg, []).append(specs)


	############################################################################################################################

		#!!!!!print "Specifications"
		#!!!!!print specs


		output['Specs']=specs


		link = original
		s = link.split("/")
		s[3] = 'features'
		link = '/'.join(s)
		link = link[:-4] + "-features.htm"
		#!!!!!print "####################################################################################"
		#!!!!!print link


		output['Features_link']=link


		driver.get(link)


		features = {}

		WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li")))
		#details_fe = driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li")
		for i,j in zip(driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li//div[@class='compareleft textalignunset']"),driver.find_elements_by_xpath("//div[@class='specinner']//div[@id = 'open-by-default-example']//div//ul//li//div[contains(@class,'compareright')]//div[@class='W50Percent']")):
			if('has not' not in j.get_attribute("title")):
				#!!!!!!!!georgyprint i.text, '-->', 'Yes'
				features[i.text.encode('UTF8')] = 'Yes'
				#category.setdefault(i.text.encode('UTF8')).append(j.text.encode('UTF8'))

		#!!!!!print "Features"
		#!!!!!print features


		output['Features']=features
		for i in output.keys():
			print ""
			print i
			print output[i]
		"""










						WRITE THE CODE TO TAKE THE LINK OF PHOTOS............
						THEN ADD IT AS output['photos']=[link1,link2,link3,..........,linkn]












		"""
		g[flag]=output
		pickle.dump(g,open("variant_muv_output.p","wb"))
		flag+=1
		print ""
		print "Time taken= ",time.time()-q," seconds"
		print "Completed= ",flag,"/",len(variants_dict)
		print "Percentage completed= ",flag*100/(float(len(variants_dict)))
		print ""

	except:
		print ""
		driver.close()
		print "Coutldnot obtain the details of ",glink
		fail.append(glink)
		print "Moving to next car "
		#time.sleep(5)
		driver = webdriver.Chrome()
		flag+=1
		print ""
		print "Time taken= ",time.time()-q," seconds"
		print "Completed= ",flag,"/",len(variants_dict)
		print "Percentage completed= ",flag*100/float(len(variants_dict))
		print ""


# print
# print "Time taken = ",time.time()-q," seconds"

driver.close()
print ""
print ""
print ""
print "Failed to obtain the details of the following cars"
pickle.dump(fail,open("fail.p","wb"))
for z in fail:
	print z