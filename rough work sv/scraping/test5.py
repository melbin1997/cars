import pickle
a={1:2,3:4,5:6,7:8}
pickle.dump(a,open("save.p","wb"))
b=pickle.load(open("save.p","rb"))
print b