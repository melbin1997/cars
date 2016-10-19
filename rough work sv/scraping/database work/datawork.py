import pickle
a=pickle.load(open("output.p","rb"))
'''y=input()
z=0
for i in a:
	if z==y:
		print a[str(i)]
		break
	z+=1'''
c=[1]
for i in a:
	print a[str(i)]
	for j in a[str(i)]:
		#print a[str(i)][j]
		for k in a[str(i)][j]:
			#print a[str(i)][j][k]
			for l in a[str(i)][j][k]:
				#print l
				for m in range(len(a[str(i)][j][k])):
					#print
					if (a[str(i)][j][k][m] not in c):
						c.append(a[str(i)][j][k][m])
	break


'''for i in c:
	print i
print 
print
print c'''
'''1124 Santa Cruz Way	Winter Springs	32708

Tvm to Doha 23 E and 23 F 
Doha to Miami 19 K and 19 J'''