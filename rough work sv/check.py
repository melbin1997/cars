import pickle
a=pickle.load(open("variant_output.p","rb"))
count=1
for i in a.keys():
	print "Details of car ",count
	count+=1
	for j in a[i].keys():
		print ""
		print j
		print a[i][j]
	print "#########################################################################################################################################################################"