from itertools import islice
from collections import deque, Counter

import pytest


def batched(s, start, step):

    for curr_start in range(start, len(s) - step + 1, step):
        yield curr_start, s[curr_start:curr_start+step]


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        substring_inds = []

        target_word_count = Counter(words)

        for i_start in range(len(words[0])):
            current_word_iter = batched(s,i_start,len(words[0]))
            words_window = deque()

            for _, word in islice(current_word_iter, len(words)):
                words_window.append(word)

            if Counter(words_window) == target_word_count:
                substring_inds.append(i_start)

            for i_word, word in current_word_iter:
                words_window.popleft()
                words_window.append(word)
                if Counter(words_window) == target_word_count:
                    substring_inds.append(i_word - len(words[0])*(len(words) - 1))

        return substring_inds


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
