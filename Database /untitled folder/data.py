import pickle
a=pickle.load(open("variant_cars_data.p","rb"))
print a.keys()		#selecting car variant

print a['Sedans'].keys()	#selecting car using the number

print a['Sedans'][4].keys()	#each detail of a car

print a['Sedans'][4]['Mileage']	#prints the mileage of the car

for i in a.keys():
	for j in a[i].keys():
		print a[i][j].keys()
		break
	break
