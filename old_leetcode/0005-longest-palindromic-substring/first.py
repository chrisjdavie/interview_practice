from functools import lru_cache
from typing import Dict, Tuple, Set
from unittest import TestCase
import sys

from parameterized import parameterized


def palindrome_cache(method):

    solution_cache: Dict[str, str] = {}

    def cached_method(obj, s: str) -> str:
        if s in solution_cache:
            return solution_cache[s]
        solution_cache[s] = method(obj, s)
        return solution_cache[s]
        
    return cached_method


class Solution:

    def __init__(self):
        self._cache: Dict[str, str] = {}

    def is_a_palindrome(self, candidate: str, left_offset: int, right_offset: int) -> bool:
        for ind in range(len(candidate) - left_offset - right_offset + 1):
            print(candidate[left_offset + ind], candidate[- right_offset - ind], right_offset, ind)
            if candidate[left_offset + ind] != candidate[- right_offset - ind]:
                return False
        return True


    def longest_palindrome(self, candidate: str, left_offset: int, right_offset: int) -> Tuple[int, int]:

        solution: Tuple[int, int]

        if self.is_a_palindrome(candidate, left_offset, right_offset):
            solution = (left_offset, right_offset)
        else:
            lh_palindrome = self.longest_palindrome(candidate, left_ind + 1, right_ind)
            rh_palindrome = self.longestPalindrome(candidate, left_ind, right_ind - 1)
            if len(lh_palindrome) > len(rh_palindrome):
                solution = lh_palindrome
            else:
                solution = rh_palindrome

        # self._cache[s] = solution        
        return solution            

    def longestPalindrome(self, s: str) -> str:
        # if s in self._cache:
        #    return self._cache[s]

        solution: str = ""

        if self.is_a_palindrome(s):
            solution = s
        else:
            lh_palindrome = self.longestPalindrome(s[:-1])
            rh_palindrome = self.longestPalindrome(s[1:])
            if len(lh_palindrome) > len(rh_palindrome):
                solution = lh_palindrome
            else:
                solution = rh_palindrome

        # self._cache[s] = solution        
        return solution


if __name__ == "__main__":
    input_string = "zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"
    print(len(input_string))
    
    import timeit
    print(timeit.timeit(lambda: Solution().longestPalindrome(input_string), number=1))

        
class TestSolution(TestCase):

    def setUp(self):
        self._solution = Solution()

    @parameterized.expand([
        ("babad", set(["bab", "aba"])),
        ("cbbd", set(["bb"])),
        ("a", set(["a"])),
        ("ac", set(["a", "c"]))
    ])
    def test_longestPalindrome_examples(self, input_string: str, valid_outputs: Set[str]):
        
        self.assertIn(
            self._solution.longestPalindrome(input_string),
            valid_outputs
        )

    @parameterized.expand([
        ("a", True),
        ("ab", False),
        ("aa", True),
        ("aba", True)
    ])
    def test_is_a_palindrome(self, candidate: str, result: bool):

        self.assertEqual(
            self._solution.is_a_palindrome(candidate, 0, -1),
            result
        )

    def test_is_a_palindrome_offset(self):
        candidate = "abdbc"
        left_offset = 1
        right_offset = -2

        self.assertEqual(
            self._solution.is_a_palindrome(candidate, left_offset, right_offset),
            True
        )        
