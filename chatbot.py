from groq import Groq
from dotenv import load_dotenv
from datetime import datetime
import os
load_dotenv()

api = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api)

messages = []
try:
    while True:
        user_input = input("Enter Your prompt:- ").strip()
        if user_input.lower() == "exit":
            break
        messages.append({"role": "user",
                         "content": user_input})
        res = client.chat.completions.create(model="llama-3.1-8b-instant",
                                             messages=messages, max_tokens= 1000)
        print(res.choices[-1].message.content)
        messages.append({
            "role": "assistant",
            "content": res.choices[-1].message.content
        })
        with open('chat_log.txt', "a+") as f:
            f.write(f"\n {str(datetime.now().strftime("%d/%m/%Y/%H:%M:%S"))}")
            f.write(f"User Input:-  {str(user_input)} \n")
            f.write(f"\n {str(datetime.now().strftime("%d/%m/%Y/%H:%M:%S"))}" )
            f.write(f"AI response:- {res.choices[-1].message.content}, \n")
except Exception as e:
    print(f"Error :-{str(e)}")