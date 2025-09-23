from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a professional detailed report on topic: {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template='Write 5 essential and key points from the following report: {report}',
    input_variables=["report"],
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

chain.get_graph().print_ascii()

chain.invoke({"topic": "Job Market in Australia"})
