import requests
from hashlib import md5
import json
URL = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
URL3= 'https://ru.wikipedia.org/wiki/'
class CountryIterator:
    def __init__(self,start,end):
        self.session = requests.Session()

    def __iter__(self):
        return self
    def __next__(self):

        def country(self):
            contres = self.session.get(URL)
            for ftg in contres.json():
                country = ftg['name']['common']
            return country

        def link(self,country):
            s = country.split()
            s = '_'.join(s)
            link =(URL3)+(s)
            return link
        country = country()
        link = link(country)
        def write_file (self,country,link):
            with open('cantry.txt','a',encoding='utf-8') as file:
                file.write(f'{country}-{link}''\n')

def country_generator(url):
    countres = requests.get(url)
    hash =[]
    for country in countres.json():
        d= json.dumps(country)

        hashed_password = md5(d.encode()).hexdigest()
        hash.append(hashed_password)
    return hash

print(country_generator(URL))