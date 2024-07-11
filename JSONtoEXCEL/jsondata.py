import pandas as pd

# json data
json_data = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

# Extract data from JSON
data_id = json_data['data']['id']
email = json_data['data']['email']
first_name = json_data['data']['first_name']
last_name = json_data['data']['last_name']
avatar = json_data['data']['avatar']
support_url = json_data['support']['url']
support_text = json_data['support']['text']

# Create a DataFrame
df = pd.DataFrame({
    'ID': [data_id],
    'Email': [email],
    'First Name': [first_name],
    'Last Name': [last_name],
    'Avatar': [avatar],
    'Support URL': [support_url],
    'Support Text': [support_text]
})

# Define Excel file name
excel_file = 'jsondata.xlsx'

# DataFrame to Excel
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f'Data has been written to {excel_file}')
