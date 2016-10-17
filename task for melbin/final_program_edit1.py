from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import datetime

cars =['Fiat 500', 'Fiat Abarth Avventura', 'Fiat Avventura', 'Fiat Avventura Urban Cross', 'Fiat Punto EVO', 'Fiat Linea', 'Fiat Linea Classic', 'Fiat Abarth Punto', 'Fiat Punto Pure', 'Lamborghini Aventador', 'Lamborghini Huracan', 'Maserati Ghibli', 'Maserati Gran Cabrio', 'Maserati Gran Turismo', 'Maserati Quattroporte', 'Renault Duster', 'Renault KWID', 'Renault Lodgy', 'Renault Pulse', 'Renault Scala', 'ICML Extreme', 'Jeep Grand Cherokee', 'Jeep Wrangler Unlimited', 'Chevrolet Beat', 'Chevrolet Cruze', 'Chevrolet Enjoy', 'Chevrolet Sail', 'Chevrolet Sail Hatchback', 'Chevrolet Spark', 'Chevrolet Tavera', 'Chevrolet Trailblazer', 'Nissan Micra Active', 'Nissan Micra', 'Nissan Sunny', 'Nissan Terrano', 'Porsche 911', 'Porsche Boxster', 'Porsche Cayenne', 'Porsche Cayman', 'Porsche Macan', 'Porsche Panamera', 'Tata Aria', 'Tata Bolt', 'Tata Indica eV2', 'Tata Indigo eCS', 'Tata Nano', 'Tata Safari', 'Tata Safari Storme', 'Tata Sumo', 'Tata Tiago', 'Tata Xenon XT', 'Tata Zest', 'DC Avanti', 'Maruti Alto 800', 'Maruti Alto K10', 'Maruti Baleno', 'Maruti Celerio', 'Maruti Ciaz', 'Maruti Eeco', 'Maruti Ertiga', 'Maruti Gypsy', 'Maruti Omni', 'Maruti Ritz', 'Maruti Swift', 'Maruti Swift Dzire', 'Maruti S-Cross', 'Maruti Vitara Brezza', 'Maruti Wagon R', 'Maruti Wagon R Stingray', 'Volvo S80', 'Volvo S60 Cross Country', 'Volvo S60', 'Volvo V40 Cross Country', 'Volvo V40', 'Volvo XC90', 'Volvo XC60', 'Honda Amaze', 'Honda BRV', 'Honda Brio', 'Honda City', 'Honda CR-V', 'Honda Jazz', 'Honda Mobilio', 'Ferrari 458 Speciale', 'Ferrari 488', 'Ferrari California T', 'Ferrari F12berlinetta', 'Ferrari FF', 'Mahindra Bolero', 'Mahindra E Verito', 'Mahindra e2o', 'Mahindra KUV100', 'Mahindra NuvoSport', 'Mahindra Quanto', 'Mahindra Scorpio', 'Mahindra Supro', 'Mahindra Thar', 'Mahindra TUV 300', 'Mahindra Verito', 'Mahindra Verito Vibe', 'Mahindra XUV500', 'Mahindra Xylo', 'Mercedes-Benz A-Class', 'Mercedes-Benz AMG GT', 'Mercedes-Benz B-Class', 'Mercedes-Benz CLA', 'Mercedes-Benz CLS', 'Mercedes-Benz E-Class', 'Mercedes-Benz G-Class', 'Mercedes-Benz GL-Class', 'Mercedes-Benz GLA 45 AMG', 'Mercedes-Benz GLA Class', 'Mercedes-Benz GLC', 'Mercedes-Benz GLE', 'Mercedes-Benz GLS', 'Mercedes-Benz M-Class', 'Mercedes-Benz C-Class', 'Mercedes-Benz S-Class', 'Mercedes-Benz SLC', 'Jaguar F-Type', 'Jaguar XE', 'Jaguar XF', 'Jaguar XJ', 'Volkswagen Ameo', 'Volkswagen Beetle', 'Volkswagen CrossPolo', 'Volkswagen Jetta', 'Volkswagen Polo', 'Volkswagen Vento', 'Toyota Camry', 'Toyota Corolla Altis', 'Toyota Platinum Etios', 'Toyota Etios Cross', 'Toyota Etios Liva', 'Toyota Fortuner', 'Toyota Innova', 'Toyota Innova Crysta', 'Toyota Land Cruiser', 'Toyota Land Cruiser Prado', 'Toyota Prius', 'Rolls-Royce Dawn', 'Rolls-Royce Ghost', 'Rolls-Royce Phantom', 'Rolls-Royce Wraith', 'Mahindra Ssangyong Rexton', 'Mini 3 DOOR', 'Mini 5 DOOR', 'Mini Cooper Convertible', 'Mini Countryman', 'Force Gurkha', 'Force One SUV', 'Bentley Bentayga', 'Bentley Continental', 'Bentley Flying Spur', 'Bentley Mulsanne', 'Isuzu D-Max V-Cross', 'Isuzu MU 7', 'Aston Martin DB11', 'Aston Martin Rapide', 'Aston Martin Vanquish', 'Aston Martin Vantage', 'Skoda Octavia', 'Skoda Rapid', 'Skoda Superb', 'Skoda Yeti', 'Conquest Evade', 'Premier Rio', 'Hyundai Creta', 'Hyundai Elantra', 'Hyundai EON', 'Hyundai Grand i10', 'Hyundai i10', 'Hyundai Elite i20', 'Hyundai i20 Active', 'Hyundai Santa Fe', 'Hyundai Verna', 'Hyundai Xcent', 'Ford EcoSport', 'Ford Endeavour', 'Ford Figo', 'Ford Aspire', 'Ford Mustang', 'Land Rover Discovery 4', 'Land Rover Discovery Sport', 'Land Rover Range Rover', 'Land Rover Range Rover Evoque', 'Land Rover Range Rover Sport', 'Datsun GO', 'Datsun GO Plus', 'Datsun Redi GO', 'BMW 1 Series', 'BMW 3 Series', 'BMW 5 Series', 'BMW 6 Series', 'BMW 7 Series', 'BMW i8', 'BMW M Series', 'BMW X1', 'BMW X3', 'BMW X5', 'BMW X6', 'BMW Z4', 'Mitsubishi Pajero Sport', 'Bugatti Veyron', 'Audi A3', 'Audi A3 cabriolet', 'Audi A4', 'Audi A6', 'Audi A8', 'Audi Q3', 'Audi Q5', 'Audi Q7', 'Audi R8', 'Audi RS6 Avant', 'Audi RS7', 'Audi S5', 'Audi TT']

review = {}
failed = []
driver = webdriver.Chrome()

for index, car in enumerate(cars):
    try:

        link_car = car.split(" ")
        model = link_car[0]
        link_car = '_'.join(link_car)
        print "%d/%d" %(index+1, len(cars))
        print "Model : ", model, "\nCar : ", link_car
        link = "https://www.cardekho.com/carmodels/"+model+"/"+link_car
        print link
        driver.get(link)
        driver.switch_to.default_content()
        print "Review for", car
        review_mat = ''
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='tabDetails jqlazy']//p")))

        for k in driver.find_elements_by_xpath("//div[@class='tabDetails jqlazy']//p"):
            review_mat += k.text

        review[car] = review_mat.encode('UTF8')
        print review_mat
    except Exception as e:
        print car ,"failed due to", e
        failed.append(car)

pickle.dump(review, open("review.p", "wb"))
pickle.dump(failed, open("failed.p", "wb"))

driver.close()