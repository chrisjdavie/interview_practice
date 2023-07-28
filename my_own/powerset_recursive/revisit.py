"""
A big improvement from the other one, in terms of doing this - possibly
less helpful in solving the original thou
"""
from collections.abc import Iterator
from itertools import zip_longest


def powerset() -> Iterator[tuple[int, ...]]:

    base: int = 3

    def _solve(i) -> Iterator[tuple[int, ...]]:
        yield ()
        while i <= base:
            this = (i,)
            for res in _solve(i + 1):
                yield this + res
            i += 1

    yield from _solve(0)


def test():

    expected = [
        (),
        (0,), (0, 1), (0, 1, 2), (0, 1, 2, 3), (0, 1, 3), (0, 2), (0, 2, 3), (0, 3),
        (1,), (1, 2), (1, 2, 3), (1, 3),
        (2,), (2, 3),
        (3,),
    ]

    for e, a in zip_longest(expected, powerset()):
        assert e == a
