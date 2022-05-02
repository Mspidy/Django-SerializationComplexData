#this is a simple python application to communicate with our django api
#3rd party application
import requests

URL = "http://127.0.0.1:8000/stuinfo"
r = requests.get(url=URL)
data=r.json()
print(data)