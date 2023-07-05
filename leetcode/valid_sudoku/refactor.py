"""
Refactor, inspired by another solution. The inspiration isn't super strong, 

https://leetcode.com/problems/valid-sudoku/description/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
"""
from collections import defaultdict

import pytest


class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:

        vals_in_cols_map = defaultdict(set)
        vals_in_rows_maps = defaultdict(set)
        vals_in_square_map = defaultdict(set)

        for i_row, row in enumerate(board):
            for j_col, letter in enumerate(row):
                if letter != ".":
                    """
                    could do something like

                    if letter in vals_in_rows_maps[i_row]: return False
                    else: letter in vals_in_rows_maps[i_row].add(letter)

                    For each, but I prefer the below
                    """
                    vals_in_row = vals_in_rows_maps[i_row]
                    vals_in_col = vals_in_cols_map[j_col]
                    vals_in_square = vals_in_square_map[(i_row//3, j_col//3)]

                    if letter in vals_in_row or letter in vals_in_col or letter in vals_in_square:
                        return False

                    vals_in_row.add(letter)
                    vals_in_col.add(letter)
                    vals_in_square.add(letter)

        return True


@pytest.mark.parametrize(
    "i_j_char,is_valid",
    (
        ([], True),
        ([(0,0,"1"),(0,4,"1")], False), # test 1st row fails
        ([(0,0,"1"),(0,4,"2")], True), # test 1st row passes
        ([(1,0,"1"),(1,4,"1")], False), # test 2nd row fails
        ([(0,1,"1"),(4,1,"1")], False), # test column fails
        ([(0,0,"3"),(2,2,"3")], False), # test square fails
    )
)
def test_violations(i_j_char, is_valid):

    board = [["."]*9 for _ in range(9)]

    for i, j, char in i_j_char:
        board[i][j] = char
    assert Solution().isValidSudoku(board) == is_valid


@pytest.mark.parametrize(
    "board,is_valid",
    (
        (
            [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]],
            True
        ),
        (
            [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]],
            False
        )
    )
)
def test_leetcode(board, is_valid):

    assert Solution().isValidSudoku(board) == is_valid
