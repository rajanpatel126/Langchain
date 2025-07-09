from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
# result = embeddings.embed_query("My name is Rajan and I am a data scientist")
# print(str(result))

documents = [
    "Hello, my name is Rajan and I am a data scientist.",
    "I love working with data and building machine learning models.",
    "Data science is a fascinating field that combines statistics, programming, and domain knowledge.",
    "Rajan enjoys analyzing data to extract insights and make informed decisions."
]

result_docs = embeddings.embed_documents(documents)
for i, doc in enumerate(result_docs):
    print(f"Document {i+1}: {str(doc)}")
