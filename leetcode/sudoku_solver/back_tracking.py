"""
Using backtracking as a real solution, from the ground up

https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.
"""
from copy import deepcopy

import pytest


class Solution:

    def solveSudoku(self, board: list[list[str]]) -> None:

        edge_length = 9

        def solve(i_row: int, j_column: int) -> bool:
            if j_column == edge_length:
                return solve(i_row+1, 0)
            if i_row == edge_length:
                return True

            def _isValid(candidate: int) -> bool:
                # check row
                for j_check in range(edge_length):
                    if board[i_row][j_check] == candidate:
                        return False

                # # check column
                for i_check in range(edge_length):
                    if board[i_check][j_column] == candidate:
                        return False

                # check blocks
                for i_check in range(edge_length//3):
                    for j_check in range(edge_length//3):
                        if board[i_row//3*3+i_check][j_column//3*3+j_check] == candidate:
                            return False

                return True

            if board[i_row][j_column] == ".":
                for candidate in range(1, edge_length+1):
                    if _isValid(str(candidate)):
                        board[i_row][j_column] = str(candidate)
                        if solve(i_row, j_column+1):
                            return True
                        board[i_row][j_column] = "."
                # no valid candidates
                return False
            else:
                return solve(i_row, j_column+1)

        solve(0,0)


@pytest.mark.parametrize(
    "cords_to_blank",
    (
        [(0,7),], # substitution blanks out 1 on first row
        [(0,7),(7,4)], # column check - blanks out 1 on first and 7th row
        [(0,6),(0,7)], # row check - blanks out 9 and 1 on first row
        [(0,5),(0,7),(3,5)], # block check - blanks out 8 and 1 on first row, and 1 in the 8 column
        [(0,6),(0,7),(8,6)], # requires backtracking - blanks out 9 and 1 on first row, and 1 in the 9 column
    )
)
def test_unit(cords_to_blank):

    valid_board = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]

    test_board = deepcopy(valid_board)
    for i_row, j_col in cords_to_blank:
        test_board[i_row][j_col] = "."

    Solution().solveSudoku(test_board)

    assert valid_board == test_board


def test_leetcode():

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    Solution().solveSudoku(board)

    assert board == [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
