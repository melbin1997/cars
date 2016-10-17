import pickle

'''with open("failed.p", 'rb') as fp:
    failed = pickle.load(fp)

for i in failed:
    print i
print len(failed)

'''
with open("review.p", 'rb') as fp:
    review = pickle.load(fp)

print len(review)
print review
#print lis
for i in review:
    print i,'-->', review[i]