from selenium import webdriver
s = raw_input().split(' ')
s="/".join([str(x) for x in s])
s="https://www.zigwheels.com/newcars/"+s
print s