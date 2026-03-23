from flask import Flask, jsonify, request
from flask_cors import CORS
from generate_sudoku_handler import generate_sudoku, create_puzzle

app = Flask(__name__)
CORS(app) #allows React App to talk to Flask

@app.route('/api/puzzle', methods=['GET'])
def get_puzzle():
    difficulty = request.args.get('difficulty', 'medium')
    solution = generate_sudoku()
    puzzle = create_puzzle(solution, difficulty)
    return jsonify({"puzzle": puzzle, "solution": solution})

if __name__ == '__main__':
    app.run(debug=True, port=8080)