import pickle

main=pickle.load(open("output.p","rb"))
convertibles=pickle.load(open("variant_convertibles_output.p","rb"))
coupe=pickle.load(open("variant_coupe_output.p","rb"))
hatchback=pickle.load(open("variant_hatchback_output.p","rb"))
hybrid=pickle.load(open("variant_hybrid_output.p","rb"))
luxury=pickle.load(open("variant_luxury_output.p","rb"))
minivans=pickle.load(open("variant_minivans_output.p","rb"))
muv=pickle.load(open("variant_muv_output.p","rb"))
pickup=pickle.load(open("variant_pickup_output.p","rb"))
sedans=pickle.load(open("variant_sedan_output.p","rb"))
suv=pickle.load(open("variant_suv_output.p","rb"))
err=[]
pickle.dump({1:2},open("main_car_type.p","wb"))
car_type=pickle.load(open("main_car_type.p","rb"))
for i in main.keys():
	for j in main[i]:
		flag=-1
		print j,"#########",
		if flag==-1:
			for k in sedans.keys():
				if sedans[k]['Features_link'].split('/')[4].replace('_',' ')==j:
					print "sedans"
					car_type[j]='sedan'
					flag=1
					break
		if flag==-1:
			for k in convertibles.keys():
				if convertibles[k]['Features_link'].split('/')[4].replace('_',' ')==j:
					print "convertibles"
					car_type[j]='convertibles'
					flag=1
					break
		if flag==-1:
			for k in coupe.keys():
				if coupe[k]['Features_link'].split('/')[4].replace('_',' ')==j:
					print "coupe"
					car_type[j]='coupe'
					flag=1
					break
		if flag==-1:
			for k in hatchback.keys():
				if hatchback[k]['Features_link'].split('/')[4].replace('_',' ')==j:
					print "hatchback"
					car_type[j]='hatchback'
					flag=1
					break
		if flag==-1:	
			for k in hybrid.keys():
				if hybrid[k]['Features_link'].split('/')[4].replace('_',' ')==j:
					print "hybrid"
					car_type[j]='hybrid'
					flag=1
					break
		if flag==-1:
			for k in luxury.keys():
				if luxury[k]['Features_link'].split('/')[4].replace('_',' ')==j:
					print "luxury"
					car_type[j]='luxury'
					flag=1
					break
		if flag==-1:	
			for k in minivans.keys():
				if minivans[k]['Features_link'].split('/')[4].replace('_',' ')==j:
					print "minivans"
					car_type[j]='minivans'
					flag=1
					break
		if flag==-1:	
			for k in muv.keys():
				if muv[k]['Features_link'].split('/')[4].replace('_',' ')==j:
					print "muv"
					car_type[j]='muv'
					flag=1
					break
		if flag==-1:	
			for k in suv.keys():
				if suv[k]['Features_link'].split('/')[4].replace('_',' ')==j:
					print "suv"
					car_type[j]='suv'
					flag=1
					break
		if j=='Mahindra KUV100' or j=='Ford EcoSport' or j=='Force One SUV' or j=='Tata Safari' or j=='Force One SUV':
			car_type[j]='suv'
			flag=1
		print " "
		if flag==-1:
			car_type[j]='sedan'
		pickle.dump(car_type,open("main_car_type.p","wb"))