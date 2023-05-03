from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def api():
    return jsonify({'message': 'Hello World'})

@app.route('/voice', methods=['POST'])
def voice():
    data = request.get_json()
    print("data",data)
    text = data['text']
    print(text)
    return jsonify({'text': text+'-server' })


if __name__ == '__main__':
    app.run(debug=True)

