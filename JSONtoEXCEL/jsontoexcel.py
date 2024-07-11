import pandas as pd

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

# json to dataframe
df = pd.json_normalize(json_data)
# define excel excel file name
excel_filename = "jsontoexcel.xlsx"
# dataframe to excel
df.to_excel(excel_filename,index=False)
