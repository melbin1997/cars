import pickle
fileObject = open("carnm",'r')
dat = pickle.load(fileObject)
val = 0
'''
for i in dat.keys():
	s = 'regiondb["' + i + '"] = ['
	for temp in dat[i]:
		 s = s + '{value:"' +temp+'", text:"' + temp +'"},'
	val+=1
	s = s[:-1] +  "];" 
	print s
'''
temp = dat.keys()
temp.sort()
for i in temp:
	s = '<option value="' + i + '">' + i + "</option>"
	print s
'''
regiondb["0"] = [{value:"102", text:"Cairo"},
                      {value:"88", text:"Lagos"},
                      {value:"80", text:"Nairobi"},
                      {value:"55", text:"Pretoria"}];
'''
