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
    frame = level
    count_array = get_count_array(_board, frame)
    for i in range(0, len(count_array)):
        for j in range(0, frame):
            print(get_row(_board[i], count_array[i]))



board = [
    ["A", "B", "C", "D"],
    ["S", "F", "E", "S"],
    ["A", "D", "E", "E"],
]

# 2차원 배열을 프린트 한다.
# 2차원 배열을 주변을 공백으로 채우고 출력한다.
# 배열의 값을 강조색으로 바꾼다.
# 배열의 특정 위치 주변의 값을 가져오고 비교하는 기능을 만든다.
# 미로를 탐색하는 코드를 만든다.

# print_board(board)


# 일단, 반복 출력으로 수정한다. 같은 문자열 출력하게 한다

print("-0-")
print_board_extend(board, 0)
print("-1-")
print_board_extend(board, 1)
print("-2-")
print_board_extend(board, 2)
print("-3-")
print_board_extend(board, 3)