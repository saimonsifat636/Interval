import requests  # type: ignore[reportMissingModuleSource]
r = requests.get('https://api.github.com/events')
print(r.text)

with open('data.txt','w') as file:
    file.write(r.text)
    