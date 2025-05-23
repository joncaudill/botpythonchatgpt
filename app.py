from openai import OpenAI
import os

# pass api key
# this is a secret key, do not share it with anyone
# and absolutely do not share it in public repositories
# windows method of securing via environment variables
# for mac version, you'll need to set the environment variable in your terminal
secret = os.environ.get('OPENAI_TEST_KEY')
if secret is None:
    raise ValueError("API key not found. Please set the OPENAI_TEST_KEY environment variable.")
client = OpenAI(api_key = secret)


# define prompt
message = {'role': 'user', 'content': 'Hello, how are you?'}
messages = []
messages.append(message)

# make an api call
response = client.chat.completions.create(messages=messages, model='gpt-4.1')

# print the response
print (response.choices[0].message.content)