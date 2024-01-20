from flask import Flask, render_template, request, redirect, url_for
import openai

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = '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'

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    prompt="generate a geography quiz question"
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=5
    )
    return render_template('questions.html', questions=response)
