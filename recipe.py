from openai import OpenAI
import os

'''
# set OpenAI API key
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

if not OpenAI.api_key:
    raise ValueError("api_key is not set")
'''

def ask_gpt(prompt):
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    print(completion.choices[0].message.content)


def main():
    ask_gpt("1+1等于几")

main()





'''
How to set key of openai?
1. 
export OPENAI_API_KEY="your_openai_api_key"
2. 
echo $OPENAI_API_KEY

'''