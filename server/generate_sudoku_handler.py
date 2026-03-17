from random import randint, randrange, shuffle

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

def find_only_options(board):
    while True:
        option_found = False
        for row in range(9):
            for column in range(9):
                cell = board[row][column]
                if cell["numOfOptions"] == 1 and cell["answer"] == None:
                    answer = cell["options"][0]
                    board[row][column]["answer"] = answer
                    propogate(board, row, column, answer)
                    option_found = True
        if option_found == False:
            break




def find_best_cell(board):
    best = None
    best_count = 10

    for row in range(9):
        for column in range(9):
            cell = board[row][column]
            if cell["answer"] == "" and cell["numOfOptions"] < best_count:
                best = (row, column)
                best_count = cell["numOfOptions"]

    return best


