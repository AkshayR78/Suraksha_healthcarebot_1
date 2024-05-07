import requests
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# OpenAI API Key
OPENAI_API_KEY = "sk-proj-2zbKJlZ5MUrrViwTwEUBT3BlbkFJyjG4k313ivUtY556gxxs"

# OpenAI Playground Endpoint
PLAYGROUND_ENDPOINT = "https://platform.openai.com/playground/chat"

# Hardcoded greeting messages
GREETING_MESSAGES = ["Hello! How can I assist you today?", "Hi there! Are you feeling unwell?",
                     "Greetings! What brings you here today?", "Hey! Is there something I can help you with?"]

# Hardcoded responses for medical treatments
TREATMENT_RESPONSES = {
    "burns": "I'm sorry to hear that you have a burn injury. Here's what you should do: Cool the burn with cool or lukewarm water for about 20 minutes. Then, cover the burn with a clean, dry cloth or bandage. Seek medical attention if necessary.",
    "snake_bites": "Oh no, a snake bite can be dangerous. Here's what you should do: Try to remain calm and still, and remove any tight clothing or jewelry near the bite. Keep the affected limb immobilized and below the heart level. Seek immediate medical help."
}

# Video URLs for treatments
VIDEO_URLS = {
    "burns": "https://www.example.com/burns_video",
    "snake_bites": "https://www.example.com/snake_bites_video"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.form['user_input'].lower()
    
    # Check if OpenAI API key is provided
    if OPENAI_API_KEY:
        response = send_request_to_openai(user_input)
        if response:
            return render_template("index.html", response=response)
    
    # Use hardcoded responses if ChatGPT Playground API doesn't provide output
    if any(word in user_input for word in ["hello", "hi", "greetings", "hey"]):
        response = get_random_greeting()
    elif "burn" in user_input:
        response = TREATMENT_RESPONSES["burns"]
    elif "snake bite" in user_input:
        response = TREATMENT_RESPONSES["snake_bites"]
    else:
        response = "I'm sorry, I couldn't understand that. Can you please provide more details?"

    return render_template("index.html", response=response)

def send_request_to_openai(user_input):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "text-davinci-002",
        "prompt": user_input,
        "max_tokens": 50
    }
    response = requests.post(PLAYGROUND_ENDPOINT, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]["text"]
    else:
        return None

def get_random_greeting():
    return random.choice(GREETING_MESSAGES)

if __name__ == "__main__":
    app.run(debug=True)
