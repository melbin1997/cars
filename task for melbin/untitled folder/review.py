import pickle
r0=pickle.load(open("review.p","rb"))
r1=pickle.load(open("review1.p","rb"))
r2=pickle.load(open("review2.p","rb"))
r3=pickle.load(open("review3.p","rb"))
r4=pickle.load(open("review4.p","rb"))
r5=pickle.load(open("review5.p","rb"))
r6=pickle.load(open("review6.p","rb"))
r7=pickle.load(open("review7.p","rb"))
r8=pickle.load(open("final_review.p","rb"))
data=pickle.load(open("output.p","rb"))
pickle.dump({1: 2},open("g_review.p","wb"))
rev=pickle.load(open("g_review.p","rb"))
for i in data.keys():
	for j in data[i]:
		flag=-1
		if j in r0.keys():
			rev[j]=r0[j]
			flag=1
			break
		elif j in r1.keys():
			rev[j]=r1[j]
			flag=1
			break
		elif j in r2.keys():
			rev[j]=r2[j]
			flag=1
			break
		elif j in r3.keys():
			rev[j]=r3[j]
			flag=1
			break
		elif j in r4.keys():
			rev[j]=r4[j]
			flag=1
			break
		elif j in r5.keys():
			rev[j]=r5[j]
			flag=1
			break
		elif j in r6.keys():
			rev[j]=r6[j]
			flag=1
			break
		elif j in r7.keys():
			rev[j]=r7[j]
			flag=1
			break
		elif j in r8.keys():
			rev[j]=r8[j]
			flag=1
			break
		else:
			rev[j]="Sorry no data available now."
		pickle.dump(rev,open("g_review.p","wb"))