from google import genai
import os 

client=genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

uploadfile=client.files.upload(file=r'C:\Interval\python A-Z\13_basic_project\photo.avif')

response=client.models.generate_content(
    model="gemini-2.8-flash",
    contents=["describe this picture " , uploadfile]
)


print(response.text)