from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
chat=client.chats.create(
    model="gemini-3.8-flash"
)

while True:
    user=input(">")
    if user=='exit':
        break
    response=chat.send_message(user)
    print(response.text)