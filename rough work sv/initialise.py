import pickle
pickle.dump({1: 2},open("variant_output.p","wb"))
output=pickle.load(open("variant_output.p","rb"))
print output