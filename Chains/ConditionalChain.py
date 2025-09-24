from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from pydantic import BaseModel, Field
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="The sentiment of the feedback, either 'positive' or 'negative'")
    
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback into postive or negative: \n{feedback} \n{format_instructions}',
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template='Write an appropiate response to this positive feedback: {feedback}',
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template='Write an appropiate response to this negative feedback: {feedback}',
    input_variables=["feedback"],
)

classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser), # type: ignore
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser), # type: ignore
    RunnableLambda(lambda x: "Could not classify the sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback": "The product quality is really good and I am satisfied with my purchase."})

print(result)