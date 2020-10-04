import requests
from hashlib import md5
import json
URL = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
URL3= 'https://ru.wikipedia.org/wiki/'

class CountryIterator:
    def __init__(self):
        self.session = requests.Session()

    def __iter__(self):
        return self
    def __next__(self):
        return

    def __next__(self):
        d = self.country()
        c = self.link(d)

        return self.write_file(d, c)

    def country(self):
        contres = self.session.get(URL)

        for x in contres.json():
            country = x['name']['common']
            return country

    def link(self,country):
        s = country.split()
        s = '_'.join(s)
        link = (URL3) + (s)
        return link


    def write_file(self,country, link):
        with open('cantry.txt', 'a', encoding='utf-8') as file:
            file.write(f'{country}-{link}''\n')





