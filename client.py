import openai

# Your OpenAI API key
api_key = "sk-proj-d2oNFBVo02tjehFbuMpfT3BlbkFJhnFLJl8rCHmC1AOwu1bB"

# Initialize the OpenAI client with your API key
openai.api_key = api_key

# Create a chat completion
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Virtual Assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

# Print the response
print(completion.choices[0].message['content'])
