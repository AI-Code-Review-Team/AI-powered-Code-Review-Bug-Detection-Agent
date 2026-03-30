from dotenv import load_dotenv
load_dotenv()
import os
from langchain_groq import ChatGroq

key = os.environ.get('GROQ_API_KEY', 'NOT FOUND')
print(f"Groq Key: {key[:15]}...")

llm = ChatGroq(model="llama3-8b-8192", temperature=0, api_key=key)
try:
    r = llm.invoke("say hello in one word")
    print("Groq SUCCESS:", r.content)
except Exception as e:
    print("Groq FAILED:", str(e))
