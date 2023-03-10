from flask import Flask, request, jsonify
import openai
import os
app = Flask(__name__)
# Set up the OpenAI API credentials
openai.api_key = os.environ['API']

# Define the route for generating bot responses
@app.route('/api/bot', methods=['POST'])
def generate_response():
    print(os.environ['API'])
    user_input = request.json['input']
    print(user_input)
    # return jsonify({'response': 'message'})
    model_engine = "text-davinci-003"
    prompt = (f"{user_input}")
    
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    print(message)
    # print(message)
    return jsonify({'response': message})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
