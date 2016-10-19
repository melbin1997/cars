import pickle

a=pickle.load(open("output.p","rb"))
b=pickle.load(open("id.p","rb"))

for key2 in b.keys():
	print key2

print 
for key1 in a.keys():
	print key1

for key2 in b.keys():
	for key1 in a.keys():
		if(b[key2]==key1):
			print "hi"
			a[str(key2)]=a[key1]
			del(a[key1])
pickle.dump(a,open("output.p","wb"))
'''b=[]
for i in a:
	b.append(i)
print sorted(b)
print'''
for key in a:
	print key
	print a[key]#[input("Enter the name of the vehicle: ")]
	print
print len(a)
#print a