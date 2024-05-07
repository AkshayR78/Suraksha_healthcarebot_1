import openai

# Set your OpenAI API key
openai.api_key = "sk-proj-2zbKJlZ5MUrrViwTwEUBT3BlbkFJyjG4k313ivUtY556gxxs"

# Initialize the OpenAI client
client = openai.ChatCompletion.create

def get_openai_response(user_input):
    # Use a supported model like "text-davinci-codex"
    response = client(
        model="text-davinci-codex",
        messages=[
            {
                "role": "user",
                "content": user_input
            },
            {
                "role": "assistant",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Return the response text
    return response.choices[0].content.strip() if response.choices else None
