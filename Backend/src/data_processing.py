import pandas as pd
import csv
import openai
from openai import OpenAI
import random
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an AI assistant designed to score users' prompts and assign a score to them based on their level of empathy."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)

# Test OpenAI GPT-4
# ai_prompt = "Provide empathetic advice: My partner just left me, and I feel lost."
# ai_response = generate_response(ai_prompt)
# print("AI Response:", ai_response)

# def load_empathy_dataset(file_path):
#     """Load and display the first few rows of a dataset."""
#     data = pd.read_csv(
#         "./data/raw/empatheticdialogues/train.csv",
#         delimiter=",",  # Ensure the correct delimiter
#         quoting=3,      # Disable special handling for quotation marks
#         engine="python" # Use Python's parser for more flexibility
#     )
#     return data

# def auto_score_ai_response(response):
#     """Basic example of automated scoring based on keyword matching."""
#     keywords = ["sorry", "support", "help", "alone", "hard"]
#     score = sum(1 for word in keywords if word in response.lower())
#     return min(score, 10)  # Cap the score at 10

# def generate_responses_from_empathy_dataset():
#     file_path = "../data/raw/empatheticdialogues/train.csv"
#     data = load_empathy_dataset(file_path)
#     output_file = "data/processed/evaluation_results.csv" 

#     results = []

#     # Randomly select a context
#     rand_int = random.randint(0, len(data) - 1)
#     context = data.loc[rand_int, 'prompt']

#     ai_prompt = f"Create a prompt for the AI that reinforces this situation (the goal is to get the AI to generate a response that evokes empathy): {context}"

#     # Example manual scores
#     sensitivity_score = 8
#     inclusivity_score = 7
    
#     results.append( {
#         "context": context,
#         "response": ai_response,
#     })
    
#     # Save to a new CSV file
#     output_file = "data/processed/ai_generated_responses.csv"
#     pd.DataFrame(results).to_csv(output_file, index=False)
#     print(f"AI responses saved to {output_file}")

if __name__ == "__main__":
    generate_responses_from_empathy_dataset()