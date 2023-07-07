"""
As I completely failed to do this right first time, and then when I redid it, I made lots of
mistakes, I'm redoing this a couple of times to get smoother at solving recursive and
backtracking algorithms

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

        def _isValid(i_row: int, j_col: int, cand: str) -> bool:

            # check column
            for i_check in range(0, edge_length):
                if board[i_check][j_col] == cand:
                    return False

            # check row
            for j_check in range(0, edge_length):
                if board[i_row][j_check] == cand:
                    return False
            
            # check block
            for i_check in range(0, 3):
                for j_check in range(0, 3):
                    if board[i_row//3*3+i_check][j_col//3*3+j_check] == cand:
                        return False

            return True

        def solve(i_row: int, j_col: int) -> None:
            if j_col == edge_length:
                return solve(i_row+1, 0)
            if i_row == edge_length:
                return True
            if board[i_row][j_col] == ".":
                for cand_num in range(1, 10):
                    cand = str(cand_num)
                    if _isValid(i_row, j_col, cand):
                        board[i_row][j_col] = cand
                        if solve(i_row, j_col+1):
                            return True
                        board[i_row][j_col] = "."
                # No valid candidates
                return False
            else:
                return solve(i_row, j_col+1)
        
        solve(0,0)


@pytest.mark.parametrize(
    "coords_to_blank",
    (
        [(0, 7),], # subs a blank with number, first row
        [(0, 7),(7,4)], # subs a blank with number, not first row
        [(0, 6), (0, 7)], # calcs the right sub from column
        [(0, 6), (1, 6)], # calcs the right sub from row
        [(3, 3), (3, 7), (8, 3)], # calcs the right sub from block
        [(0, 6), (0, 7), (8, 6)], # introduces a contradiction, so requires backtracking
    )
)
def test_unit(coords_to_blank):

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
    for i_row, j_col in coords_to_blank:
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
