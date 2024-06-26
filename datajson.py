import pandas as pd

# json data
json_data = {
    "data": {
         "first_name": "Janet",
         "last_name": "Weaver",
         "email": "janet.weaver@reqres.in",
         "id": 2
    }
}

# Extract data from JSON
first_name = json_data['data']['first_name']
last_name = json_data['data']['last_name']
email = json_data['data']['email']
data_id = json_data['data']['id']

# Create a DataFrame
df = pd.DataFrame({
    'First Name': [first_name],
    'Last Name': [last_name],
    'Email': [email],
    'ID': [data_id]
})

# Define Excel file name
excel_file = 'datajson.xlsx'

# DataFrame to Excel
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f'Data has been written to {excel_file}')
