from langchain_google_genai import ChatGoogleGenerativeAI
import os

# initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key=os.getenv("GEMINI_APT_KEY")
)

# simple invocation / prompt
def temp():
    response = llm.invoke("Write a short poem about the moon.")
    return response