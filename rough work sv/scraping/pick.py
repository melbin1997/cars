import pickle

f = open("save.p", "a++")
pickle.dump("123", open("save.p", "wb"))
pickle.dump("456", f)
pickle.dump("#####", f)
f.close()
