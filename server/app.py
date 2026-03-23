from flask import Flask, jsonify
from flask_cors import CORS
from generate_sudoku_handler import generate_sudoku, create_puzzle
from empty_grid_handler import get_empty_grid

app = Flask(__name__)
CORS(app) #allows React App to talk to Flask

@app.route('/api/puzzle', methods=['GET'])
def get_puzzle():
    difficulty = request.args.get('difficulty')
    solution = generate_sudoku()
    puzzle = create_puzzle(solution, difficulty)
    return jsonify({"puzzle": puzzle, "solution": solution})

if __name__ == '__main__':
    app.run(debug=True, port=8080)