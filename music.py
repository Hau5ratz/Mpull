import sys
import os
import requests
from bs4 import BeautifulSoup
from pprint import pprint as p

os.system("clear")

d = "/data/data/com.termux/files/home/storage/music/"
notes = "/data/data/com.termux/files/home/storage/shared/My Documents/notes/Songs.txt" 
sample = "https://www.google.com/search?q=site%3Awww.youtube.com+i+like+to+singa"
template = "https://www.google.com/search?q=site%%3Awww.youtube.com+%s"
yt_dl = "youtube-dl --extract-audio --audio-format mp3 %s"
os.chdir(d)
dll = []

def query(x):
	'''Takes song name queries google and returns URL'''
	b = []
	result = requests.get(template%x)
	assert result.status_code == 200, "Error with connection to google"
	soup = BeautifulSoup(result.content, features="html.parser")
	results = soup.find_all("div", {"class": "g"})
	for tag in results:
		cites = tag.find_all("cite")
		for c in cites:
			b += [c.text]
	return b[0]
		


def clean(name):
	'''Transforms text name to query valid syntax'''
	if ' ' in name:
		\
		name = name.replace(' ','+')
	return name

def download(url):
	os.system(yt_dl%url)
	
lines = []
if sys.argv[1:]:
	for x in sys.argv[1:]:
		assert isinstance(x, str), "Invalid arguement type must be song name as string"
		lines += [x]
else:
	assert os.path.isfile(notes), "File path still not valid"
	with open(notes,'r') as file:
		lines = [x.replace('\n','') for x in file.readlines()]
		
for x in lines:
	print("Searching for song: %s"%x)
	dll += [query(clean(x))]
	print("Found: %s"%(dll[-1])
	
[download(y) for y in dll]
print("Finished")
