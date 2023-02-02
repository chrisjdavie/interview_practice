# I want to code up this pattern:
# input (0, 1, 2), 3
# outputs { (0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), ... (2, 2, 1), (2, 2, 2) }
from typing import Iterator

import pytest

def simple_product(n: int) -> Iterator[list[int]]:

    result: list[int] = [0]*(n + 1)

    i: int = n

    yield result
    while i >= 0:
        result[i] += 1
        if result[i] < n + 1:
            yield result            
            i = n
        else:
            result[i] = 0
            i -= 1
