import pickle

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
price=pickle.load(open("price.p","rb"))


final_output={}
err=[]

dict_convertibles={}
for i in convertibles.keys():
	try:
		convertibles['Main Car Name'] = convertibles[i]['Review_link'].split('/')[4].replace('_',' ')
		dict_convertibles['Variant Car Name'] = convertibles[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_convertibles['Mileage'] = float(convertibles[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_convertibles['Specs and Features'] = [convertibles[i]['Specs'],convertibles[i]['Features']]
		dict_convertibles['Review'] = convertibles[i]['Review']
		dict_convertibles['Price']	= price[convertibles[i]['Features_link']]
		break
	except:
		err.append(["convertibles",convertibles[i]['Review_link']])
for i in dict_convertibles.keys():
	print ""
	print ""
	print dict_convertibles[i]

print len(err)