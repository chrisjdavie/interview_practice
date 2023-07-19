"""
So I want a power set, but I want the execution in a certain order - implying there's work to with each chunk,
that depends on the other chunks to some extent, but I don't want to repeat it
"""
from itertools import zip_longest


def powerset() -> tuple[int]:

    cands = [0, 1, 2, 3]

    def _solve(start):
        results = []
        for i, c in enumerate(cands[start:]):
            results.append([c])
            for r in _solve(start+i+1):
                results.append([c] + r)
        return results

    return _solve(0)


def test():

    pattern = (
        [0,],
        [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 3],
        [0, 2], [0, 2, 3],
        [0, 3],
        [1,], 
        [1, 2], [1, 2, 3],
        [1, 3],
        [2,], 
        [2, 3],
        [3,],
    )

    for producted, expected in zip_longest(powerset(), pattern):
        assert producted == expected
