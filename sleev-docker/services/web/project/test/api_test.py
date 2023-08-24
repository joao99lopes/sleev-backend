import requests
from datetime import datetime

url = 'http://127.0.0.1:1338/user/login'  # Replace with your Flask server URL
add_user_data = {
    'first_name': 'joao', 
    'last_name': 'Lopes', 
    'email': 'joao@test.com', 
    'password': 'complexpassword',
    "birth_date": (datetime(1999, 11, 6)).isoformat(),
    "scout_id": 1,
    "scout_group": 158,
    "role": 'leader',
    }
    
delete_user_data = {'email': 'alice_inwasfonderland@test.com'}

login_data = {
    'email': 'joao@test.com', 
    'password': 'complexpassword',
    }
    
#response = requests.post(url, json=add_user_data)
response = requests.post(url, json=login_data)

print(response.status_code)  # Get the HTTP status code of the response
print(response.json())