# Trie practice

# https://www.hackerrank.com/challenges/contacts/problem
from typing import List
from unittest import TestCase

from parameterized import parameterized


class Contacts:

    def add(self, name: str):
        pass

    def find_partial(self, name: str) -> List[str]:
        return []


class TestContacts(TestCase):

    def _build_and_check(
            self, words_to_add: List[str], query: str, expected_results: List[str]):

        contacts = Contacts()

        for word in words_to_add:
            contacts.add(word)

        results = contacts.find_partial("query")

        for word in expected_results:
            self.assertIn(word, results)
        self.assertEqual(len(results), len(expected_results))

    @parameterized.expand([
        (["foo"], "bar", []),
        (["foo"], "f", ["foo"]),
        (["back", "berry"], "b", ["back", "berry"]),
        (["red", "roll"], "re", ["red"]),
        (["hack", "hackerrank"], "hac", ["hack", "hackerrank"]),
        (["hack", "hackerrank"], "hak", []),
    ])
    def test(
            self, words_to_add: List[str], query: str,
            expected_results: List[str]):

        contacts = Contacts()

        for word in words_to_add:
            contacts.add(word)

        results = contacts.find_partial(query)

        for word in expected_results:
            self.assertIn(word, results)
        self.assertEqual(len(results), len(expected_results))
