import pytest

from cache_digit import sum_of_squares, arrives_at_one_or_eighty_nine, count_arrives_at_eighty_nine


@pytest.mark.parametrize(
    "number,expected_sum_of_squares",
    (
        (44, 32),
        (32, 13),
        (4, 16),
    )
)
def test_sum_of_squares(number, expected_sum_of_squares):
    assert sum_of_squares(str(number)) == expected_sum_of_squares


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
