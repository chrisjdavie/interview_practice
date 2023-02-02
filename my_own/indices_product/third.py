# thrid time, the second was a lot better, but I still was pretty clunky with it
# also, yielding lists from iterators is unsafe, you can write them backwards, so
# tuple it is
from itertools import zip_longest
from typing import Iterator

import pytest


def product_indices(n: int) -> Iterator[tuple[int, ...]]:

    indices: list[int] = [0]*(n+1)
    yield tuple(indices)

    i: int = n

    while i >= 0:

        if indices[i] < n:
            indices[i] += 1
            yield tuple(indices)
            i = n
        else:
            indices[i] = 0
            i -= 1


@pytest.mark.parametrize(
    "base,expected_indices",
    (
        (0, [(0,)]),
        (1, [(0,0), (0,1), (1,0), (1,1)]),
        (2, [(0,0,0), (0,0,1), (0,0,2), (0,1,0), (0,1,1), (0,1,2), (0,2,0), (0,2,1), (0,2,2), (1,0,0), (1,0,1), (1,0,2), (1,1,0), (1,1,1), (1,1,2), (1,2,0), (1,2,1), (1,2,2), (2,0,0), (2,0,1), (2,0,2), (2,1,0), (2,1,1), (2,1,2), (2,2,0), (2,2,1), (2,2,2)])
    )
)
def test_indices(base, expected_indices):

    for act_inds, expt_inds in zip_longest(product_indices(base), expected_indices):
        assert act_inds == expt_inds
