from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful assistant in {domain}.'),
    ('human', 'explain {input} in simple terms')
])

prompt = chat_template.invoke({'domain': 'Cricket', 'input':'What is a googly?'})

print(prompt)