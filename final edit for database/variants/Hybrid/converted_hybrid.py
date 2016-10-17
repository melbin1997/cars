import pickle

with open("price_hybrid.p", 'rb') as fp:
    prices = pickle.load(fp)

converted_convert = {}
for index, price in zip(prices.keys(),prices.values()):
    s = price.split(" ")
    if(s[1] == 'Lakh'):
        res = float(s[0]) * 100000
    elif(s[1] == 'Cr'):
        res = float(s[0]) * 10000000
    converted_convert[index] = int(res)

pickle.dump(converted_convert, open("converted_hybrid.p", "wb"))

