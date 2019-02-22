import sys
import os
import requests
from bs4 import BeautifulSoup
from pprint import pprint as p

os.system("clear")
sample = "https://www.google.com/search?q=site%3Awww.youtube.com+i+like+to+singa"
template = "https://www.google.com/search?q=site%3Awww.youtube.com+%s"
dll = []

def query(x):
	'''Takes song name queries google and returns URL'''
	result = requests.get(template)
	assert result.status_code == 200, "Error with connection to google"
	soup = BeautifulSoup(result.content, features="html.parser")
	results = soup.find_all('a', href=True)
	p(results)


def clean(name):
	'''Transforms text name to query valid syntax'''
	if ' ' in name:
		\
		name = name.replace(' ','+')
	return name

if sys.argv[1:]:
	for x in sys.argv[1:]:
		assert isinstance(x, str), "Invalid arguement type must be song name as string"
		print("Searching for song: %s"%x)
		dll += [query(clean(x))]
