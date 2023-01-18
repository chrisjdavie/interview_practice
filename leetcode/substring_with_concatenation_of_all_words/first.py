"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

    For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.

Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

https://leetcode.com/problems/substring-with-concatenation-of-all-words/
-----------------------------------
A solution for this would be a Trie + a counter, so I'll give that a go when I'm next doing this
"""
import pytest


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        return [-1]


@pytest.mark.parametrize(
    "input_string,words,expected_indicies",
    (
        ("barfoothefoobarman", ["foo","bar"], [0,9]),
        ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
        ("barfoofoobarthefoobarman", ["bar","foo","the"])
    )
)
def test_leetcode(input_string, words, expected_indicies):
    assert Solution().findSubstring(input_string, words) == expected_indicies

"""
Can convert the following into a test using itertools.permutations and then some magic

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
"""
