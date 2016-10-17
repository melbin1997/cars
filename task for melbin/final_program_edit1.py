from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import datetime

print datetime.datetime.now()
print ""
p=time.time()
q = time.time()

d=['Fiat 500', 'Fiat Abarth Avventura', 'Fiat Avventura', 'Fiat Avventura Urban Cross', 'Fiat Punto EVO', 'Fiat Linea', 'Fiat Linea Classic', 'Fiat Abarth Punto', 'Fiat Punto Pure', 'Lamborghini Aventador', 'Lamborghini Huracan', 'Maserati Ghibli', 'Maserati Gran Cabrio', 'Maserati Gran Turismo', 'Maserati Quattroporte', 'Renault Duster', 'Renault KWID', 'Renault Lodgy', 'Renault Pulse', 'Renault Scala', 'ICML Extreme', 'Jeep Grand Cherokee', 'Jeep Wrangler Unlimited', 'Chevrolet Beat', 'Chevrolet Cruze', 'Chevrolet Enjoy', 'Chevrolet Sail', 'Chevrolet Sail Hatchback', 'Chevrolet Spark', 'Chevrolet Tavera', 'Chevrolet Trailblazer', 'Nissan Micra Active', 'Nissan Micra', 'Nissan Sunny', 'Nissan Terrano', 'Porsche 911', 'Porsche Boxster', 'Porsche Cayenne', 'Porsche Cayman', 'Porsche Macan', 'Porsche Panamera', 'Tata Aria', 'Tata Bolt', 'Tata Indica eV2', 'Tata Indigo eCS', 'Tata Nano', 'Tata Safari', 'Tata Safari Storme', 'Tata Sumo', 'Tata Tiago', 'Tata Xenon XT', 'Tata Zest', 'DC Avanti', 'Maruti Alto 800', 'Maruti Alto K10', 'Maruti Baleno', 'Maruti Celerio', 'Maruti Ciaz', 'Maruti Eeco', 'Maruti Ertiga', 'Maruti Gypsy', 'Maruti Omni', 'Maruti Ritz', 'Maruti Swift', 'Maruti Swift Dzire', 'Maruti S-Cross', 'Maruti Vitara Brezza', 'Maruti Wagon R', 'Maruti Wagon R Stingray', 'Volvo S80', 'Volvo S60 Cross Country', 'Volvo S60', 'Volvo V40 Cross Country', 'Volvo V40', 'Volvo XC90', 'Volvo XC60', 'Honda Amaze', 'Honda BRV', 'Honda Brio', 'Honda City', 'Honda CR-V', 'Honda Jazz', 'Honda Mobilio', 'Ferrari 458 Speciale', 'Ferrari 488', 'Ferrari California T', 'Ferrari F12berlinetta', 'Ferrari FF', 'Mahindra Bolero', 'Mahindra E Verito', 'Mahindra e2o', 'Mahindra KUV100', 'Mahindra NuvoSport', 'Mahindra Quanto', 'Mahindra Scorpio', 'Mahindra Supro', 'Mahindra Thar', 'Mahindra TUV 300', 'Mahindra Verito', 'Mahindra Verito Vibe', 'Mahindra XUV500', 'Mahindra Xylo', 'Mercedes-Benz A-Class', 'Mercedes-Benz AMG GT', 'Mercedes-Benz B-Class', 'Mercedes-Benz CLA', 'Mercedes-Benz CLS', 'Mercedes-Benz E-Class', 'Mercedes-Benz G-Class', 'Mercedes-Benz GL-Class', 'Mercedes-Benz GLA 45 AMG', 'Mercedes-Benz GLA Class', 'Mercedes-Benz GLC', 'Mercedes-Benz GLE', 'Mercedes-Benz GLS', 'Mercedes-Benz M-Class', 'Mercedes-Benz C-Class', 'Mercedes-Benz S-Class', 'Mercedes-Benz SLC', 'Jaguar F-Type', 'Jaguar XE', 'Jaguar XF', 'Jaguar XJ', 'Volkswagen Ameo', 'Volkswagen Beetle', 'Volkswagen CrossPolo', 'Volkswagen Jetta', 'Volkswagen Polo', 'Volkswagen Vento', 'Toyota Camry', 'Toyota Corolla Altis', 'Toyota Platinum Etios', 'Toyota Etios Cross', 'Toyota Etios Liva', 'Toyota Fortuner', 'Toyota Innova', 'Toyota Innova Crysta', 'Toyota Land Cruiser', 'Toyota Land Cruiser Prado', 'Toyota Prius', 'Rolls-Royce Dawn', 'Rolls-Royce Ghost', 'Rolls-Royce Phantom', 'Rolls-Royce Wraith', 'Mahindra Ssangyong Rexton', 'Mini 3 DOOR', 'Mini 5 DOOR', 'Mini Cooper Convertible', 'Mini Countryman', 'Force Gurkha', 'Force One SUV', 'Bentley Bentayga', 'Bentley Continental', 'Bentley Flying Spur', 'Bentley Mulsanne', 'Isuzu D-Max V-Cross', 'Isuzu MU 7', 'Aston Martin DB11', 'Aston Martin Rapide', 'Aston Martin Vanquish', 'Aston Martin Vantage', 'Skoda Octavia', 'Skoda Rapid', 'Skoda Superb', 'Skoda Yeti', 'Conquest Evade', 'Premier Rio', 'Hyundai Creta', 'Hyundai Elantra', 'Hyundai EON', 'Hyundai Grand i10', 'Hyundai i10', 'Hyundai Elite i20', 'Hyundai i20 Active', 'Hyundai Santa Fe', 'Hyundai Verna', 'Hyundai Xcent', 'Ford EcoSport', 'Ford Endeavour', 'Ford Figo', 'Ford Aspire', 'Ford Mustang', 'Land Rover Discovery 4', 'Land Rover Discovery Sport', 'Land Rover Range Rover', 'Land Rover Range Rover Evoque', 'Land Rover Range Rover Sport', 'Datsun GO', 'Datsun GO Plus', 'Datsun Redi GO', 'BMW 1 Series', 'BMW 3 Series', 'BMW 5 Series', 'BMW 6 Series', 'BMW 7 Series', 'BMW i8', 'BMW M Series', 'BMW X1', 'BMW X3', 'BMW X5', 'BMW X6', 'BMW Z4', 'Mitsubishi Pajero Sport', 'Bugatti Veyron', 'Audi A3', 'Audi A3 cabriolet', 'Audi A4', 'Audi A6', 'Audi A8', 'Audi Q3', 'Audi Q5', 'Audi Q7', 'Audi R8', 'Audi RS6 Avant', 'Audi RS7', 'Audi S5', 'Audi TT']
g13=1

g12=1
for g10 in d:
    q=time.time()
    user_input = g10
    driver = webdriver.Chrome()
    driver.get("https://www.cardekho.com/")
    car_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cardekhosearchtext")))
    car_name.clear()
    car_name.send_keys(user_input)
    car_name.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.switch_to.default_content()
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "a[title*='" + user_input + "']"))).click()
    driver.find_element_by_css_selector("a[title*='" + user_input + "']").click()

    driver.find_element_by_css_selector("a[href*='specification']").click()


    ############################################################################################################################


    category = {}
    keyf_collection = driver.find_elements_by_xpath("//table[@class='keyfeature']/tbody/tr")
    key_specs = {}

    # Displays key features
    for elem in range(len(keyf_collection)):
        td = keyf_collection[elem].find_elements_by_tag_name('td')
        for index, i in enumerate(td):
            # Even numbers are the keys and Odd numbers are the values
            if index % 2 == 1:
                key_specs[td[index - 1].text.encode('UTF8')] = i.text.encode('UTF8')
    category.setdefault('Key Specs', []).append(key_specs)


    ############################################################################################################################



    techf_collection = driver.find_elements_by_xpath("//div[@class='specinner']/div/table")

    # Displays technical specs
    for li in range(len(techf_collection)):
        catg = techf_collection[li].find_elements_by_xpath("//div[@class='specinner']/div/table//th")[li].get_attribute(
            'title').encode('UTF8')
        tr = techf_collection[li].find_elements_by_tag_name('tr')
        specs = {}
        for i in range(len(tr)):
            td = tr[i].find_elements_by_tag_name('td')
            for index, j in enumerate(td):
                # Even numbers are the keys and Odd numbers are the values
                if index % 2 == 1:
                    if 'has not' in j.get_attribute('title'):
                        specs[td[index - 1].text.encode('UTF8')] = 'False'
                    elif 'has' in j.get_attribute('title'):
                        specs[td[index - 1].text.encode('UTF8')] = 'True'
                    else:
                        specs[td[index - 1].text.encode('UTF8')] = j.text.encode('UTF8')
        category.setdefault(catg, []).append(specs)
    car = {user_input: category}
    g11=pickle.load(open("output.p","rb"))
    g11[user_input]=car
    pickle.dump(g11,open("output.p","wb"))


    ############################################################################################################################


    # print category
    print ""
    print car
    print ""
    print "Time taken= ",time.time()-q," seconds"
    print "Data accured= ",g12,"/",g13
    print "Percentage completed= ",g12*100/float(g13)
    g12+=1
    # print
    # print "Time taken = ",time.time()-q," seconds"

    driver.close()
print ""
print "Task completed"
print datetime.datetime.now()