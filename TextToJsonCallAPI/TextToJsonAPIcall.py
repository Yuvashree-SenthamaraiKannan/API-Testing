import json
import requests

# file name
file_path = 'data.txt'

# Initialize an empty dictionary to hold the parsed data
data_dict = {}

# Read data from the text file and convert to JSON
with open(file_path, 'r') as file:
    for line in file:
        key, value = line.strip().split(': ')
        data_dict[key] = value

# Convert dictionary to JSON format
json_data = json.dumps(data_dict, indent=4)


print("JSON data:")
print(json_data)

# Send JSON data through an API call
api_url = 'https://reqres.in/api/users'
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(api_url, headers=headers, json=data_dict)


    if response.status_code == 200 or response.status_code == 201:
        print('Data successfully sent to the API')
        print(response.text)
        print(response.status_code)
    else:
        print(f'Failed to send data. Status code: {response.status_code}')
        print(response.text)
except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')


"""
output : 

JSON data:
{
    "name": "Yuvashree ,",
    "age": "22,",
    "city": "Bangalore"
}
Data successfully sent to the API
{"name":"Yuvashree ,","age":"22,","city":"Bangalore","id":"362","createdAt":"2024-07-18T05:29:05.000Z"}
201
"""