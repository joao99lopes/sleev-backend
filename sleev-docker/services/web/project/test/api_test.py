import requests

url = 'http://127.0.0.1:1338/user/delete_all'  # Replace with your Flask server URL
add_user_data = {'first_name': 'Joao', 'last_name': 'Lopes', 'email': 'alice_inwasfonderland@test.com', 'password': 'complexpassword'}
delete_user_data = {'email': 'alice_inwasfonderland@test.com'}

response = requests.post(url, json=add_user_data)

print(response.status_code)  # Get the HTTP status code of the response
print(response.json())