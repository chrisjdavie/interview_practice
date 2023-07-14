"""
Probably final revisit, learnt some new stuff last time, wasn't as precise as I'd like.

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

        def _solve(i_row: int, j_col: int) -> bool:
            if j_col == edge_length:
                return _solve(i_row + 1, 0)
            if i_row == edge_length:
                return True

            def _isValid(cand: str) -> bool:

                # from column
                for i_test in range(edge_length):
                    if board[i_test][j_col] == cand:
                        return False
                    
                # from row
                for j_test in range(edge_length):
                    if board[i_row][j_test] == cand:
                        return False

                # from block
                for i_test in range(3):
                    for j_test in range(3):
                        if board[i_row//3*3 + i_test][j_col//3*3 + j_test] == cand:
                            return False

                return True

            if board[i_row][j_col] == ".":
                for cand_int in range(1, 10):
                    cand = str(cand_int)
                    if _isValid(cand):
                        board[i_row][j_col] = cand
                        if _solve(i_row, j_col+1):
                            return True
                        board[i_row][j_col] = "."

                return False

            return _solve(i_row, j_col+1)

        _solve(0, 0)


@pytest.mark.parametrize(
    "coords_to_blank",
    (
        ([(0, 5), (0, 7)]), # filled via columns
        ([(0, 5), (3, 5)]), # filled via rows
        ([(0, 2), (0, 3), (4, 2)]), # break when valid candidate found
        ([(3, 3), (8, 3), (3, 7)]), # filled via blocks
        ([(0, 6), (0, 7), (8, 6)]), # needs single backfill
        ([(0, 6), (0, 7), (8, 6), (4, 7)]), # needs two backfills
    )
)
def test(coords_to_blank):

    filled_board = [
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

    unfilled_board = deepcopy(filled_board)

    for i_row, j_col in coords_to_blank:
        unfilled_board[i_row][j_col] = "."

    Solution().solveSudoku(unfilled_board)

    assert unfilled_board == filled_board


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
