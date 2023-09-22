"""
I'm getting there :) 

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
from typing import Iterator
matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"]
]

def gen_indices(I_max: int, J_max: int) -> Iterator[tuple[int, int]]:

    for j_row in range(J_max):
        for delta in range(j_row + 1):
            yield (0 + delta, j_row - delta)
    
    for i_col in range(1, I_max):
        for delta in range(J_max):
            i_col_p = i_col + delta
            if i_col_p >= I_max:
                break
            yield (i_col_p, J_max - 1 - delta)


def print_diags(matrix: list[list[str]]) -> None:

    j_row_prev: int = 0
    for i_col, j_row in gen_indices(len(matrix), len(matrix[0])):
        if j_row > j_row_prev:
            print()
        print(matrix[i_col][j_row], end=" ")
        j_row_prev: int = j_row

    print()


print_diags(matrix)
