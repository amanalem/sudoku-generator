import random

def make_cell():
    cell = {
        "options": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "answer": None
    }
    cell["numOfOptions"] = lambda: len(cell['options'])
    return cell

def get_row(board, row):
    return board[row]

def get_column(board, column):
    return [board[row][column] for row in range(9)]

def get_box(board, row, column):
    box_row = (row // 3) * 3
    box_column = (column // 3) * 3
    return [board[box_row + r][box_column + c] for r in range(3) for c in range(3)]

def propagate(board, row, column, answer):
    related_cells = get_row(board, row) + get_column(board, column) + get_box(board, row, column)

    for cell in related_cells:
        if answer in cell["options"]:
            cell["options"].remove(answer)

def count_solved(board):
    count = 0
    for row in range(9):
        for column in range(9):
            if board[row][column]["answer"] is not None:
                count += 1
    return count

def find_naked_singles(board):
    for row in range(9):
        for column in range(9):
            cell = board[row][column]
            if cell["numOfOptions"]() == 1 and cell["answer"] is None:
                answer = cell["options"][0]
                board[row][column]["answer"] = answer
                propagate(board, row, column, answer)


def find_hidden_singles(board):
    # First we look for hidden row singles
    for row in range(9):
        cells = get_row(board, row)
        for number in range(1, 10):
            possible_cells = [i for i, cell in enumerate(cells) if number in cell["options"] and cell["answer"] is None]
            if len(possible_cells) == 1:
                column = possible_cells[0]
                board[row][column]["answer"] = number
                board[row][column]["options"] = [number]
                propagate(board, row, column, number)
    # Second we look for hidden column singles
    for column in range(9):
        cells = get_column(board, column)
        for number in range(1, 10):
            possible_cells = [i for i, cell in enumerate(cells) if number in cell["options"] and cell["answer"] is None]
            if len(possible_cells) == 1:
                row = possible_cells[0]
                board[row][column]["answer"] = number
                board[row][column]["options"] = [number]
                propagate(board, row, column, number)
    # Third we look for hidden box singles
    for box_row in range(3):
        for box_column in range(3):
            cells = get_box(board, box_row * 3, box_column * 3)
            for number in range(1, 10):
                possible_cells = [(i, cell) for i, cell in enumerate(cells) if number in cell["options"] and cell["answer"] is None]
                if len(possible_cells) == 1:
                    index = possible_cells[0][0]
                    row = box_row * 3 + index // 3
                    column = box_column * 3 + index % 3
                    board[row][column]["answer"] = number
                    board[row][column]["options"] = [number]
                    propagate(board, row, column, number)

def find_all_singles(board):
    while True:
        before = count_solved(board)
        find_naked_singles(board)
        find_hidden_singles(board)
        after = count_solved(board)
        if before == after:
            break

def find_best_cell(board):
    best = None
    best_count = 10

    for row in range(9):
        for column in range(9):
            cell = board[row][column]
            if cell["answer"] is None and cell["numOfOptions"]() < best_count:
                best = (row, column)
                best_count = cell["numOfOptions"]()
    return best

def make_guess(board, row, column, answer):
    board[row][column]["answer"] = answer
    board[row][column]["options"] = [answer]
    propagate(board, row, column, answer)
    return answer

def has_conflict(board):
    for row in range(9):
        for column in range(9):
            cell = board[row][column]
            if cell["answer"] is None and cell["numOfOptions"]() == 1:
                return True
    return False

def save_state(board, states):
    state = [[{"options": cell["options"][:], "answer": cell["answer"]} for cell in row] for row in board]
    states.append(state)
    return states

def restore_state(board, states):
    state = states.pop()
    for row in range(9):
        for column in range(9):
            board[row][column]["options"] = state[row][column]["options"][:]
            board[row][column]["answer"] = state[row][column]["answer"]
            

def backtrack(board, states):
    find_all_singles(board)
    if has_conflict(board):
        return False
    if count_solved(board) == 81:
        return True
    cell = find_best_cell(board)
    row, column = cell
    options = board[row][column]["options"][:]
    random.shuffle(options)
    for option in options:
        save_state(board)
        make_guess(board, row, column, option)
        if backtrack(board, states):
            return True
        restore_state(board, states)
    return False

        

def generate_sudoku():

    board_states = []
    board = [[make_cell() for _ in range(9)] for _ in range(9)]
    