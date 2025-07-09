from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-3.5-turbo-instruct', temperature=0.7)

result = llm.invoke("What is the capital of Australia?")
print(result.content)