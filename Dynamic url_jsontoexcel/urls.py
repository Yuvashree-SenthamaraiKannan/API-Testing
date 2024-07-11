import requests
import pandas as pd

# store data
all_users = []

# loop url 1 to 10
for page in range(1, 11):
    url = f"https://reqres.in/api/users?page={page}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('data', [])
        all_users.extend(data)
        print(url)
    else:
        print(f"Failed {url} {page}")

# Create DataFrame
df = pd.DataFrame(all_users)

# Sort DataFrame by 'first_name' in ascending order
df_sorted = df.sort_values(by='first_name')

# Excel
excel_file = 'urls.xlsx'
df_sorted.to_excel(excel_file, index=False)

print(f"Data has been written to {excel_file}")