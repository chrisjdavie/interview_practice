from typing import Iterator
from itertools import zip_longest

import pytest

def _perms(items: list[str], pos: int) -> Iterator[str]:

    if pos == len(items):
        yield "".join(items)

    for i_pos in range(pos, len(items)):
        items[pos], items[i_pos] = items[i_pos], items[pos]
        yield from _perms(items, pos + 1)
        items[pos], items[i_pos] = items[i_pos], items[pos]


def perms(items: str) -> Iterator[str]:
    yield from _perms(list(items), 0)


@pytest.mark.parametrize(
    "items,expected_perms",
    (
        ("1", ["1"]),
        ("12", ["12", "21"]),
        ("123", ["123", "132", "213", "231", "321", "312"]),
        ("1234", ["1234", "1243", "1324", "1342", "1423", "1432", "2134", "2143", "2314", "2341", "2413", "2431", "3124", "3142", "3214", "3241", "3412", "3421", "4123", "4132", "4213", "4231", "4312", "4321"])
    )
)
def test_perms(items, expected_perms):

    _expected = set(expected_perms)

    for act_perm in perms(items):
        assert act_perm in _expected
        _expected.remove(act_perm)
    assert len(_expected) == 0
