from selenium import webdriver
import time

q = time.time()
driver = webdriver.Chrome()
driver.get("file:///home/georgy/Downloads/CarDekho%20-%20Cars%20in%20India,%20New%20Car%20Prices%202016,%20Buy%20and%20Sell%20Used%20Cars%20_%20CarDekho.com.html")
driver.find_element_by_id("searchNewCarByBrandInputDiv").click()
s = driver.find_element_by_id("newCarBrandSelect")
a = [s.text]
a = [a[0].encode('UTF8') for x in a]
a = a[0].split('\n')
a = a[14:]
#print a

output={}
c = []
for i in range(15, 15+len(a)):
    element = driver.find_element_by_xpath("//*[@id='newCarBrandSelect']/option[" + str(i) + "]").click()
    t = driver.find_element_by_id("newCarModelSelect")
    b=[]
    b = [t.text]
    b = [b[0].encode('UTF8') for x in b]
    b = b[0].split('\n')
    j=0
    while j<len(b):
        #print"helloo"
        if b[j]=='-Upcoming Model-' or b[j]=='-Upcoming Models-':
            b=b[0:j]
            #print"hiii"
        j+=1
    if '-Select Model-' in b:
        b.remove('-Select Model-')
    #print b
    #print i
    c.append(b)
    #print len(c[i-15])
    '''print a[i-15]
    print ""
    print c[i-15]
    print ""
    print ""'''
    output[a[i-15]]=c[i-15]
    #time.sleep(1)
# print c
#d = []
print output
print " "
# print a
# print c

'''i = 0
while i < len(a):
    j = 0
    if len(c[i])==0:
        i+=1
        continue
    while j < len(c[i]):
        d.append(a[i] + ' ' + c[i][j])
        j += 1
    i += 1
print d     #list of all cars
print
print "Total No of cars=", len(d)
print "Total time taken=", time.time() - q, "seconds"  
'''