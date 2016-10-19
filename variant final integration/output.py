import sys
import pickle

convertibles=pickle.load(open("variant_convertibles_output.p","rb"))
coupe=pickle.load(open("variant_coupe_output.p","rb"))
hatchback=pickle.load(open("variant_hatchback_output.p","rb"))
hybrid=pickle.load(open("variant_hybrid_output.p","rb"))
luxury=pickle.load(open("variant_luxury_output.p","rb"))
minivans=pickle.load(open("variant_minivans_output.p","rb"))
muv=pickle.load(open("variant_muv_output.p","rb"))
#pickup=pickle.load(open("variant_pickup_output.p","rb"))
sedans=pickle.load(open("variant_sedan_output.p","rb"))
suv=pickle.load(open("variant_suv_output.p","rb"))

price=pickle.load(open("price.p","rb"))

namefix=pickle.load((open("matched.p","rb")))

final_output={}

num=0
mdict_convertibles={}
for i in convertibles.keys():
	if convertibles[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','') not in ['Mahindra E Verito D2', 'Mahindra E Verito D6', 'Mahindra E Verito D4', 'Mercedes-Benz SLC 43 AMG', 'Rolls-Royce Dawn Convertible', 'Tata New Safari DICOR 2.2 EX 4x2 BS IV', 'Tata New Safari DICOR 2.2 LX 4x2 BS IV', 'Jeep Grand Cherokee Summit 4X4', 'Mercedes-Benz GLC Class 220d 4MATIC Style', 'Mercedes-Benz GLC Class 220d 4MATIC Sport', 'Jeep Wrangler 4X4', 'Jeep Grand Cherokee SRT 4X4', 'Mercedes-Benz GLC Class 300 4MATIC Sport', 'Jeep Grand Cherokee Limited 4X4']:
		dict_convertibles={}
		dict_convertibles['Main Car Name'] = namefix[convertibles[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')]
		dict_convertibles['Variant Car Name'] =convertibles[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_convertibles['Mileage'] = float(convertibles[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_convertibles['Specs and Features'] = [convertibles[i]['Specs'],convertibles[i]['Features']]
		dict_convertibles['Review'] = convertibles[i]['Review']
		dict_convertibles['Price']	= price[convertibles[i]['Review_link']]
		mdict_convertibles[num]=dict_convertibles
		num+=1
		final_output['Convertibles']=mdict_convertibles

pickle.dump(final_output,open("abcopt.p","wb"))

num=0
mdict_coupe={}
for i in coupe.keys():
	if coupe[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','') not in ['Mahindra E Verito D2', 'Mahindra E Verito D6', 'Mahindra E Verito D4', 'Mercedes-Benz SLC 43 AMG', 'Rolls-Royce Dawn Convertible', 'Tata New Safari DICOR 2.2 EX 4x2 BS IV', 'Tata New Safari DICOR 2.2 LX 4x2 BS IV', 'Jeep Grand Cherokee Summit 4X4', 'Mercedes-Benz GLC Class 220d 4MATIC Style', 'Mercedes-Benz GLC Class 220d 4MATIC Sport', 'Jeep Wrangler 4X4', 'Jeep Grand Cherokee SRT 4X4', 'Mercedes-Benz GLC Class 300 4MATIC Sport', 'Jeep Grand Cherokee Limited 4X4']:
		dict_coupe={}
		dict_coupe['Main Car Name'] = namefix[coupe[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')]
		dict_coupe['Variant Car Name'] =coupe[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		dict_coupe['Mileage'] = float(coupe[i]['Specs']['Mileage-Highway (kmpl)'])
		dict_coupe['Specs and Features'] = [coupe[i]['Specs'],coupe[i]['Features']]
		dict_coupe['Review'] = coupe[i]['Review']
		dict_coupe['Price']	= price[coupe[i]['Review_link']]
		mdict_coupe[num]=dict_coupe
		num+=1
		final_output['Coupe']=mdict_coupe
pickle.dump(final_output,open("abcopt.p","wb"))

num=0
mdict_hatchback={}
for i in hatchback.keys():
	if hatchback[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','') not in ['Mahindra E Verito D2', 'Mahindra E Verito D6', 'Mahindra E Verito D4', 'Mercedes-Benz SLC 43 AMG', 'Rolls-Royce Dawn Convertible', 'Tata New Safari DICOR 2.2 EX 4x2 BS IV', 'Tata New Safari DICOR 2.2 LX 4x2 BS IV', 'Jeep Grand Cherokee Summit 4X4', 'Mercedes-Benz GLC Class 220d 4MATIC Style', 'Mercedes-Benz GLC Class 220d 4MATIC Sport', 'Jeep Wrangler 4X4', 'Jeep Grand Cherokee SRT 4X4', 'Mercedes-Benz GLC Class 300 4MATIC Sport', 'Jeep Grand Cherokee Limited 4X4']:
		dict_hatchback={}
		mil='fail'
		dict_hatchback['Main Car Name'] = namefix[hatchback[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')]
		dict_hatchback['Variant Car Name'] =hatchback[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		if(mil=='fail'):
			try:
				dict_hatchback['Mileage'] = float(hatchback[i]['Specs']['Mileage-Highway (kmpl)'])
				mil='pass'
			except:
				pass

		if(mil=='fail'):
			try:
				dict_hatchback['Mileage'] = float(hatchback[i]['Specs']['Mileage-City (km/kg)'])
				mil='pass'
			except:
				pass
		if(mil=='fail'):
			try:
				dict_hatchback['Mileage'] = float(hatchback[i]['Specs']['Mileage-City km/full charge'])
				mil='pass'
			except:
				print hatchback[i]
				sys.exit()

		dict_hatchback['Specs and Features'] = [hatchback[i]['Specs'],hatchback[i]['Features']]
		dict_hatchback['Review'] = hatchback[i]['Review']
		dict_hatchback['Price']	= price[hatchback[i]['Review_link']]
		mdict_hatchback[num]=dict_hatchback
		num+=1
		final_output['Hatchback']=mdict_hatchback

pickle.dump(final_output,open("abcopt.p","wb"))


num=0
mdict_hybrid={}
for i in hybrid.keys():
	if hybrid[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','') not in ['Mahindra E Verito D2', 'Mahindra E Verito D6', 'Mahindra E Verito D4', 'Mercedes-Benz SLC 43 AMG', 'Rolls-Royce Dawn Convertible', 'Tata New Safari DICOR 2.2 EX 4x2 BS IV', 'Tata New Safari DICOR 2.2 LX 4x2 BS IV', 'Jeep Grand Cherokee Summit 4X4', 'Mercedes-Benz GLC Class 220d 4MATIC Style', 'Mercedes-Benz GLC Class 220d 4MATIC Sport', 'Jeep Wrangler 4X4', 'Jeep Grand Cherokee SRT 4X4', 'Mercedes-Benz GLC Class 300 4MATIC Sport', 'Jeep Grand Cherokee Limited 4X4']:
		dict_hybrid={}
		mil='fail'
		dict_hybrid['Main Car Name'] = namefix[hybrid[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')]
		dict_hybrid['Variant Car Name'] =hybrid[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		if(mil=='fail'):
			try:
				dict_hybrid['Mileage'] = float(hybrid[i]['Specs']['Mileage-Highway (kmpl)'])
				mil='pass'
			except:
				pass

		if(mil=='fail'):
			try:
				dict_hybrid['Mileage'] = float(hybrid[i]['Specs']['Mileage-City (km/kg)'])
				mil='pass'
			except:
				pass
		if(mil=='fail'):
			try:
				dict_hybrid['Mileage'] = float(hybrid[i]['Specs']['Mileage-City km/full charge'])
				mil='pass'
			except:
				print hybrid[i]
				sys.exit()

		dict_hybrid['Specs and Features'] = [hybrid[i]['Specs'],hybrid[i]['Features']]
		dict_hybrid['Review'] = hybrid[i]['Review']
		dict_hybrid['Price']	= price[hybrid[i]['Review_link']]
		mdict_hybrid[num]=dict_hybrid
		num+=1
		final_output['Hybrid']=mdict_hybrid

pickle.dump(final_output,open("abcopt.p","wb"))


num=0
mdict_luxury={}
for i in luxury.keys():
	if luxury[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','') not in ['Mahindra E Verito D2', 'Mahindra E Verito D6', 'Mahindra E Verito D4', 'Mercedes-Benz SLC 43 AMG', 'Rolls-Royce Dawn Convertible', 'Tata New Safari DICOR 2.2 EX 4x2 BS IV', 'Tata New Safari DICOR 2.2 LX 4x2 BS IV', 'Jeep Grand Cherokee Summit 4X4', 'Mercedes-Benz GLC Class 220d 4MATIC Style', 'Mercedes-Benz GLC Class 220d 4MATIC Sport', 'Jeep Wrangler 4X4', 'Jeep Grand Cherokee SRT 4X4', 'Mercedes-Benz GLC Class 300 4MATIC Sport', 'Jeep Grand Cherokee Limited 4X4']:
		dict_luxury={}
		mil='fail'
		dict_luxury['Main Car Name'] = namefix[luxury[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')]
		dict_luxury['Variant Car Name'] =luxury[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		if(mil=='fail'):
			try:
				dict_luxury['Mileage'] = float(luxury[i]['Specs']['Mileage-Highway (kmpl)'])
				mil='pass'
			except:
				pass

		if(mil=='fail'):
			try:
				dict_luxury['Mileage'] = float(luxury[i]['Specs']['Mileage-City (km/kg)'])
				mil='pass'
			except:
				pass
		if(mil=='fail'):
			try:
				dict_luxury['Mileage'] = float(luxury[i]['Specs']['Mileage-City km/full charge'])
				mil='pass'
			except:
				print luxury[i]
				sys.exit()

		dict_luxury['Specs and Features'] = [luxury[i]['Specs'],luxury[i]['Features']]
		dict_luxury['Review'] = luxury[i]['Review']
		dict_luxury['Price']	= price[luxury[i]['Review_link']]
		mdict_luxury[num]=dict_luxury
		num+=1
		final_output['Luxury']=mdict_luxury

pickle.dump(final_output,open("abcopt.p","wb"))


num=0
mdict_minivans={}
for i in minivans.keys():
	if minivans[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','') not in ['Mahindra E Verito D2', 'Mahindra E Verito D6', 'Mahindra E Verito D4', 'Mercedes-Benz SLC 43 AMG', 'Rolls-Royce Dawn Convertible', 'Tata New Safari DICOR 2.2 EX 4x2 BS IV', 'Tata New Safari DICOR 2.2 LX 4x2 BS IV', 'Jeep Grand Cherokee Summit 4X4', 'Mercedes-Benz GLC Class 220d 4MATIC Style', 'Mercedes-Benz GLC Class 220d 4MATIC Sport', 'Jeep Wrangler 4X4', 'Jeep Grand Cherokee SRT 4X4', 'Mercedes-Benz GLC Class 300 4MATIC Sport', 'Jeep Grand Cherokee Limited 4X4']:
		dict_minivans={}
		mil='fail'
		dict_minivans['Main Car Name'] = namefix[minivans[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')]
		dict_minivans['Variant Car Name'] =minivans[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		if(mil=='fail'):
			try:
				dict_minivans['Mileage'] = float(minivans[i]['Specs']['Mileage-Highway (kmpl)'])
				mil='pass'
			except:
				pass

		if(mil=='fail'):
			try:
				dict_minivans['Mileage'] = float(minivans[i]['Specs']['Mileage-City (km/kg)'])
				mil='pass'
			except:
				pass
		if(mil=='fail'):
			try:
				dict_minivans['Mileage'] = float(minivans[i]['Specs']['Mileage-City km/full charge'])
				mil='pass'
			except:
				print minivans[i]
				sys.exit()

		dict_minivans['Specs and Features'] = [minivans[i]['Specs'],minivans[i]['Features']]
		dict_minivans['Review'] = minivans[i]['Review']
		dict_minivans['Price']	= price[minivans[i]['Review_link']]
		mdict_minivans[num]=dict_minivans
		num+=1
		final_output['Minivans']=mdict_minivans

pickle.dump(final_output,open("abcopt.p","wb"))


num=0
mdict_muv={}
for i in muv.keys():
	if muv[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','') not in ['Mahindra E Verito D2', 'Mahindra E Verito D6', 'Mahindra E Verito D4', 'Mercedes-Benz SLC 43 AMG', 'Rolls-Royce Dawn Convertible', 'Tata New Safari DICOR 2.2 EX 4x2 BS IV', 'Tata New Safari DICOR 2.2 LX 4x2 BS IV', 'Jeep Grand Cherokee Summit 4X4', 'Mercedes-Benz GLC Class 220d 4MATIC Style', 'Mercedes-Benz GLC Class 220d 4MATIC Sport', 'Jeep Wrangler 4X4', 'Jeep Grand Cherokee SRT 4X4', 'Mercedes-Benz GLC Class 300 4MATIC Sport', 'Jeep Grand Cherokee Limited 4X4']:
		dict_muv={}
		mil='fail'
		dict_muv['Main Car Name'] = namefix[muv[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')]
		dict_muv['Variant Car Name'] =muv[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		if(mil=='fail'):
			try:
				dict_muv['Mileage'] = float(muv[i]['Specs']['Mileage-Highway (kmpl)'])
				mil='pass'
			except:
				pass

		if(mil=='fail'):
			try:
				dict_muv['Mileage'] = float(muv[i]['Specs']['Mileage-City (km/kg)'])
				mil='pass'
			except:
				pass
		if(mil=='fail'):
			try:
				dict_muv['Mileage'] = float(muv[i]['Specs']['Mileage-City km/full charge'])
				mil='pass'
			except:
				print muv[i]
				sys.exit()

		dict_muv['Specs and Features'] = [muv[i]['Specs'],muv[i]['Features']]
		dict_muv['Review'] = muv[i]['Review']
		dict_muv['Price']	= price[muv[i]['Review_link']]
		mdict_muv[num]=dict_muv
		num+=1
		final_output['MUV']=mdict_muv

pickle.dump(final_output,open("abcopt.p","wb"))

num=0
mdict_sedans={}
for i in sedans.keys():
	if sedans[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','') not in ['Mahindra E Verito D2', 'Mahindra E Verito D6', 'Mahindra E Verito D4', 'Mercedes-Benz SLC 43 AMG', 'Rolls-Royce Dawn Convertible', 'Tata New Safari DICOR 2.2 EX 4x2 BS IV', 'Tata New Safari DICOR 2.2 LX 4x2 BS IV', 'Jeep Grand Cherokee Summit 4X4', 'Mercedes-Benz GLC Class 220d 4MATIC Style', 'Mercedes-Benz GLC Class 220d 4MATIC Sport', 'Jeep Wrangler 4X4', 'Jeep Grand Cherokee SRT 4X4', 'Mercedes-Benz GLC Class 300 4MATIC Sport', 'Jeep Grand Cherokee Limited 4X4']:
		dict_sedans={}
		mil='fail'
		dict_sedans['Main Car Name'] = namefix[sedans[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')]
		dict_sedans['Variant Car Name'] =sedans[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		if(mil=='fail'):
			try:
				dict_sedans['Mileage'] = float(sedans[i]['Specs']['Mileage-Highway (kmpl)'])
				mil='pass'
			except:
				pass

		if(mil=='fail'):
			try:
				dict_sedans['Mileage'] = float(sedans[i]['Specs']['Mileage-City (km/kg)'])
				mil='pass'
			except:
				pass
		if(mil=='fail'):
			try:
				dict_sedans['Mileage'] = float(sedans[i]['Specs']['Mileage-City km/full charge'])
				mil='pass'
			except:
				pass
		if(mil=='fail' and sedans[i]['Review_link']=='https://www.cardekho.com/overview/Mahindra_E_Verito/Mahindra_E_Verito_D2.htm'):
			try:
				dict_sedans['Mileage'] = 19.52
				mil='pass'
			except:
				pass
				print sedans[i]
				sys.exit()

		dict_sedans['Specs and Features'] = [sedans[i]['Specs'],sedans[i]['Features']]
		dict_sedans['Review'] = sedans[i]['Review']
		dict_sedans['Price']	= price[sedans[i]['Review_link']]
		mdict_sedans[num]=dict_sedans
		num+=1
		final_output['Sedans']=mdict_sedans

pickle.dump(final_output,open("abcopt.p","wb"))


num=0
mdict_suv={}
for i in suv.keys():
	if suv[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','') not in ['Mahindra E Verito D2', 'Mahindra E Verito D6', 'Mahindra E Verito D4', 'Mercedes-Benz SLC 43 AMG', 'Rolls-Royce Dawn Convertible', 'Tata New Safari DICOR 2.2 EX 4x2 BS IV', 'Tata New Safari DICOR 2.2 LX 4x2 BS IV', 'Jeep Grand Cherokee Summit 4X4', 'Mercedes-Benz GLC Class 220d 4MATIC Style', 'Mercedes-Benz GLC Class 220d 4MATIC Sport', 'Jeep Wrangler 4X4', 'Jeep Grand Cherokee SRT 4X4', 'Mercedes-Benz GLC Class 300 4MATIC Sport', 'Jeep Grand Cherokee Limited 4X4']:
		dict_suv={}
		mil='fail'
		dict_suv['Main Car Name'] = namefix[suv[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')]
		dict_suv['Variant Car Name'] =suv[i]['Review_link'].split('/')[5].replace('_',' ').replace('.htm','')
		if(mil=='fail'):
			try:
				dict_suv['Mileage'] = float(suv[i]['Specs']['Mileage-Highway (kmpl)'])
				mil='pass'
			except:
				pass

		if(mil=='fail'):
			try:
				dict_suv['Mileage'] = float(suv[i]['Specs']['Mileage-City (km/kg)'])
				mil='pass'
			except:
				pass
		if(mil=='fail'):
			try:
				dict_suv['Mileage'] = float(suv[i]['Specs']['Mileage-City km/full charge'])
				mil='pass'
			except:
				pass
		if(mil=='fail' and suv[i]['Review_link']=='https://www.cardekho.com/overview/Mahindra_E_Verito/Mahindra_E_Verito_D2.htm'):
			try:
				dict_suv['Mileage'] = 19.52
				mil='pass'
			except:
				pass
				print suv[i]
				sys.exit()

		dict_suv['Specs and Features'] = [suv[i]['Specs'],suv[i]['Features']]
		dict_suv['Review'] = suv[i]['Review']
		dict_suv['Price']	= price[suv[i]['Review_link']]
		mdict_suv[num]=dict_suv
		num+=1
		final_output['SUV']=mdict_suv

pickle.dump(final_output,open("abcopt.p","wb"))