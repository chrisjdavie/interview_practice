# this is using indices and product. This is not how leetcode wants it, as 
# it's not using constant memory
import pytest


def next_perm(nums: list[int]) -> None:
    if len(set(nums)) == 1:
        return

    # establish mapping
    mapping_n_c = {n: c for c, n in enumerate(sorted(nums))}
    mapping_c_n = {c: n for c, n in enumerate(sorted(nums))}

    condensed = [mapping_n_c[n] for n in nums]
    max_cond = max(condensed)
    m = max_cond
    while m >= 0: # think about loop limit
        if condensed[m] < max_cond:
            condensed[m] += 1
            if len(set(condensed)) == len(condensed):
                break
            m = max_cond
        else:
            condensed[m] = 0
            m -= 1

    if m == -1:
        for i, c in enumerate(sorted(nums)):
            nums[i] = c
    else:
        for i, c in enumerate(condensed):
            nums[i] = mapping_c_n[c]        


@pytest.mark.parametrize(
    "nums,expected_next_perm",
    (
        ([1,1], [1,1]),
        ([1,5,7], [1,7,5]),
        ([1,2,3], [1,3,2]),
        ([3,2,1], [1,2,3]), # looping case
        ([1,1,5], [1,5,1]), # duplicates case
        ([1,2,1,3,1], [1,2,3,1,1]),
        ([1,2,3,1,1], [1,3,1,1,2])
    )
)
def test_next_perm(nums, expected_next_perm):

    next_perm(nums)
    assert nums == expected_next_perm
