from itertools import zip_longest
from typing import Iterator

import pytest


def product_indices(base: int) -> Iterator[tuple[int,...]]:

    indices: list[int] = [0]* (base + 1)
    current_pos: int = base

    while current_pos >= 0:

        yield tuple(indices)

        indices[-1] += 1
        current_pos: int = base
        while current_pos >= 0 and indices[current_pos] > base:
            indices[current_pos] = 0
            current_pos -= 1
            indices[current_pos] += 1


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
