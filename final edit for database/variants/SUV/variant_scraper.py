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
#####pickle.dump({1: 2},open("variant_suv_output.p","wb"))##################
###################################################################

g=pickle.load(open("variant_suv_output.p","rb"))
fail=[]
#################################################################################################


variants_dict = ['https://www.cardekho.com/overview/Ford_Ecosport/Ford_Ecosport_1.5_TDCi_Trend.htm']
driver = webdriver.Chrome()
flag=267
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
		pickle.dump(g,open("variant_suv_output.p","wb"))
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