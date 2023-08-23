import requests
from datetime import datetime

url = 'http://127.0.0.1:1338/user/migrate'  # Replace with your Flask server URL
add_user_data = {
    'first_name': 'tttt', 
    'last_name': 'Lopes', 
    'email': 'luizinhoaa@test.com', 
    'password': 'complexpassword',
    "birth_date": (datetime(1999, 11, 6)).isoformat(),
    "scout_id": 1,
    "scout_group": 158,
    "role": 'leader',
    }
    
delete_user_data = {'email': 'alice_inwasfonderland@test.com'}

#response = requests.post(url, json=add_user_data)
response = requests.post(url)

print(response.status_code)  # Get the HTTP status code of the response
print(response.json())