"""
Not smooth, not yet, but better each time

a
b d
c e g
f h j
i k m
n l
o

0 0
0 1, 1 0
0 2, 1 1, 2 0
1 2, 2 1, 3 0
2 2, 3 1, 4 0
3 2, 4 1
4 2
"""
matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"]
]


def print_diags(matrix):
    for j_col in range(len(matrix[0])):
        for i_row in range(j_col + 1):
            print(matrix[i_row][j_col - i_row], end=" ")
        print()

    for i_row in range(1, len(matrix) - len(matrix[0])):
        for i_row_m, j_col in enumerate(range(len(matrix[0]) - 1, -1, -1)):
            print(matrix[i_row + i_row_m][j_col], end=" ")
        print()

    for i_row_p in range(len(matrix[0])):
        i_row_s = len(matrix) - len(matrix[0]) + i_row_p
        for i_row_pp, j_col in enumerate(range(len(matrix[0]) - 1, i_row_p - 1, -1)):
            print(matrix[i_row_s + i_row_pp][j_col], end=" ")
        print()

print_diags(matrix)
