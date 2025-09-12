import sys

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types





def main():
    print("Hello from ai-agent!")
    
    if len(sys.argv) < 2: 
        print("error: missing prompt")
        exit(1)
    #check for prompt

    prompt = sys.argv[1]
    
    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]
    #list of user prompts

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
    )
    #generate answer
    text = str(response.usage_metadata)

    if len(sys.argv) >= 3:
        if sys.argv[2] == "--verbose":
            print(f"User prompt: {prompt}")
            #print user prompt

            index_X = text.find("prompt_token_count=")+len("prompt_token_count=")
            index_Y = text.find("candidates_token_count=")+len("candidates_token_count=")

            value_X = text[index_X:index_X+2]
            value_Y = text[index_Y:index_Y+2]

            print(f"Prompt tokens: {value_X}\nResponse tokens: {value_Y}")
            #print tokens
        else:
            print(f"Unknown flag: {sys.argv[2]}")
    
    print(response.text)
    #print(text)
   

if __name__ == "__main__":
    main()
