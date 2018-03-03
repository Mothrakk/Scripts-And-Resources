#Downloads every .mp3 from keygenjukebox.net

import requests
from bs4 import BeautifulSoup as soup

def Download(filename, url):
	with open(filename, "wb") as file:
		file.write(requests.get(url).content)

counter = 0
url = "http://keygenjukebox.net"

r = requests.get(url)
parsed = soup(r.content, "html.parser")
container = parsed.findAll("a")

for link in container:
	newurl = (url + link.get("href"))
	filename = link.text
	filename = filename.replace("_"," ")
	try:
		Download(filename, newurl)
		counter += 1
		print("Downloaded %d - %s" %(counter, filename))
	except Exception as e:
		print(e)