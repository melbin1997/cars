import pickle

#Testing link in the pickle file

with open("links.p", 'rb') as fp:
    sList = pickle.load(fp)

cars_dict = sList[0]
catg = sList[1]

print cars_dict
print catg