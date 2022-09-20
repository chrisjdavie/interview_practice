"""
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

The not-too Pythonic "class Solution" is a leetcode thing

This is a vast improvement compared to mine
    - it has a unified validity check at the start
    - holds board as a local constant
    - clearly shows what the dfs is doing
    - is in general way easier to read
"""
from typing import List, Set
from unittest import TestCase

from parameterized import parameterized


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        row_len = len(board)
        col_len = len(board[0])

        def dfs(row_num: int, col_num: int, char_pos: int, visited: Set) -> bool:
            coords = (row_num, col_num)
            if (row_num >= row_len
                    or row_num < 0
                    or col_num >= col_len
                    or col_num < 0
                    or coords in visited
                    or board[row_num][col_num] != word[char_pos]):
                return False

            visited.add(coords)
            result = (
                char_pos == len(word) - 1
                or dfs(row_num + 1, col_num, char_pos + 1, visited)
                or dfs(row_num - 1, col_num, char_pos + 1, visited)
                or dfs(row_num, col_num + 1, char_pos + 1, visited)
                or dfs(row_num, col_num - 1, char_pos + 1, visited)
            )
            visited.remove(coords)

            return result

        for row_num in range(row_len):
            for col_num in range(col_len):
                visited = set()
                if dfs(row_num, col_num, 0, visited):
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

    def test_not_present(self):

        board = [["A", "A"],
                 ["A", "A"]]

        self.assertFalse(self.solution.exist(board, "B"))

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
