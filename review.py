from bs4 import BeautifulSoup
import urllib
import re
import pickle

a=pickle.load(open("combined_links.p","rb"))
review = {}
failed = []

for url in a.values():
	try:
		print url
		review_mat = ''
		page = urllib.urlopen(url)
		soup = BeautifulSoup(page.read())
		soup=soup.find("section", {"id": "aboutmodelproduct"})
		for node in soup.findAll('p'):
				print '\n'.join(node.findAll(text=True))
				review_mat += '\n'.join(node.findAll(text=True))
		review[url] = review_mat
	except Exception as e:
		print url
		failed.append(url)

pickle.dump(review, open("review.p", "wb"))
pickle.dump(failed, open("failed_rev_url", "wb"))