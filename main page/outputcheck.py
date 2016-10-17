import pickle
a=pickle.load(open("main_one_car.p","r"))
for i in a.keys():
	for r in a[i].keys():
		print r
		for temp in a[i][r]:
			print temp 
	