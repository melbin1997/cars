import pickle

f = open("save.p", "a++")
print pickle.load(f)
print pickle.load(f)
print pickle.load(f)
f.close()
