from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# Set your OpenAI API key directly
os.environ['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')

print("Openai API key: ",os.environ['OPENAI_API_KEY'])
# llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.7)

# result = llm.invoke("What is the capital of Australia?")
# print(result.content)
