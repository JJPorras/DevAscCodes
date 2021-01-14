#INVALID URI
import requests

url = "uri or url.com/efw"
resp = requests.get(url, verify = False)
print(resp)
