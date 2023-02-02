from typing import Iterator
from itertools import zip_longest

import pytest

def permutations(iterable):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    indices = list(range(n))
    cycles = list(range(n, 0, -1))
    yield "".join(pool[i] for i in indices)
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield "".join(pool[i] for i in indices)
                break
        else:
            return

@pytest.mark.parametrize(
    "items,expected_perms",
    (
        ("0", ["0"]),
        ("01", ["01", "10"]),
        ("012", ["012", "021", "102", "120", "201", "210"]),
        ("0123", ["0123", "0132", "0213", "0231", "0312", "0321", "1023", "1032", "1203", "1230", "1302", "1320", "2013", "2031", "2103", "2130", "2301", "2310", "3012", "3021", "3102", "3120", "3201", "3210"])
    )
)
def test_perms(items, expected_perms):

    for act_perm, expt_perm in zip_longest(permutations(items), expected_perms):
        assert act_perm == expt_perm
