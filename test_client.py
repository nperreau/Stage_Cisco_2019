import requests

temp = 5.0
humi = 6.5

URL = "http://localhost:8001/setinfo"

PARAMS = {'temp':temp, 'humi':humi} 

r = requests.get(url = URL, params = PARAMS)

print r.text
