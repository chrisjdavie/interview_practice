from unittest import TestCase


class PhoneBook:

    def __init__(self):

        self._children = []
        self._is_end_of_word = False

    def _build(self):
        if self._children:
            return
        for _ in range(26):
            self._children.append(PhoneBook())

    def insert_entry(self, entry):
        if not entry:
            self._is_end_of_word = True
            return
        self._build()
        self._children[ord(entry[0]) - 97].insert_entry(entry[1:])
        return

    def all_suggestions(self):
        all_suggestions = []
        for i, child in enumerate(self._children):
            current_char = chr(i+97)
            for sug in child.all_suggestions():
                all_suggestions.append(current_char + sug)
        if self._is_end_of_word:
            all_suggestions.append("")
        return all_suggestions

    def suggestions(self, query):
        if not query:
            return self.all_suggestions()
        if not self._children:
            return []

        current_char = query[0]
        child_suggestions = self._children[
            ord(current_char) - 97].suggestions(query[1:])
        return [current_char + sug for sug in child_suggestions]


if __name__ == "__main__":

    num_tests = int(input())
    for _ in range(num_tests):
        input()
        entries = input().split()
        query = input()

        phone_book = PhoneBook()
        for entry in entries:
            phone_book.insert_entry(entry)

        for i in range(len(query)):
            sub_query = query[:i+1]
            suggestions = phone_book.suggestions(sub_query)
            if suggestions:
                print(" ".join(sorted(suggestions)))
            else:
                print(0)


class TestPhoneBook(TestCase):

    def test_suggestions_one(self):

        entries = ["geeikistest"]

        phone_book = PhoneBook()

        for entry in entries:
            phone_book.insert_entry(entry)

        query = ""

        expected_suggestions = entries

        self.assertEqual(
            expected_suggestions, phone_book.suggestions(query))

    def setUp(self):

        self.entries = ["geeikistest", "geeksforgeeks", "geeksfortest"]

        self.phone_book = PhoneBook()

        for entry in self.entries:
            self.phone_book.insert_entry(entry)

    def test_suggestions_many(self):

        query = ""

        expected_suggestions = self.entries

        self.assertEqual(
            expected_suggestions, self.phone_book.suggestions(query))

    def test_suggestions_pref_many(self):

        query = "gee"

        expected_suggestions = self.entries

        self.assertEqual(
            expected_suggestions, self.phone_book.suggestions(query))

    def test_suggestions_pref_one(self):

        query = "geei"

        expected_suggestions = ["geeikistest"]

        self.assertEqual(
            expected_suggestions, self.phone_book.suggestions(query))

    def test_suggestions_pref_none(self):

        query = "geeip"

        expected_suggestions = []

        self.assertEqual(
            expected_suggestions, self.phone_book.suggestions(query))

    def test_suggestions_pref_none_2(self):

        query = "geeips"

        expected_suggestions = []

        self.assertEqual(
            expected_suggestions, self.phone_book.suggestions(query))

    def test_lexiographical_order(self):

        entries = [
            "saneadeb", "sanadcbabdcb", "sanbcaccd", "sanbded", "sanccdcdbd", "sancdcbeceaa", "sanadcadeee",
            "saneabddabcdea", "sanbaeecdecab", "sanbbeeaaa", "saneab", "sanaccccbcbedce", "sanbabdbaecba", "sancaa"]

        phone_book = PhoneBook()

        for entry in entries:
            phone_book.insert_entry(entry)

        query = "s"

        expected_suggestions = [
            "sanaccccbcbedce", "sanadcadeee", "sanadcbabdcb", "sanbabdbaecba", "sanbaeecdecab", "sanbbeeaaa",
            "sanbcaccd", "sanbded", "sancaa", "sanccdcdbd", "sancdcbeceaa", "saneab", "saneabddabcdea", "saneadeb"]

        results = phone_book.suggestions(query)
        self.assertEqual(expected_suggestions, sorted(results))

    def test_query_in_entries(self):

        entries = ["d"]
        query = "d"

        expected_suggestions = ["d"]

        phone_book = PhoneBook()

        for entry in entries:
            phone_book.insert_entry(entry)

        results = phone_book.suggestions(query)
        self.assertEqual(expected_suggestions, sorted(results))


'''
2
3
geeikistest geeksforgeeks geeksfortest
geeips
14
saneadeb sanadcbabdcb sanbcaccd sanbded sanccdcdbd sancdcbeceaa sanadcadeee saneabddabcdea sanbaeecdecab sanbbeeaaa saneab sanaccccbcbedce sanbabdbaecba sancaa
sandde
'''
