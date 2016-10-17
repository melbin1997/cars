import pickle
a=pickle.load(open("variant_one_car.p","r"))
for i in  a['Review']:
	print i
temp = 0
for i in a['Specs']:
	data = []
	values = []
	t = i + ":" +  a['Specs'][i] + ","
	print t,
	temp = temp+1
print temp 