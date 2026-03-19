from flask import Flask, jsonify
from flask_cors import CORS
from server.generate_sudoku_handler import *

app = Flask(__name__)
CORS(app) #allows React App to talk to Flask

@app.route('/api/puzzle', methods=['GET'])
def get_puzzle():

    puzzle = generate_sudoku()
    return jsonify({"puzzle": puzzle})

if __name__ == '__main__':
    app.run(debug=True, port=5000)