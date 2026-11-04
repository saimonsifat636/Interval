import requests
queries=input("please enter what you want: ")
key="2639f033bdef4c0a9d595ddad3a3df90"

url=f"https://newsapi.org/v2/everything?q={queries}&from=2026-09-26&sortBy=publishedAt&apiKey={key}"

r=requests.get(url)
data=r.json()  # it is storing nested dectionary.
article=data['articles']   # -> This is a dectionary key and it will return the dectionary value on that key.
for index,articl in enumerate(article):   # -> it will fetch each dectionay from key from that dectionary 
    print(f"{index+1}",articl['title'])
    print(articl["url"])
    print("\n____________________________________________\n")