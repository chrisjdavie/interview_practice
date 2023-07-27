from itertools import zip_longest
from collections.abc import Iterator

import pytest


def product_indices(base: int) -> Iterator[tuple[int,...]]:

    indices: list = [0]*(base + 1)

    yield tuple(indices)

    i: int = base

    while i >= 0:
        if indices[i] < base:
            indices[i] += 1
            yield tuple(indices)
            i: int = base
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

