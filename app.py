from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def start_flask():
    return "hello flask"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)