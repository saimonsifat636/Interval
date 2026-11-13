# import requests
# import pandas as pd

# # r=requests.get(r"https://www.w3schools.com/python/pandas/data.js")
# # data=r.text
# # print ((data))

# # with open("new_text.json","w") as f:
# #     f.write(data)
# json_data=pd.read_json("new_text.json")
# print(json_data.to_string())
import pandas as pd
import requests

# 1. Fetch valid JSON data from the correct URL (.json instead of .js)

# 3. Read the file into Pandas and display it
df = pd.read_json("new_text.json")

print(df.head())  # Summarized view
# print(df.to_string()) # Full view without truncationry single row and column without truncation (...)
# print(df.to_string())