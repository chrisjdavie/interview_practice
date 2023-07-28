from collections.abc import Iterator
from itertools import zip_longest


def powerset() -> Iterator[tuple[int, ...]]:

    base: int = 3

    yield ()

    results = [-1]

    while results:
        results[-1] += 1
        yield tuple(results)
        if results[-1] < base:
            results.append(results[-1])
        else:
            results.pop()
    

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
