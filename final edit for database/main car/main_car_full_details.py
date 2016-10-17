import pickle
data=pickle.load(open("output.p","rb"))
image=pickle.load(open("images_found.p","rb"))
err=[]
for i in data.keys():
	for j in data[i]:
		try:
			print ""
			print "Car Name: ",j
			print ""
			print "Car Price: ",int(data[i][j]['Key Specs'][0]['Ex-showroom Price New Delhi'][2:-15].replace(",",""))
			for k in image.keys():
				if (k==j):
					print ""
					print "Car images: "
					print image[j]
			print ""
			print "Car Mileage: ",sum(map(float,data[i][j]['Key Specs'][0]['City / Highway Mileage'].replace(" kmpl","").split(" / ")))/float(len(data[i][j]['Key Specs'][0]['City / Highway Mileage'].replace(" kmpl","").split(" / ")))
			print ""
			print data[i][j]
		except:
			err.append(j)
print ""
print ""
print err