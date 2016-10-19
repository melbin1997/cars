from bs4 import BeautifulSoup
import urllib
import re
import pickle

a=pickle.load(open("combined_links.p","rb"))


for url in a.values():
	try:
		print url
		page = urllib.urlopen(url)
		soup = BeautifulSoup(page.read())
		soup=soup.find("section", {"id": "aboutmodelproduct"})
		for node in soup.findAll('p'):
				print '\n'.join(node.findAll(text=True))
	except Exception as e:
		print url