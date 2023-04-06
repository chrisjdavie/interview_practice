"""
https://projecteuler.net/problem=92

Had an interview where I didn't solve this super well. There were two sides to it, though I'd been practicing
leetcode style problems, I hadn't been practicing as if I was solving it in the context of an interview, and
that threw me.

The other was once I calmed myself down, I didn't really come up with the optimal solution, but as it's not
one of those ones that has an *obvious* O analysis, it's not super clear what optimisations are actual
optimisations.

I wouldn't be keen on this sort of question in an interview, seems like people could very easily stumble on it,
but don't really have insight into the process that led to this decision (or if there was a thoughtful process at all!)

This is addressing the second problem, and partly curiousity on my part - it seems like there could be a lot
of optimisations, and I don't know that they're all obvious or how the current CPython implementation of things
occurs. I'll document more as I go
"""
import pytest


def sum_of_squares(number: int) -> int:
    # doing this using strings and not *other* approaches. They're all O(digits of number), but string casting
    # is a slow way of handling numbers
    return sum(int(digit_str)**2 for digit_str in str(number))
    

def arrives_at_one_or_eighty_nine(number: int) -> int:
    # this most obviously can involve a cache, not certain best approach
    while number != 89 and number != 1:
        number = sum_of_squares(number)

    return number


def count_arrives_at_eighty_nine(threshold: int) -> int:
    return sum(1 if arrives_at_one_or_eighty_nine(number) == 89 else 0 for number in range(1, threshold))


@pytest.mark.parametrize(
    "number,expected_sum_of_squares",
    (
        (44, 32),
        (32, 13),
        (4, 16),
    )
)
def test_sum_of_squares(number, expected_sum_of_squares):
    assert sum_of_squares(number) == expected_sum_of_squares


@pytest.mark.parametrize(
    "number,arrives_at",
    (
        (44, 1),
        (85, 89),
        (20, 89),
    )
)
def test_arrives_at_one_or_eighty_nine(number, arrives_at):
    assert arrives_at_one_or_eighty_nine(number) == arrives_at


@pytest.mark.parametrize(
    "threshold,expected_eighty_nine_count",
    (
        (10**2, 80),
        (10**3, 857),
        (10**4, 8558),
        (10**5, 85623),
    )
)
def test_count_arrives_at_eighty_nine(threshold, expected_eighty_nine_count):
    assert count_arrives_at_eighty_nine(threshold) == expected_eighty_nine_count
