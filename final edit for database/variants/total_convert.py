import pickle


with open("converted_convert.p", 'rb') as fp:
    converted_convert = pickle.load(fp)

with open("converted_coupe.p", 'rb') as fp:
    converted_coupe = pickle.load(fp)

with open("converted_hybrid.p", 'rb') as fp:
    converted_hybrid = pickle.load(fp)

with open("converted_luxury.p", 'rb') as fp:
    converted_luxury = pickle.load(fp)

with open("converted_minivans.p", 'rb') as fp:
    converted_minivans = pickle.load(fp)

with open("converted_MUV.p", 'rb') as fp:
    converted_MUV = pickle.load(fp)

with open("converted_pickup.p", 'rb') as fp:
    converted_pickup = pickle.load(fp)

with open("converted_sedans.p", 'rb') as fp:
    converted_sedans = pickle.load(fp)

with open("converted_SUV.p", 'rb') as fp:
    converted_SUV = pickle.load(fp)

with open("converted_hatch.p", 'rb') as fp:
    converted_hatch = pickle.load(fp)

final_converted = {}

for i in converted_convert:
    final_converted[i]= converted_convert[i]
for i in converted_coupe:
    final_converted[i]= converted_coupe[i]
for i in converted_hybrid:
    final_converted[i]= converted_hybrid[i]
for i in converted_luxury:
    final_converted[i]= converted_luxury[i]
for i in converted_minivans:
    final_converted[i]= converted_minivans[i]
for i in converted_MUV:
    final_converted[i]= converted_MUV[i]
for i in converted_pickup:
    final_converted[i]= converted_pickup[i]
for i in converted_sedans:
    final_converted[i]= converted_sedans[i]
for i in converted_SUV:
    final_converted[i]= converted_SUV[i]
for i in converted_hatch:
    final_converted[i]= converted_hatch[i]


print len(final_converted)
pickle.dump(final_converted, open("final_converted.p", "wb"))

