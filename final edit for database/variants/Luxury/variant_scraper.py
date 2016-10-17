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
pickle.dump({1: 2},open("variant_luxury_output.p","wb"))##################
###################################################################

g=pickle.load(open("variant_luxury_output.p","rb"))
fail=[]
#################################################################################################


variants_dict = ['https://www.cardekho.com/overview/Aston_Martin_Rapide/Aston_Martin_Rapide_S_V12.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_Maybach_S600.htm', 'https://www.cardekho.com/overview/Maserati_Ghibli/Maserati_Ghibli_Diesel.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320d_Luxury_Line.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320i_Prestige.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_4.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E350_CDI_Avantgrade.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_X6_M.htm', 'https://www.cardekho.com/overview/Maserati_Quattroporte/Maserati_Quattroporte_Diesel.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_Turbo.htm', 'https://www.cardekho.com/overview/BMW_7_Series/BMW_7_Series_750Li_M_Sport_CBU.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_CLS-Class/Mercedes-Benz_CLS-Class_250_CDI.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_W12_quattro.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E_200_CGI.htm', 'https://www.cardekho.com/overview/Audi_A6/Audi_A6_35_TFSI.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E250_CDI_Avantgarde.htm', 'https://www.cardekho.com/overview/BMW_7_Series/BMW_7_Series_730Ld_Design_Pure_Excellence_CBU.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_60_TDI_Quattro.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_2.0_Petrol_Portfolio.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_Security.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_2.0_Diesel_Prestige.htm', 'https://www.cardekho.com/overview/Audi_A4/Audi_A4_30_TFSI_Premium_Plus.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_220_CDI_Avantgarde.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_Maybach_S500.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_2.0_Petrol_Prestige.htm', 'https://www.cardekho.com/overview/Audi_A4/Audi_A4_30_TFSI_Technology.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_GTS.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_Diesel.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_D4_Momentum.htm', 'https://www.cardekho.com/overview/Audi_RS7/Audi_RS7_Sportback.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320i_Luxury_Line.htm', 'https://www.cardekho.com/overview/BMW_5_Series/BMW_5_Series_520i_Luxury_Line.htm', 'https://www.cardekho.com/overview/BMW_5_Series/BMW_5_Series_520d_M_Sport.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_D4_KINETIC.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_220_CDI_Style.htm', 'https://www.cardekho.com/overview/BMW_7_Series/BMW_7_Series_730Ld_Design_Pure_Excellence.htm', 'https://www.cardekho.com/overview/Audi_A6/Audi_A6_35_TDI.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_60_TFSI_Quattro.htm', 'https://www.cardekho.com/overview/BMW_7_Series/BMW_7_Series_750Li_Design_Pure_Excellence_CBU.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E250_Edition_E.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Ghost/Rolls-Royce_Ghost_Series_II_Standard.htm', 'https://www.cardekho.com/overview/Volvo_S60_Cross_Country/Volvo_S60_Cross_Country_D4_AWD.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320d.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S400.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Drophead_Coupe.htm', 'https://www.cardekho.com/overview/Audi_RS6/Audi_RS6_4.0_TFSI.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M4_Coupe.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320d_M_Sport.htm', 'https://www.cardekho.com/overview/Jaguar_XE/Jaguar_XE_Prestige.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_50_TDI_Quattro.htm', 'https://www.cardekho.com/overview/BMW_5_Series/BMW_5_Series_520d_Luxury_Line.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E350_Edition_E.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M6_Gran_Coupe.htm', 'https://www.cardekho.com/overview/Bentley_Flying_Spur/Bentley_Flying_Spur_W12.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_Turbo_S.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Extended_Wheelbase.htm', 'https://www.cardekho.com/overview/BMW_6_Series/BMW_6_Series_640d_Design_Pure_Experience.htm', 'https://www.cardekho.com/overview/Volvo_S_80/Volvo_S_80_D5.htm', 'https://www.cardekho.com/overview/Volvo_S_80/Volvo_S_80_D4.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_200_CGI.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_D5_Inscription.htm', 'https://www.cardekho.com/overview/BMW_7_Series/BMW_7_Series_730Ld_M_Sport.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E_63_AMG.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_350_CDI.htm', 'https://www.cardekho.com/overview/Jaguar_XJ/Jaguar_XJ_3.0L_Premium_Luxury.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_Diesel_250hp.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E200_Edition_E.htm', 'https://www.cardekho.com/overview/BMW_5_Series/BMW_5_Series_530d_M_Sport.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_Guard.htm', 'https://www.cardekho.com/overview/BMW_3_Series/BMW_3_Series_320d_Sport.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_500_Coupe.htm', 'https://www.cardekho.com/overview/Jaguar_XE/Jaguar_XE_Pure.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_R_Supercharged_5.0_Litre_V8_Petrol.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_2.0_Diesel_Pure.htm', 'https://www.cardekho.com/overview/BMW_5_Series/BMW_5_Series_520d_Prestige_Plus.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_Maybach_S600_Guard.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M3_Sedan.htm', 'https://www.cardekho.com/overview/BMW_6_Series/BMW_6_Series_640d_Eminence.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_M5_Sedan.htm', 'https://www.cardekho.com/overview/Jaguar_XF/Jaguar_XF_2.0_Diesel_Portfolio.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Phantom.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Ghost/Rolls-Royce_Ghost_Series_II_Extended_Wheelbase.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E400_Cabriolet.htm', 'https://www.cardekho.com/overview/Maserati_Quattroporte/Maserati_Quattroporte_GTS.htm', 'https://www.cardekho.com/overview/Audi_A8/Audi_A8_L_50_TDI_Quattro_Premium_Plus.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_63_AMG.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_New_C-Class/Mercedes-Benz_New_C-Class_C_63_S_AMG.htm', 'https://www.cardekho.com/overview/BMW_M_Series/BMW_M_Series_X5_M.htm', 'https://www.cardekho.com/overview/Audi_S5/Audi_S5_Sportback.htm', 'https://www.cardekho.com/overview/Jaguar_XJ/Jaguar_XJ_2.0L_Portfolio.htm', 'https://www.cardekho.com/overview/Volvo_S60/Volvo_S60_T6.htm', 'https://www.cardekho.com/overview/Porsche_Panamera/Porsche_Panamera_Base.htm', 'https://www.cardekho.com/overview/Bentley_Flying_Spur/Bentley_Flying_Spur_V8.htm', 'https://www.cardekho.com/overview/Bentley_Mulsanne/Bentley_Mulsanne_6.8.htm', 'https://www.cardekho.com/overview/Jaguar_XJ/Jaguar_XJ_3.0L_Portfolio.htm', 'https://www.cardekho.com/overview/Jaguar_XE/Jaguar_XE_Portfolio.htm', 'https://www.cardekho.com/overview/Audi_A6/Audi_A6_35_TFSI_Matrix.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_S-Class/Mercedes-Benz_S-Class_S_63_AMG_Coupe.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Coupe.htm']
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
		pickle.dump(g,open("variant_luxury_output.p","wb"))
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