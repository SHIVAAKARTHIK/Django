import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'apiJsonCBVMixin/'

resp = requests.get(BASE_URL+END_POINT)
data = resp.json()
print(data)
