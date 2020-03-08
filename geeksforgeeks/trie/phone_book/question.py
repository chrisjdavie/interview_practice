from unittest import TestCase


class PhoneBook:

    def insert_entry(self, entry):
        pass

    def suggestions(self, query):
        return []


class TestPhoneBook(TestCase):

    def test_autocomplete(self):

        entries = ["geeikistest" "geeksforgeeks" "geeksfortest"]

        phone_book = PhoneBook()

        for entry in entries:
            phone_book.insert_entry(entry)

        query = "gee"

        expected_suggestions = [
            "geeikistest", "geeksforgeeks", "geeksfortest"]

        self.assertEqual(
            expected_suggestions, phone_book.suggestions(query))

        query = "geei"

        expected_suggestions = ["geeikistest"]

        self.assertEqual(
            expected_suggestions, phone_book.suggestions(query))

        query = "geeip"

        expected_suggestions = []

        self.assertEqual(
            expected_suggestions, phone_book.suggestions(query))
