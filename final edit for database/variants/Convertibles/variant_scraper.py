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
pickle.dump({1: 2},open("variant_convertibles_output.p","wb"))##################
###################################################################

g=pickle.load(open("variant_convertibles_output.p","rb"))
fail=[]
#################################################################################################


variants_dict = ['https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E350_Edition_E.htm', 'https://www.cardekho.com/overview/Bugatti_Veyron/Bugatti_Veyron_16.4_Grand_Sport.htm', 'https://www.cardekho.com/overview/Jaguar_F_Type/Jaguar_F_Type_S_Coupe.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Phantom.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E400_Cabriolet.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Extended_Wheelbase.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_V8_S_Convertible.htm', 'https://www.cardekho.com/overview/Jaguar_F_Type/Jaguar_F_Type_Coupe.htm', 'https://www.cardekho.com/overview/Audi_A3_cabriolet/Audi_A3_cabriolet_40_TFSI_Premium_Plus.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Carrera_S.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Turbo.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_SLC/Mercedes-Benz_SLC_43_AMG.htm', 'https://www.cardekho.com/overview/Jaguar_F_Type/Jaguar_F_Type_3.0_V6_S.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E350_CDI_Avantgrade.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Turbo_S_Cabriolet.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_V8_Convertible.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E_63_AMG.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E_200_CGI.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Dawn/Rolls-Royce_Dawn_Convertible.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E200_Edition_E.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_V8.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E250_CDI_Avantgarde.htm', 'https://www.cardekho.com/overview/Jaguar_F_Type/Jaguar_F_Type_R_Coupe.htm', 'https://www.cardekho.com/overview/Mercedes-Benz_E-Class/Mercedes-Benz_E-Class_E250_Edition_E.htm', 'https://www.cardekho.com/overview/BMW_Z4/BMW_Z4_35i_DPT.htm', 'https://www.cardekho.com/overview/BMW_Z4/BMW_Z4_35i.htm', 'https://www.cardekho.com/overview/Jaguar_F_Type/Jaguar_F_Type_5.0_V8_S.htm', 'https://www.cardekho.com/overview/Maserati_Gran_Cabrio/Maserati_Gran_Cabrio_4.7_V8.htm', 'https://www.cardekho.com/overview/Lamborghini_Aventador/Lamborghini_Aventador_Roadster_LP_700_4.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Carrera_Cabriolet.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Carrera.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_Speed_Convertible.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GTC.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Drophead_Coupe.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Turbo_S.htm', 'https://www.cardekho.com/overview/Porsche_Boxster/Porsche_Boxster_S.htm', 'https://www.cardekho.com/overview/Mini_Cooper_Convertible/Mini_Cooper_Convertible_S.htm', 'https://www.cardekho.com/overview/Porsche_Boxster/Porsche_Boxster_GTS.htm', 'https://www.cardekho.com/overview/Ferrari_California/Ferrari_California_T.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT.htm', 'https://www.cardekho.com/overview/Lamborghini_Aventador/Lamborghini_Aventador_LP700_4.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_Speed.htm', 'https://www.cardekho.com/overview/Bentley_Continental/Bentley_Continental_GT_V8_S.htm', 'https://www.cardekho.com/overview/Rolls-Royce_Phantom/Rolls-Royce_Phantom_Coupe.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Carrera_S_Cabriolet.htm', 'https://www.cardekho.com/overview/Porsche_911/Porsche_911_Turbo_Cabriolet.htm']
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
		pickle.dump(g,open("variant_convertibles_output.p","wb"))
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