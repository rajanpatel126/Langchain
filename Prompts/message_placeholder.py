from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support assistant.'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{query}')
])

chat_history = []
# load chat History
with open('chat_history.txt', 'r') as file:
    chat_history.extend(file.readlines())
    
chat_template.invoke({'chat_history': chat_history, 'query':'What is the status of my order?'})