## Using api end-point
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
#     )

# model = ChatHuggingFace(llm=llm)

# result = model.invoke("What is the capital of France?")
# print(result.content)

## Using downloaded model
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/HuggingFace_cache'  # Set the Hugging Face cache directory
llm = HuggingFacePipeline.from_model_id(
 model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature= 0.1,
        max_new_tokens=100,
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of Australia?")
print(result.content)