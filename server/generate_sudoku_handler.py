import random

def make_cell():
    cell = {
        "options": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "answer": None
    }
    cell["numOfOptions"] = lambda: len(cell['options'])
    return cell

board = [[make_cell() for _ in range(9)] for _ in range(9)]

def get_row(board, row):
    return board[row]

def get_column(board, column):
    return [board[row][column] for row in range(9)]

def get_box(board, row, column):
    box_row = (row // 3) * 3
    box_column = (column // 3) * 3
    return [board[box_row + r][box_column + c] for r in range(3) for c in range(3)]

def propogate(board, row, column, answer):
    related_cells = get_row(board, row) + get_column(board, column) + get_box(board, row, column)

    for cell in related_cells:
        if answer in cell["options"]:
            cell["options"].remove(answer)

def find_naked_singles(board):
    while True:
        option_found = False
        for row in range(9):
            for column in range(9):
                cell = board[row][column]
                if cell["numOfOptions"]() == 1 and cell["answer"] is None:
                    answer = cell["options"][0]
                    board[row][column]["answer"] = answer
                    propogate(board, row, column, answer)
                    option_found = True
        if not option_found:
            break

def find_hidden_singles(board):
    while True:
        repeat = False
        # First we look for hidden row singles
        for row in range(9):
            cells = get_row(board, row)
            for number in range(1, 10):
                possible_cells = [i for i, cell in enumerate(cells) if number in cell["options"] and cell["answer"] is None]
                if len(possible_cells) == 1:
                    column = possible_cells[0]
                    board[row][column]["answer"] = number
                    board[row][column]["options"] = [number]
                    propogate(board, row, column, number)
                    repeat = True
        # Second we look for hidden column singles
        for column in range(9):
            cells = get_column(board, column)
            for number in range(1, 10):
                possible_cells = [i for i, cell in enumerate(cells) if number in cell["options"] and cell["answer"] is None]
                if len(possible_cells) == 1:
                    row = possible_cells[0]
                    board[row][column]["answer"] = number
                    board[row][column]["options"] = [number]
                    propogate(board, row, column, number)
                    repeat = True
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
                        propogate(board, row, column, number)
                        repeat = True
        if not repeat:
            break

def find_best_cell(board):
    best = None
    best_count = 10

    for row in range(9):
        for column in range(9):
            cell = board[row][column]
            if cell["answer"] == None and cell["numOfOptions"] < best_count:
                best = (row, column)
                best_count = cell["numOfOptions"]

    return best
