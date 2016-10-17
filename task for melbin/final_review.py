import pickle


with open("review.p", 'rb') as fp:
    review = pickle.load(fp)

with open("review1.p", 'rb') as fp:
    review1 = pickle.load(fp)

with open("review2.p", 'rb') as fp:
    review2 = pickle.load(fp)

with open("review3.p", 'rb') as fp:
    review3 = pickle.load(fp)

with open("review4.p", 'rb') as fp:
    review4 = pickle.load(fp)

with open("review5.p", 'rb') as fp:
    review5 = pickle.load(fp)

with open("review6.p", 'rb') as fp:
    review6 = pickle.load(fp)

with open("review7.p", 'rb') as fp:
    review7 = pickle.load(fp)

final_review = {}

for i in review:
    final_review[i]= review[i]
for i in review1:
    final_review[i]= review1[i]
for i in review2:
    final_review[i]= review2[i]
for i in review3:
    final_review[i]= review3[i]
for i in review4:
    final_review[i]= review4[i]
for i in review5:
    final_review[i]= review5[i]
for i in review6:
    final_review[i]= review6[i]
for i in review7:
    final_review[i]= review7[i]

print len(final_review)
pickle.dump(final_review, open("final_review.p", "wb"))

