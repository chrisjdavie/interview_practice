"""
Cos it took me way more effort than I thought to do this the first time

-----

Did much better, but got the test case wrong again...
"""
def powerset_recursive() -> list[list[int]]:

    numbers = [0, 1, 2, 3]

    def _solve(ind_num: int) -> list[list[int]]:

        results = []

        for i, n in enumerate(numbers[ind_num:]):
            results.append([n])
            for r in _solve(ind_num + i + 1):
                results.append([n] + r)

        return results

    return _solve(0)


def test():

    expected = [
        [0,], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 3], [0, 2], [0, 2, 3], [0, 3],
        [1,], [1, 2], [1, 2, 3], [1, 3],
        [2,], [2, 3],
        [3,],
    ]

    assert expected == powerset_recursive()
