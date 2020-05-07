import copy


# rotate 90 degrees
# Implement your function below.
# n = # rows = # columns in the given 2d array
def rotate(given_array, n):
    rotated = copy.deepcopy(given_array)
    for row_index in range(len(given_array)):
        for column_index in range(len(given_array[row_index])):
            # print(("row:" + str(row_index), "column:" + str(column_index), "value:" +
            #        str(given_array[row_index][column_index])))
            new_row_index, new_column_index = rotate_index(row_index, column_index, n)
            rotated[new_row_index][new_column_index] = given_array[row_index][column_index]
    #print()
    return rotated


def rotate_index(current_row, current_column, n):
    return current_column, n - 1 - current_row


# Implement your function below.
def click(field, num_rows, num_cols, given_i, given_j):
    import queue
    to_check = queue.Queue()
    if field[given_i][given_j] == 0:
        field[given_i][given_j] = -2
        to_check.put((given_i, given_j))
    else:
        return field
    while not to_check.empty():
        (current_i, current_j) = to_check.get()
        for i in range(current_i - 1, current_i + 2):
            for j in range(current_j - 1, current_j + 2):
                if (0 <= i < num_rows and 0 <= j < num_cols and field[i][j] == 0):
                    field[i][j] = -2
                    to_check.put((i, j))
    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
# rotate(a1, 3) should return:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
print(to_string(rotate(a1, 3)))
print()

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
# rotate(a2, 4) should return:
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]
print(to_string(rotate(a2, 4)))
print()
# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 2, 2) should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]
print(to_string(click(field1, 3, 5, 2, 2)))
print()

# click(field1, 3, 5, 1, 4) should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]
print(to_string(click(field1, 3, 5, 1, 4)))
print()

field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

# click(field2, 4, 4, 0, 1) should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]
print(to_string(click(field2, 4, 4, 0, 1)))
print()

# click(field2, 4, 4, 1, 3) should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]
print(to_string(click(field2, 4, 4, 1, 3)))
print()