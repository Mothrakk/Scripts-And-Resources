from sys import argv
from requests import post
from json import loads

cwd = "/".join(argv[0].split("/")[:-1])

filepath_to_image = argv[1]
filepath_to_client_id = cwd + "/client_id.txt"

with open(filepath_to_image, "rb") as file:
	image_binary = file.read()

with open(filepath_to_client_id, "r") as file:
	client_id = file.read()

response = post(
	"https://api.imgur.com/3/image",
	data={"image":image_binary},
	headers={"Authorization":"Client-ID {}".format(client_id)}
	)

parsed = loads(response.content.decode("utf-8"))
link = parsed["data"]["link"]

print(link)