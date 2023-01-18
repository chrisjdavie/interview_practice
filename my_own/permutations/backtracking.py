from typing import Iterator
from itertools import zip_longest

import pytest


def _perms(items: list[str], pos: int) -> Iterator[str]:

    if pos + 1 == len(items):
        yield "".join(items)
    else:
        for i in range(pos,len(items)):
            items[pos], items[i] = items[i], items[pos]
            yield from _perms(items, pos + 1)
            items[pos], items[i] = items[i], items[pos]


def perms(items: str) -> Iterator[str]:
    yield from _perms(list(items), 0)


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
