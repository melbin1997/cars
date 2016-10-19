import pickle
a=pickle.load(open("output.p","rb"))
for i in a.keys():
	for j in a[i]:
		print j
		print a[i][j]
		break
	break