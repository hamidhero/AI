from BeautifulSoup import BeautifulSoup
import urllib2 
import re

resp = urllib2.urlopen("http://en.wikipedia.org/wiki/2008_in_film")

html = str(resp.read())
soup = BeautifulSoup(html)
links = soup("i")
#print len(links)

for i in range(134, 327):
	start = str(links[i]).find('>', 4)
	print str(links[i])[start+1: -8]



