import json
import requests

# data to be stored in the text file
data = {
    "name": "Yuvashree",
    "age": 22,
    "city": "Bangalore"
}

# Create a text file and store data
filename = 'data.txt'
with open(filename, 'w') as file:
    file.write(json.dumps(data))

print(f'Data stored in {filename}')

# Convert data to JSON format
with open(filename, 'r') as file:
    json_data = json.load(file)

# Send JSON data through an API call
api_url = 'https://reqres.in/api/users'
headers = {'Content-Type': 'application/json'}

response = requests.post(api_url, headers=headers, json=json_data)

if response.status_code == 200 or response.status_code == 201:
    print('Data successfully sent to the API')
    print(response.text)
else:
    print(f'Failed to send data. Status code: {response.status_code}')
    print(response.text)

