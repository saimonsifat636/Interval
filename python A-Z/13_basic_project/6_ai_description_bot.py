
from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)




user=input("what you want to know ? \n")
response = client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents=user
)

for stream in response:
    print(stream.text)
