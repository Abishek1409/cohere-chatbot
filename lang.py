import cohere
import os
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(api_key=os.getenv("api_key"))

print("Enter a large paragraph")
para = input()

prompt='summarize this paragraph to no more than 30 words\n paragraph: ' + para

res = co.chat(
    model='command-r-plus',
    message=prompt,
)

print('\n Summerized Text\n' + res.text)

