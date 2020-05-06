# Implement your function below.
def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for bomb in bombs:
        row_bomb = bomb[0]
        column_bomb = bomb[1]
        field[row_bomb][column_bomb] = -1
        for i in range(row_bomb - 1, row_bomb + 2):
            for j in range(column_bomb - 1, column_bomb + 2):
                if 0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1:
                    field[i][j] += 1
    return field


# Implement your function below.
def click(field, num_rows, num_cols, given_i, given_j):
    return field

# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n'.join(list_rows) + ']\n'


# NOTE: The following input values will be used for testing your solution.
# mine_sweeper([[0, 2], [2, 0]], 3, 3) should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]
print(to_string(mine_sweeper([[0, 2], [2, 0]], 3, 3)))

# mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4) should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]
print(to_string(mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)))

# mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5) should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]
print(to_string(mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5)))

# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

print("click")

print(to_string(click(field1, 3, 5, 2, 2)))
# should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

print(to_string(click(field1, 3, 5, 1, 4)))
# should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

print(to_string(click(field2, 4, 4, 0, 1)))
# should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

print(to_string(click(field2, 4, 4, 1, 3)))
# should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]