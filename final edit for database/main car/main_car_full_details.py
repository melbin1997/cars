import pickle
data=pickle.load(open("output.p","rb"))
image=pickle.load(open("images_found.p","rb"))
car_type=pickle.load(open("main_car_type.p","rb"))
review=pickle.load(open("g_review.p","rb"))


pickle.dump({'Mahindra e2o':123},open("main_car_full_data.p","wb"))
main_main=pickle.load(open("main_car_full_data.p","rb"))
err=[]
for i in data.keys():
	for j in data[i]:
		try:
			main={}
			main['Car Name']=j
			main['Car Price']=int(data[i][j]['Key Specs'][0]['Ex-showroom Price New Delhi'][2:-15].replace(",",""))
			for k in image.keys():
				if (k==j):
					main['Car Images']=image[j]
					break
			if(j=='Mahindra e2o'):
				main['Car Mileage']='120 km on full charge'	
			else:
				main['Car Mileage']=sum(map(float,data[i][j]['Key Specs'][0]['City / Highway Mileage'].replace(" kmpl","").split(" / ")))/float(len(data[i][j]['Key Specs'][0]['City / Highway Mileage'].replace(" kmpl","").split(" / ")))
			main['Car Features']=data[i][j]
			main['Car Type']=car_type[j]
			if j in ['Audi RS7', 'Ford Figo', 'Porsche Cayenne', 'Rolls-Royce Ghost', 'Maserati Ghibli', 'Nissan Terrano', 'Mercedes-Benz AMG GT', 'BMW 6 Series', 'Bugatti Veyron', 'Ford Mustang', 'Jaguar XJ', 'Mahindra Verito']:
				main['Car Review']="Sorry no data available now."
			else:
				main['Car Review']=review[j]
		



			main_main[j]=main
			pickle.dump(main_main,open("main_car_full_data.p","wb"))
		except:
			err.append(j)
print ""
print ""
print err