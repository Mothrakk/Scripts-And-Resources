from requests import get
from bs4 import BeautifulSoup as soup
from win32clipboard import OpenClipboard, GetClipboardData, CloseClipboard

def Download(filename, url):
	with open(filename, "wb") as file:
		file.write(get(url).content)

def CopyFromClipboard():
	OpenClipboard()
	data = GetClipboardData()
	CloseClipboard()
	return data

r = get(CopyFromClipboard())
parsed = soup(r.content, "html.parser")

imageContainers = parsed.findAll("a", {"class":"fileThumb"})

for container in imageContainers:
	link = "http:" + container.get('href')
	filename = link.split('/')[4]
	Download(filename, link)