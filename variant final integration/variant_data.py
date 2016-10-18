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

err=[]

dict_convertibles={}
for i in convertibles.keys():
	try:
		convertibles['Main Car Name'] = convertibles[i]['Review_link'].split('/')[4].replace('_',' ')
		dict_convertibles['Variant Car Name'] = convertibles[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_convertibles['Mileage'] = float(convertibles[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_convertibles['Specs and Features'] = [convertibles[i]['Specs'],convertibles[i]['Features']]
		dict_convertibles['Review'] = convertibles[i]['Review']
		#dict_convertibles['Price']	= price[convertibles[i]['Review_link']]
	except:
		err.append(["convertibles",convertibles[i]['Review_link']])
print len(err)

dict_coupe={}
for i in coupe.keys():
	try:
		coupe['Main Car Name'] = coupe[i]['Review_link'].split('/')[4].replace('_',' ')
		dict_coupe['Variant Car Name'] = coupe[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_coupe['Mileage'] = float(coupe[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_coupe['Specs and Features'] = [coupe[i]['Specs'],coupe[i]['Features']]
		dict_coupe['Review'] = coupe[i]['Review']
		#dict_coupe['Price']	= price[coupe[i]['Review_link']]
	except:
		err.append(["coupe",coupe[i]['Review_link']])
print len(err)

dict_hatchback={}
for i in hatchback.keys():
	try:
		hatchback['Main Car Name'] = hatchback[i]['Review_link'].split('/')[4].replace('_',' ')
		dict_hatchback['Variant Car Name'] = hatchback[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_hatchback['Mileage'] = float(hatchback[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_hatchback['Specs and Features'] = [hatchback[i]['Specs'],hatchback[i]['Features']]
		dict_hatchback['Review'] = hatchback[i]['Review']
		#dict_hatchback['Price']	= price[hatchback[i]['Review_link']]
	except:
		err.append(["hatchback",hatchback[i]['Review_link']])
print len(err)

dict_hybrid={}
for i in hybrid.keys():
	try:
		hybrid['Main Car Name'] = hybrid[i]['Review_link'].split('/')[4].replace('_',' ')
		dict_hybrid['Variant Car Name'] = hybrid[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_hybrid['Mileage'] = float(hybrid[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_hybrid['Specs and Features'] = [hybrid[i]['Specs'],hybrid[i]['Features']]
		dict_hybrid['Review'] = hybrid[i]['Review']
		#dict_hybrid['Price']	= price[hybrid[i]['Review_link']]
	except:
		err.append(["hybrid",hybrid[i]['Review_link']])
print len(err)

dict_luxury={}
for i in luxury.keys():
	try:
		luxury['Main Car Name'] = luxury[i]['Review_link'].split('/')[4].replace('_',' ')
		dict_luxury['Variant Car Name'] = luxury[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_luxury['Mileage'] = float(luxury[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_luxury['Specs and Features'] = [luxury[i]['Specs'],luxury[i]['Features']]
		dict_luxury['Review'] = luxury[i]['Review']
		#dict_luxury['Price']	= price[luxury[i]['Review_link']]
	except:
		err.append(["luxury",luxury[i]['Review_link']])
print len(err)

dict_minivans={}
for i in minivans.keys():
	try:
		minivans['Main Car Name'] = minivans[i]['Review_link'].split('/')[4].replace('_',' ')
		dict_minivans['Variant Car Name'] = minivans[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_minivans['Mileage'] = float(minivans[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_minivans['Specs and Features'] = [minivans[i]['Specs'],minivans[i]['Features']]
		dict_minivans['Review'] = minivans[i]['Review']
		#dict_minivans['Price']	= price[minivans[i]['Review_link']]
	except:
		err.append(["minivans",minivans[i]['Review_link']])
print len(err)

dict_muv={}
for i in muv.keys():
	try:
		muv['Main Car Name'] = muv[i]['Review_link'].split('/')[4].replace('_',' ')
		dict_muv['Variant Car Name'] = muv[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_muv['Mileage'] = float(muv[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_muv['Specs and Features'] = [muv[i]['Specs'],muv[i]['Features']]
		dict_muv['Review'] = muv[i]['Review']
		#dict_muv['Price']	= price[muv[i]['Review_link']]
	except:
		err.append(["muv",muv[i]['Review_link']])
print len(err)

'''dict_pickup={}
for i in pickup.keys():
	try:
		pickup['Main Car Name'] = pickup[i]['Review_link'].split('/')[4].replace('_',' ')
		dict_pickup['Variant Car Name'] = pickup[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_pickup['Mileage'] = float(pickup[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_pickup['Specs and Features'] = [pickup[i]['Specs'],pickup[i]['Features']]
		dict_pickup['Review'] = pickup[i]['Review']
		dict_pickup['Price']	= price[pickup[i]['Review_link']]
	except:
		err.append(["pickup",pickup[i]['Review_link']])
print len(err)'''

dict_sedans={}
for i in sedans.keys():
	try:
		sedans['Main Car Name'] = sedans[i]['Review_link'].split('/')[4].replace('_',' ')
		dict_sedans['Variant Car Name'] = sedans[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_sedans['Mileage'] = float(sedans[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_sedans['Specs and Features'] = [sedans[i]['Specs'],sedans[i]['Features']]
		dict_sedans['Review'] = sedans[i]['Review']
		#dict_sedans['Price']	= price[sedans[i]['Review_link']]
	except:
		err.append(["sedans",sedans[i]['Review_link']])
print len(err)

dict_suv={}
for i in suv.keys():
	try:
		suv['Main Car Name'] = suv[i]['Review_link'].split('/')[4].replace('_',' ')
		dict_suv['Variant Car Name'] = suv[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_suv['Mileage'] = float(suv[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_suv['Specs and Features'] = [suv[i]['Specs'],suv[i]['Features']]
		dict_suv['Review'] = suv[i]['Review']
		#dict_suv['Price']	= price[suv[i]['Review_link']]
	except:
		err.append(["suv",suv[i]['Review_link']])
print len(err)

final_output=[dict_convertibles,dict_coupe,dict_hatchback,dict_hybrid,dict_luxury,dict_minivans,dict_muv,dict_sedans,dict_suv]