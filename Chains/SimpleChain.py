from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="Write 5 sarcastic line about the country: {country}?",
    input_variables=["country"],
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

chain.get_graph().print_ascii()