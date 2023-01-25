"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

    For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.

Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

https://leetcode.com/problems/substring-with-concatenation-of-all-words/
-----------------------------------
A solution for this would be a Trie + a counter, so I'll give that a go when I'm next doing this
"""
from collections import Counter

import pytest


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        len_word = len(words[0])
        words_count = Counter(words)
        i_start_substring = []

        for i in range(len(s) - len(words)*len(words[0]) + 1):
            found_words_count = Counter()
            for j in range(len(words)):
                if found_words_count[(this_word := s[(i_this_word := i + j*len_word): i_this_word + len_word])] < words_count[this_word]: # this is not helpful and I wouldn't do this IRL
                    found_words_count[this_word] += 1
                else:
                    break
            else:
                i_start_substring.append(i)

        return i_start_substring

@pytest.mark.parametrize(
    "input_string,words,expected_indicies",
    (
        ("barfoothefoobarman", ["foo","bar"], [0,9]),
        ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
        ("barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12]),
        ("wordgoodgoodgoodbestword", ["word","good","best","good"], [8])
    )
)
def test_leetcode(input_string, words, expected_indicies):
    assert Solution().findSubstring(input_string, words) == expected_indicies

"""
Can convert the following into a test using itertools.permutations and then some magic

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
"""
