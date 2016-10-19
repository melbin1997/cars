import pickle
import time
a=pickle.load(open("output.p","rb"))
'''b=pickle.load(open("id.p","rb"))
ip=raw_input("Enter the name of the vehicle: ")
for key in b:
	if b[key]==ip:
		k=key
print a[int(ip)]'''
#print a
'''for key in a.keys():
	a[str(key)]=a[key]
	del(a[key])'''
for key in a:
	print
	print type(key)
	print a[key]
print
print len(a)