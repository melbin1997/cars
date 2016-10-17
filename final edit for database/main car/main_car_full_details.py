import pickle
data=pickle.load(open("output.p","rb"))
image=pickle.load(open("images_found.p","rb"))

main={}
err=[]
for i in data.keys():
	for j in data[i]:
		try:
			#print ""
			#print "Car Name: ",j
			main['Car Name']=j
			#print ""
			#print "Car Price: ",int(data[i][j]['Key Specs'][0]['Ex-showroom Price New Delhi'][2:-15].replace(",",""))
			main['Car Price']=int(data[i][j]['Key Specs'][0]['Ex-showroom Price New Delhi'][2:-15].replace(",",""))
			for k in image.keys():
				if (k==j):
					#print ""
					#print "Car images: "
					#print image[j]
					main['Car Images']=image[j]
					break
			#print ""
			#print "Car Mileage: ",sum(map(float,data[i][j]['Key Specs'][0]['City / Highway Mileage'].replace(" kmpl","").split(" / ")))/float(len(data[i][j]['Key Specs'][0]['City / Highway Mileage'].replace(" kmpl","").split(" / ")))
			if(j=='Mahindra e2o'):
				main['Car Mileage']='120 km on full charge'	
			else:
				main['Car Mileage']=sum(map(float,data[i][j]['Key Specs'][0]['City / Highway Mileage'].replace(" kmpl","").split(" / ")))/float(len(data[i][j]['Key Specs'][0]['City / Highway Mileage'].replace(" kmpl","").split(" / ")))
			#print ""
			#print data[i][j]
			main['Car Features']=data[i][j]
		except:
			err.append(j)
print ""
print ""
print err
#print main