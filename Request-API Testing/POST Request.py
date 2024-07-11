import requests

url_post = "https://reqres.in/api/users"

headers = {
    'Content-Type':'application/json; charset=utf-8' ,
    'Content-Length':'84'
}

payload = {
    'name': 'John Doe',
    'job': 'Engineer'
}

response = requests.post(url_post,headers=headers, json=payload)
print(response.status_code)

try:
    if response.status_code == 201:
        print("Response code is 201")
        print(response.json())
    else:
        print(f"Request was not successful. Actual Status code: {response.status_code}")


except requests.exceptions.Timeout:
    print('Timeout error occurred. Please try again later.')

except requests.exceptions.TooManyRedirects:
    print('Too many redirects. Try a different URL.')

except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')

