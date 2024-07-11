import requests

url = 'https://reqres.in/api/users'
params = {'page': 2}
headers = {'Content-Type':'application/json; charset=utf-8'}

response = requests.get(url, params=params, headers=headers)
print(response.status_code)

try:
    if response.status_code == 200:
        print("Response code is 200")
        print(response.json())
    else:
        print(f"Request was not successful. Actual Status code: {response.status_code}")

except:
    print("An error occurred")