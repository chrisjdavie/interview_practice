# Trie practice

# https://www.hackerrank.com/challenges/contacts/problem
from typing import List
from unittest import TestCase

from parameterized import parameterized


class TrieNode:

    def __init__(self):

        self.children = {}
        self.end_of_word = False
        self.words_in_subtree = 0

    def add(self, word: str):
        self.words_in_subtree += 1
        current_node = self
        for this_chr in word:
            if not current_node.children.get(this_chr):
                current_node.children[this_chr] = TrieNode()
            current_node = current_node.children[this_chr]
            current_node.words_in_subtree += 1
        current_node.end_of_word = True

    def find_partial(self, query: str, i: int = 0) -> List[str]:
        all_matches = []
        if i >= len(query):
            if self.end_of_word:
                all_matches.append("")
            for child_chr, child in self.children.items():
                child_matches = child.find_partial(query, i+1)
                for match in child_matches:
                    all_matches.append(child_chr+match)
        elif self.children:
            child_chr = query[i]
            child = self.children.get(child_chr)
            if child:
                child_matches = self.children[child_chr].find_partial(
                    query, i+1)
                for match in child_matches:
                    all_matches.append(child_chr+match)
        return all_matches

    def match_count(self, query: str, i: int = 0) -> List[str]:
        matches = 0
        if i >= len(query):
            return self.words_in_subtree
        elif self.children:
            child_chr = query[i]
            child = self.children.get(child_chr)
            if child:
                matches += child.match_count(query, i+1)
        return matches


if __name__ == "__main__":
    contacts = TrieNode()
    for _ in range(int(input())):
        command, word = input().split()
        if command == "add":
            contacts.add(word)
        if command == "find":
            print(contacts.match_count(word))


class TestContacts(TestCase):

    @parameterized.expand([
        (["foo"], "bar", []),
        (["foo"], "f", ["foo"]),
        (["back", "berry"], "b", ["back", "berry"]),
        (["red", "roll"], "re", ["red"]),
        (["aca"], "ac", ["aca"]),
        (["hack", "hackerrank"], "hac", ["hack", "hackerrank"]),
        (["hack", "hackerrank"], "hak", []),
    ])
    def test(
            self, words_to_add: List[str], query: str,
            expected_results: List[str]):

        contacts = TrieNode()

        for word in words_to_add:
            contacts.add(word)

        results = contacts.find_partial(query)

        for word in expected_results:
            self.assertIn(word, results)
        self.assertEqual(len(results), len(expected_results))
