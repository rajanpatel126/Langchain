from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint( #type: ignore
    repo_id='google/gemma-2-2b-it',
    task='text-generation',
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='The first fact'),
    ResponseSchema(name='fact_2', description='The second fact'),
    ResponseSchema(name='fact_3', description='The third fact'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give me 3 facts about the topic: {topic}. \n{format_instructions}\n',
    input_variables = ['topic'],
    partial_variables = {'format_instructions': parser.get_format_instructions()},
)

chain = template | model | parser

output = chain.invoke({'topic': 'The Bermuda Triangle'})
print(output)
 