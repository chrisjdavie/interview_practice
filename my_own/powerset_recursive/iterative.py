"""
Realisted I was thinking about this recursively, but the iterative approach is fine too.

Noticed this while writing out the tests, don't *think* it applies to the case I'm interested
in, but I'll think on it
"""
from itertools import zip_longest
from collections.abc import Iterator


def powerset() -> Iterator[tuple[int, ...]]:

    end: int = 3

    c = [-1]
    while c:
        c[-1] += 1
        yield tuple(c)

        if c[-1] < end:
            c.append(c[-1])
        else:
            c.pop() 


def test():

    expected = [
        (0,), (0, 1), (0, 1, 2), (0, 1, 2, 3), (0, 1, 3), (0, 2), (0, 2, 3), (0, 3),
        (1,), (1, 2), (1, 2, 3), (1, 3),
        (2,), (2, 3),
        (3,),
    ]

    for e, a in zip_longest(expected, powerset()):
        assert e == a
