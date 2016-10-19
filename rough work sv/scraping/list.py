from selenium import webdriver
import time

q = time.time()
driver = webdriver.Chrome()
driver.get("https://www.cardekho.com/")
driver.find_element_by_id("searchNewCarByBrandInputDiv").click()
s = driver.find_element_by_id("newCarBrandSelect")
a = [s.text]
a = [a[0].encode('UTF8') for x in a]
a = a[0].split('\n')
a = a[14:]
# print a
# print type(a[0])
# print a
# print a[0]
# print type(a[0])
c = []
for i in range(15, 57):
    element = driver.find_element_by_xpath("//*[@id='newCarBrandSelect']/option[" + str(i) + "]").click()
    t = driver.find_element_by_id("newCarModelSelect")
    b = [t.text]
    b = [b[0].encode('UTF8') for x in b]
    b = b[0].split('\n')
    if '-Upcoming Model-' in b:
        b.remove('-Upcoming Model-')
    if '-Upcoming Models-' in b:
        b.remove('-Upcoming Models-')
    if '-Select Model-' in b:
        b.remove('-Select Model-')
    c.append(b)
    # print a
    # time.sleep(10)
# print c
d = []
# print a
# print c
'''for i in a:
    for j in c:
        for k in j:
            d.append(i+' '+k)'''
i = 0
while i < len(a):
    j = 0
    while j < len(c[i]):
        d.append(a[i] + ' ' + c[i][j])
        j += 1
    i += 1
'''while(i<len(a)):
...     j=0
...     while(j<len(k[i])):
...             c.append(a[i]+k[i][j])
...             j+=1
...     i+=1'''

print d  # List of all cars
# time.sleep(0.5)
print
print "Total No of cars=", len(d)
print "Total time taken=", time.time() - q
