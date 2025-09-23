from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text: \n{text}',
    input_variables=["text"],
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text: \n{text}',
    input_variables=["text"],
)

prompt3 = PromptTemplate(
    template='Combine these two results into a single document: Notes: {notes}, Q&A: {qa}',
    input_variables=["notes", "qa"]
)

model1 = ChatOpenAI()

model2 = ChatAnthropic(model_name="claude-3", timeout=120, stop=['\n'])

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "qa": prompt2 | model2 | parser,
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

chain.get_graph().print_ascii()