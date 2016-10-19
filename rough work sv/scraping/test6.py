import pickle
b=pickle.load(open("save.p","rb"))
b[9]=10
pickle.dump(b,open("save.p","wb"))