import array as arr

def print_board(_board):
    for row in _board:
        for item in row:
            print(item, end=" ")
        print()

def get_count_array(_board, level):
    return [[level] * len(_board[0]) for _ in range(len(_board))]

def get_row(array, count_array):
    buffer = ""
    for i in range(0, len(array)):
        for x in range(0, count_array[i]):
            buffer += str(array[i]) + " "
    return buffer

def print_board_extend(_board, level):
    count_array = get_count_array(_board, level)
    for i in range(0, len(count_array)):
        for j in range(0, level):
            print(get_row(_board[i], count_array[i]))

board = [
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"],
    ["M", "N", "O", "P"],
]
print("-print board-")
print_board(board)
print("-0-")
print_board_extend(board, 0)
print("-1-")
print_board_extend(board, 1)
print("-2-")
print_board_extend(board, 2)
print("-3-")
print_board_extend(board, 3)