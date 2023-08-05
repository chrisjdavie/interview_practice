from collections.abc import Iterator
from itertools import zip_longest

import pytest


def perms(items: str) -> Iterator[str]:

    yield "b"


@pytest.mark.parametrize(
    "items,expected_perms",
    (
        ("a",("a",)),
        ("ab", ("ab", "ba")),
        ("abc", ("abc", "acb", "bac", "bca", "cba", "cab"))
    )
)
def test_perms(items, expected_perms):

    for actual, expected in zip_longest(perms(items), expected_perms):
        assert actual == expected
