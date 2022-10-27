from typing import Optional

import pytest


class Solution():

    def isMatch(self, text: str, pattern: str) -> bool:
        
        pattern_blocks: list[str] = []
        for letter in pattern:
            if letter != "*":
                pattern_blocks.append(letter)
            else:
                pattern_blocks[-1] += "*"

        memo: list[Optional[bool]] = [[False]*(len(pattern_blocks) + 1) for _ in range(len(text) + 1)]
        memo[-1][-1] = True

        for i in range(len(text), -1, -1):
            for j in range(len(pattern_blocks)-1, -1, -1):
                char_match = len(text) > i and (
                    text[i] == pattern_blocks[j][0]
                    or "." == pattern_blocks[j][0]
                )
                if pattern_blocks[j][-1] == "*":
                    memo[i][j] = (
                        memo[i][j+1]
                        or (char_match and memo[i+1][j])
                    )
                else:
                    memo[i][j] = char_match and memo[i+1][j+1]

        return memo[0][0]


@pytest.mark.parametrize(
    "text,pattern,expected_match",
    (
        ("a", "a", True),
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aaa", False),
        ("", "b*", True),
        ("c", "b*", False),
        ("b", "b*", True),
        ("bb", "b*", True),
        ("e", ".", True),
        ("e", ".*", True),
        ("d", ".*a", False),
    )
)
def test(text, pattern, expected_match):

    assert expected_match == Solution().isMatch(text, pattern)

