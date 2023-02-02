# the first try at this took me a really long time to figure out, so I'm 
# trying again. Slow is smooth, smooth is fast
from itertools import zip_longest
from typing import Iterable

import pytest

def product_indices(n: int) -> Iterable[list[int]]:

    inds = [0]*(n+1)

    i = n

    yield inds
    while i >= 0:
        if inds[i] < n:
            inds[i] += 1
            yield inds
            i = n
        else:
            inds[i] = 0
            i -= 1


@pytest.mark.parametrize(
    "base,expected_indices",
    (
        (0, [[0,]]),
        (1, [[0,0], [0,1], [1,0], [1,1]]),
        (2, [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2], [0,2,0], [0,2,1], [0,2,2], [1,0,0], [1,0,1], [1,0,2], [1,1,0], [1,1,1], [1,1,2], [1,2,0], [1,2,1], [1,2,2], [2,0,0], [2,0,1], [2,0,2], [2,1,0], [2,1,1], [2,1,2], [2,2,0], [2,2,1], [2,2,2]])
    )
)
def test_indices(base, expected_indices):

    for act_inds, expt_inds in zip_longest(product_indices(base), expected_indices):
        assert act_inds == expt_inds
