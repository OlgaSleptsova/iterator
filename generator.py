import requests
from hashlib import md5
import json
URL = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'

# v=requests.get(URL)
# for z in v.json():
#     print(json.dumps(z))
def country_generator(url):
    countres = requests.get(url)
    hash =[]
    for country in countres.json():
        d= json.dumps(country)

        hashed_password = md5(d.encode()).hexdigest()

    yield hash.append(hashed_password)


print(country_generator(URL))