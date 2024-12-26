from flask import Flask, request, jsonify
from openai import OpenAI
import openai

app = Flask(__name__)
app.config["DEBUG"] = True

client = OpenAI()

@app.route("/chat", methods=["POST"])
def chat():
    # Initialize the message history
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

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
        return jsonify({"response": assistant_reply})
    except openai.error.OpenAIError as e:
        return jsonify({f"An error occurred: {e}"})

if __name__ == "__main__":
    app.run(debug=True)