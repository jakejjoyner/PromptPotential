from flask import Flask, request, make_response
from openai import OpenAI
import openai
import json
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True

client = OpenAI()

CORS(app)

# Initialize the message history
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

@app.route("/chat", methods=["POST"])
def chat():

    # Get user input
    user_input = request.get_json(force=True)["message"]
    print(f"You: {user_input}")
    # Exit condition
    if user_input.lower() == "exit":
        print("Ending conversation. Goodbye!")

    # Append user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})
    
    try:
        # Get the ChatGPT response
        response = client.chat.completions.create(
            model="ft:gpt-4o-mini-2024-07-18:personal::AiTfDGWu",  # or "gpt-3.5-turbo"
            messages=conversation_history
        )

        # Extract the assistant's reply
        assistant_reply = response.choices[0].message.content
        print(f"ChatGPT: {assistant_reply}")
        
        # Add the assistant's reply to the conversation history
        conversation_history.append({"role": "assistant", "content": assistant_reply})
        response = json.dumps({"response": assistant_reply})
        response_ =  make_response(response)
        return response_
    except openai.error.OpenAIError as e:
        response = json.dumps({f"An error ocurred: {e}"})
        response_ =  make_response(response)
        return response_

if __name__ == "__main__":
    app.run(debug=True)