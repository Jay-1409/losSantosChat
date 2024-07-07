from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

characters = {
    "character1": "Franklin",
    "character2": "Micheal",
    "character3": "Trevor"
}

@app.route('/')
def index():
    return render_template('index.html', characters=characters)
@app.route('/index2.html')
def index2():
    return render_template('index2.html',characters=characters)
@app.route('/chat/character1')
def chat_character1():
    return render_template('chat_character1.html', character=characters["character1"])
@app.route('/chat/character2')
def chat_character2():
    return render_template('chat_character2.html', character=characters["character2"])
@app.route('/chat/character3')
def chat_character3():
    return render_template('chat_character3.html', character=characters["character3"])

@app.route('/chat', methods=['POST'])
def chat_response():
    message = request.form['message']
    character = request.form['character']
    response = f"Response from {character}: {message}"  # Placeholder response logic
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
