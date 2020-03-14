from unittest import TestCase


class TrieNode:

    def __init__(self):

        self.children = []
        self.is_end_of_word = False

    def build(self):
        if not self.children:
            self.children = [TrieNode() for _ in range(26)]

    def insert_word(self, word):
        if not word:
            self.is_end_of_word = True
            return

        self.build()
        self.children[ord(word[0])-97].insert_word(word[1:])
        return

    def has_word(self, word):
        if not word:
            return self.is_end_of_word
        if not self.children:
            return False
        return self.children[ord(word[0]) - 97].has_word(word[1:])


class TestTrieNode(TestCase):

    def test_found(self):

        words = [
            "the", "a", "there", "answer", "any", "by", "bye",
            "their", "the"]

        trie = TrieNode()

        for word in words:
            trie.insert_word(word)

        self.assertTrue(trie.has_word("any"))

    def test_not_found_0(self):

        words = [
            "the", "a", "there", "answer", "any", "by", "bye",
            "their", "the"]

        trie = TrieNode()

        for word in words:
            trie.insert_word(word)

        self.assertFalse(trie.has_word("bob"))

    def test_not_found_1(self):

        words = [
            "cey" "vpj" "hvf"]

        trie = TrieNode()

        for word in words:
            trie.insert_word(word)

        self.assertFalse(trie.has_word("gxp"))


if __name__ == "__main__":

    num_tests = int(input())
    for _ in range(num_tests):
        trie = TrieNode()

        input()
        all_words = input().split()
        for word in all_words:
            trie.insert_word(word)

        test_word = input()
        print(int(trie.has_word(test_word)))
