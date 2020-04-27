"""
3rd try - just making sure I've got all the aspects of this in my head
    - I can do it faster without bugs
    - I can write the clean code first time round
    - I understand the details

Retro - I did get most of these. I think the code is a tad better.
It revieled that I still have slight issues automaticallly figuring out index
ordering in grids. But this isn't a new issue.

https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

The not-too Pythonic "class Solution" is a leetcode thing
"""
from typing import List, Set
from unittest import TestCase

from parameterized import parameterized


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        row_max = len(board)
        col_max = len(board[0])

        def dfs(char_num: int, row_num: int, col_num: int, visited: Set[int]
                ) -> bool:
            if char_num >= len(word):
                return True

            coords = (row_num, col_num)

            if (coords in visited
                    or col_num >= col_max
                    or col_num < 0
                    or row_num >= row_max
                    or row_num < 0
                    or word[char_num] != board[row_num][col_num]):
                return False

            visited.add(coords)
            valid = (
                dfs(char_num + 1, row_num, col_num + 1, visited)
                or dfs(char_num + 1, row_num, col_num - 1, visited)
                or dfs(char_num + 1, row_num + 1, col_num, visited)
                or dfs(char_num + 1, row_num - 1, col_num, visited))
            visited.remove(coords)
            return valid

        visited = set()

        for row_num in range(row_max):
            for col_num in range(col_max):
                if dfs(0, row_num, col_num, visited):
                    return True
        return False


class TestExist(TestCase):

    def setUp(self):

        self._solution = Solution()

    @parameterized.expand([
        ("A", True),
        ("B", False)
    ])
    def test_single_character(self, word, expected_result):

        board = [
            ["A"]
        ]

        self.assertEqual(self._solution.exist(board, word), expected_result)

    def test_one_row_single_charater(self):

        word = "A"

        board = [
            ["B", "A"]
        ]

        self.assertEqual(self._solution.exist(board, word), True)

    def test_multi_row_single_charater(self):

        word = "A"

        board = [
            ["B"],
            ["A"]
        ]

        self.assertEqual(self._solution.exist(board, word), True)

    @parameterized.expand([
        ("AB", True),
        ("AC", True),
        ("BA", True),
        ("CA", True),
        ("AD", False)
    ])
    def test_two_charaters(self, word, expected_result):

        board = [
            ["A", "B"],
            ["C", "D"]
        ]

        self.assertEqual(self._solution.exist(board, word), expected_result)

    @parameterized.expand([
        ("AG", False),
        ("AC", False)
    ])
    def test_doesnt_loop(self, word, expected_result):

        board = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]

        self.assertEqual(self._solution.exist(board, word), expected_result)

    def test_doesnt_repeat(self):

        word = "ABA"

        board = [
            ["B", "A"]
        ]

        self.assertEqual(self._solution.exist(board, word), False)

    def test_can_revisit(self):

        word = "ABEFCB"

        board = [
            ["A", "B", "C"],
            ["B", "E", "F"]
        ]

        self.assertEqual(self._solution.exist(board, word), True)

    @parameterized.expand([
        ("ABCCED", True),
        ("SEE", True),
        ("ABCB", False)
    ])
    def test_examples(self, word, expected_result):

        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]

        self.assertEqual(self._solution.exist(board, word), expected_result)
