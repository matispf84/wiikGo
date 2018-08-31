from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/item')
def get_item():
    return "Hola"


app.run(port=5000)