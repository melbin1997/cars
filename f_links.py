import pickle

man_links = {'Fiat Avventura Urban Cross':'https://www.cardekho.com/fiat/avventura-urban-cross',
'Jeep Grand Cherokee':'https://www.cardekho.com/jeep/grand-cherokee',
'Jeep Wrangler Unlimited':'https://www.cardekho.com/jeep/wrangler',
'Mahindra E Verito':'https://www.cardekho.com/mahindra/e-verito',
'Mercedes-Benz CLA':'https://www.cardekho.com/carmodels/Mercedes-Benz/Mercedes-Benz_CLA',
'Mercedes-Benz CLS':'https://www.cardekho.com/carmodels/Mercedes-Benz/Mercedes-Benz_CLS-Class',
'Mercedes-Benz GLA 45 AMG':'https://www.cardekho.com/overview/Mercedes-Benz_GLA/Mercedes-Benz_GLA_45_AMG.htm',
'Mercedes-Benz GLC':'https://www.cardekho.com/mercedes-benz/glc-class',
'Mercedes-Benz GLE':'https://www.cardekho.com/carmodels/Mercedes-Benz/Mercedes-Benz_GLE_Class',
'Mercedes-Benz GLS':'https://www.cardekho.com/mercedes-benz/gls',
'Mercedes-Benz SLC':'https://www.cardekho.com/mercedes-benz/slc',
'Rolls-Royce Dawn':'https://www.cardekho.com/rolls-royce/dawn',
'Isuzu D-Max V-Cross':'https://www.cardekho.com/overview/Isuzu_D-Max_V-Cross/Isuzu_D-Max_V-Cross_4X4.htm',
'Aston Martin DB11':'https://www.cardekho.com/aston-martin/db11',
'Hyundai Creta':'https://www.cardekho.com/hyundai-cars/creta',
}

combined_links = {}

with open("link.p", 'rb') as fp:
    s1 = pickle.load(fp)

for i in s1:
    combined_links[i] = s1[i]

for i in man_links:
    combined_links[i] = man_links[i]

pickle.dump(combined_links, open("combined_links.p","wb"))