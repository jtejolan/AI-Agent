import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)


#Argument Parser - Accepts the prompt as well as the verbose flag
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
)

if response.usage_metadata is None:
    raise RuntimeError("No usage metadata found")

if args.verbose:
    print(f"User prompt: {args.prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens:{response.usage_metadata.candidates_token_count}")


print(response.text)