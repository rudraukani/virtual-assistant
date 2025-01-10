import openai

def aiProcess(command):
    openai.api_key = "<Your Key Here>"  # Replace with your actual OpenAI API key

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model
        messages=[ 
            {"role": "system", "content": "You are a virtual assistant skilled in general tasks. Give short responses."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message['content']  # Accessing the response text
