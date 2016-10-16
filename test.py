import pickle

#Testing link in the pickle file

with open("links.p", 'rb') as fp:
    sList = pickle.load(fp)

main = sList[0]
catg = sList[1]

print "Main cars : ", main
print "Variants : ", catg