from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2b',
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

# 1st prompt -> Detailed report
template1 = PromptTemplate(
    template="Write a detailed report on the following topic: {topic}",
    input_variables=["topic"]
)

# 2nd prompt -> Summary
template2 = PromptTemplate(
    template="Summarize the following report in 5 lines: {report}",
    input_variables=["report"]
)

# prompt1 = template1.invoke({'topic': 'MCP vs A2A vs ACP vs ANP protocols in agent communication'})

# res1 = model.invoke(prompt1)

# prompt2 = template2.invoke({'report': res1.content})

# res2 = model.invoke(prompt2)
# print(res2.content)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic': 'MCP vs A2A vs ACP vs ANP protocols in agent communication'})
print(result)