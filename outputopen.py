import pickle
fileObject = open("carnm",'r')
dat = pickle.load(fileObject)
val = 0
for i in dat.keys():
	s = 'regiondb["' + str(val) + '"] = ['
	for temp in dat[i]:
		 s = s + '{value:"' +temp+'", text:"' + temp +'"},'
	val+=1
	s = s[:-1] +  "];" 
	print s

'''
regiondb["0"] = [{value:"102", text:"Cairo"},
                      {value:"88", text:"Lagos"},
                      {value:"80", text:"Nairobi"},
                      {value:"55", text:"Pretoria"}];
'''
