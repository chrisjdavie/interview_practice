"""
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

The not-too Pythonic "class Solution" is a leetcode thing
"""
from typing import List, Set
from unittest import TestCase

from parameterized import parameterized


class Solution:

    def _explore(
            self, board: List[List[str]], word: str, row_num: int, col_num: int,
            visited: Set[int]) -> bool:
        if not word:
            return True
        found = False

        for row_inc in (-1, 1):
            row_num_next = row_num + row_inc
            if (row_num_next < len(board)
                    and row_num_next > -1
                    and word[0] == board[row_num_next][col_num]):
                new_coords = (row_num_next, col_num)
                if new_coords not in visited:
                    visited.add(new_coords)
                    found = self._explore(
                        board, word[1:], row_num_next, col_num, visited)
                    visited.remove(new_coords)
                if found:
                    break
        if not found:
            for col_inc in (-1, 1):
                col_num_next = col_num + col_inc
                if (col_num_next < len(board[0])
                        and col_num_next > -1
                        and word[0] == board[row_num][col_num_next]):
                    new_coords = (row_num, col_num_next)
                    if new_coords not in visited:
                        visited.add(new_coords)
                        found = self._explore(
                            board, word[1:], row_num, col_num_next, visited)
                        visited.remove(new_coords)
                        if found:
                            break
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:

        for row_num, row in enumerate(board):
            for col_num, letter in enumerate(row):
                if letter == word[0]:
                    if self._explore(
                        board, word[1:], row_num, col_num, set(
                            [(row_num, col_num)])):
                        return True

        return False


class TestSolution(TestCase):

    def setUp(self):

        self.solution = Solution()

    @parameterized.expand(
        [("ABCCED", True),
         ("SEE", True),
         ("ABCB", False)]
    )
    def test_example(self, word, expected_result):

        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]

        self.assertEqual(
            self.solution.exist(board, word), expected_result
        )

    def test_breaks_both(self):

        word = "AB"

        board = [
            ["A", "B"],
            ["A", "D"]
        ]

        self.assertTrue(self.solution.exist(board, word))

    @parameterized.expand([("A", True), ("I", True), ("D", False)])
    def test_find_single_letter(self, word, expected_result):

        board = [
            ["B", "C", "E"],
            ["F", "A", "G"],
            ["H", "I", "J"]
        ]

        self.assertEqual(
            self.solution.exist(board, word), expected_result
        )

    @parameterized.expand([
        ("AF", True),
        ("IJ", True),
        ("GE", True),
        ("GC", False),
        ("FG", False),
        ("CI", False)])
    def test_find_two_letters(self, word, expected_result):

        board = [
            ["B", "C", "E"],
            ["F", "A", "G"],
            ["H", "I", "J"]
        ]

        self.assertEqual(
            self.solution.exist(board, word), expected_result
        )

    @parameterized.expand(
        [("BCE", True),
         ("BCI", False),
         ("CAH", False)])
    def test_find_three_chars(self, word, expected_result):

        board = [
            ["B", "C", "E"],
            ["F", "A", "G"],
            ["H", "I", "J"]
        ]

        self.assertEqual(
            self.solution.exist(board, word), expected_result
        )

    def test_two_starting_chars(self):

        word = "BI"

        board = [
            ["B", "C"],
            ["I", "B"]
        ]

        self.assertTrue(self.solution.exist(board, word))

    def test_cannot_use_char_twice_horz(self):

        word = "BCB"

        board = [
            ["B", "C"]
        ]

        self.assertFalse(self.solution.exist(board, word))

    def test_cannot_use_char_twice_vert(self):

        word = "BCB"

        board = [
            ["B"],
            ["C"]
        ]

        self.assertFalse(self.solution.exist(board, word))

    def test_cannot_use_char_twice_after_start_horiz(self):

        word = "BCDC"

        board = [
            ["B", "C", "D"]
        ]

        self.assertFalse(self.solution.exist(board, word))

    def test_cannot_use_char_twice_after_start_vert(self):

        word = "BCEC"

        board = [
            ["B"],
            ["C"],
            ["E"]
        ]

        self.assertFalse(self.solution.exist(board, word))
