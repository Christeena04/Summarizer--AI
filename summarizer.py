# summarizer.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("sk-xxxxxxxxxxxxxxxxxxxxxxxx")

def read_input_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_summary(text):
    prompt = f"Summarize the following text in 3–4 lines:\n\n{text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response['choices'][0]['message']['content'].strip()

def write_summary_file(summary, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(summary)

def main():
    input_text = read_input_file('input.txt')
    summary = generate_summary(input_text)
    write_summary_file(summary, 'output_summary.txt')
    print("✅ Real summary written to output_summary.txt")

if __name__ == "__main__":
    main()
