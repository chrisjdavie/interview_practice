"""
So turns out I have a real blank spot around indices manipulation like this.

Well, that and live interviewing, probably been practicing TDD-like too much.

Of course, I can do it, no doubt, but live, nah

------------------------

Given a matrix

[
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"]
]

Print the inverse diags as bellow

a
b d
c e g
f h j
i k m
n l
o

Do not access the matrix any 
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

    for i_row_s in range(1, len(matrix) - len(matrix[0])):
        for i_row_p, j_col in enumerate(range(len(matrix[0])-1, -1, -1)):
            print(matrix[i_row_s + i_row_p][j_col], end=" ")
        print()

    for i_row_p in range(len(matrix[0])):
        i_row_s = len(matrix) - len(matrix[0]) + i_row_p
        for i_row_p, j_col in enumerate(range(len(matrix[0])-1, i_row_p-1, -1)):
            print(matrix[i_row_s + i_row_p][j_col], end=" ")
        print()


print_diags(matrix)
