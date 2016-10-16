import pickle
import price

ip='Maruti Swift'

main=pickle.load(open("output.p","rb"))
for i in main.keys():
	for j in main[i]:
		if j==ip:
			print "Full details of main car"
			print main[i]
			print ""
			print "Name of main car: "
			print j
			print ""
			print "Price of main car: "
			print main[i][j]['Key Specs'][0]['Ex-showroom Price New Delhi']

photos=pickle.load(open("images_found.p","rb"))
print "Photo links: "
for i in photos:
	if i==ip:
		print ""
		print photos[i]


variant=pickle.load(open("variant_hatchback_output.p","rb"))

print "Variant details: "
for i in variant:
	if variant[i]['Features_link'].split('/')[4].replace('_',' ')==ip:
		print ""
		print variant[i]['Review']
		print ""
		print variant[i]['Specs']
		print ""
		print variant[i]['Features']
		break

print" "
print "Price of variant: ",price.p()