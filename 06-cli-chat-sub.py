'''
message = [
    {"role": "system","content":"..."},
    {"role": "user","content":"..."},
    {"role": "assistance","content":"..."},
    {"role": "user","content":"..."}
]

for event in stream:
    if hasattr(event, "delta"):
        print(event.delta, end="",flush= True)

'''

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()


system_prompt = """
영어 상황극을 해보자. 스타벅스에서 커피구매.너는점원. 나는 손님
"""

conversations = [
    {"role": "system","content": system_prompt},
    #{"role": "user","content":"start the conversation"}
    ]

response = client.responses.create(
    model="gpt-4o",
    input=conversations,
)


assistant_content: str = response.output_text
print("[AI]",assistant_content)
conversations.append({
    "role" : "assistant"
    "content" : assistant_content
})

user_content: str = input("[HUMAN]").strip()
if user_content :
    conversations.append({
    "role" : "user
    "content" : user_content
})
    response = client.responses.create(
    model="gpt-4o",
    input=conversations,
)
    assistant_content: str = response.output_text
print("[AI]",assistant_content)
conversations.append({
    "role" : "assistant"
    "content" : assistant_content
})
    