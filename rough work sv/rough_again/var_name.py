import pickle
var_name=[]
variant=pickle.load(open("variant_cars_data.p","rb"))
for i in variant.keys():
	for j in variant[i].keys():
		var_name.append(variant[i][j]['Variant Car Name'])

print var_name
#print len(set(var_name))
