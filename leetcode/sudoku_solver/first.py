"""
https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.
"""
from copy import deepcopy
from collections import defaultdict

import pytest


class Solution:

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_nums_map: dict[int,set[str]] = defaultdict(lambda: set(str(i) for i in range(1,10)))
        col_nums_map: dict[int,set[str]] = defaultdict(lambda: set(str(i) for i in range(1,10)))
        square_nums_map: dict[tuple[int,int],set[str]] = defaultdict(lambda: set(str(i) for i in range(1,10)))
        # available_nums_map: dict[tuple[int,int], set[str]] = defaultdict(lambda _: set(str(i) for i in range(1,10)))

        coords = set((i, j) for i in range(len(board)) for j in range(len(board[0])))
        unfilled_nums: set[tuple[int, int]] = set()
        for i_row, j_col in coords:
            if (letter := board[i_row][j_col]) != ".":
                row_nums_map[i_row].remove(letter)
                col_nums_map[j_col].remove(letter)
                square_nums_map[(i_row//3,j_col//3)].remove(letter)
            else:
                unfilled_nums.add((i_row, j_col))

        prev_num_coords: int = len(unfilled_nums) + 1

        while len(unfilled_nums) < prev_num_coords:
            unfilled_nums_again: set[tuple[int, int]] = set()
            for i_row, j_col in unfilled_nums:

                row_nums = row_nums_map[i_row]
                col_nums = col_nums_map[j_col]
                square_nums = square_nums_map[(i_row//3,j_col//3)]

                candidate = row_nums.intersection(col_nums).intersection(square_nums)

                if len(candidate) == 1:
                    letter = candidate.pop()
                    board[i_row][j_col] = letter

                letter = board[i_row][j_col]

                if letter != ".":
                    row_nums_map[i_row].discard(letter)
                    col_nums_map[j_col].discard(letter)
                    square_nums_map[(i_row//3,j_col//3)].discard(letter)                
                else:
                    unfilled_nums_again.add((i_row, j_col))

            prev_num_coords: int = len(unfilled_nums)
            unfilled_nums = unfilled_nums_again


@pytest.mark.parametrize(
    "cords_to_blank",
    (
        [(0,8),(1,8)], # fills rows
        [(0,8),(0,0)], # fills cols
        [(0,8),(0,0),(8,0)], # fills squares
        [(0,8),(0,7),(1,8)], # keeps going
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


def test_from_board(): # using intersection of sets

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

    test_board = [
        ["5",".","4","6","7","8","9","1","."],
        ["6","7",".",".","9","5",".","4","8"],
        [".","9","8","3","4",".","5","6","7"],
        ["8","5","9","7","6",".","4",".","."],
        ["4",".","6","8","5","3","7","9","."],
        ["7",".",".","9",".","4","8","5","6"],
        ["9","6",".","5",".","7",".","8","4"],
        [".","8","7","4",".","9","6",".","5"],
        [".","4","5",".","8","6","1","7","9"]
    ]

    Solution().solveSudoku(test_board)

    assert valid_board == test_board


# def test_leetcode():

#     board = [
#         ["5","3",".",".","7",".",".",".","."],
#         ["6",".",".","1","9","5",".",".","."],
#         [".","9","8",".",".",".",".","6","."],
#         ["8",".",".",".","6",".",".",".","3"],
#         ["4",".",".","8",".","3",".",".","1"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".","6",".",".",".",".","2","8","."],
#         [".",".",".","4","1","9",".",".","5"],
#         [".",".",".",".","8",".",".","7","9"]
#     ]

#     Solution().solveSudoku(board)

#     assert board == [
#         ["5","3","4","6","7","8","9","1","2"],
#         ["6","7","2","1","9","5","3","4","8"],
#         ["1","9","8","3","4","2","5","6","7"],
#         ["8","5","9","7","6","1","4","2","3"],
#         ["4","2","6","8","5","3","7","9","1"],
#         ["7","1","3","9","2","4","8","5","6"],
#         ["9","6","1","5","3","7","2","8","4"],
#         ["2","8","7","4","1","9","6","3","5"],
#         ["3","4","5","2","8","6","1","7","9"]
#     ]
