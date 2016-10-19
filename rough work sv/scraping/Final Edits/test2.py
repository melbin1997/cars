import pickle

a=pickle.load(open("output.p","rb"))
for key in a:
	print key
	print a[key]
	print