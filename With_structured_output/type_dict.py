from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI

# class Person(TypedDict):
#     name: str
#     age: int
    
# new_person: Person = {
#     'name': 'Rajan',
#     'age': 22
# }

# another_person: Person = {
#     'name': 'John',
#     'age': '30'
# }

model = ChatOpenAI()
class Review(TypedDict):
    summary: Annotated[str, 'Summarize the review in one sentence.']
    sentiment: Annotated[str, 'Sentiment of the review.']  # e.g., Positive, Negative, Neutral
    
structured_model = model.with_structured_output(Review)
result = structured_model.invoke("The movie INTERSTELLAR was a masterpiece. The visuals were stunning and the plot was mind-bending. I loved the character development and the emotional depth of the story. Overall, it was an unforgettable experience.")

print(result)
print(result['summary'])
print(result['sentiment'])

# The prompt was automatically generated in the backend 