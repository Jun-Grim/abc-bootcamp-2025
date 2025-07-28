from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()



stream = client.responses.create(
    model="gpt-4o",
    input="tell me about interesting japan's ancient stroy limit 4line",
    stream= True,
)

for event in stream:
    if hasattr(event, "delta"):
        print(event.delta, end="",flush= True)
