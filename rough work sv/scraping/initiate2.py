import pickle
a={1:2}
pickle.dump(a,open("output2.p","wb"))
b=pickle.load(open("output2.p","rb"))
print b