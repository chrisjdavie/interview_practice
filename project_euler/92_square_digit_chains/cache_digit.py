"""
This is a very simple cache, 
"""
import sys
from collections import Counter
from typing import Iterable

def sum_of_squares(number: Iterable[str]) -> int:
    # doing this using strings and not *other* approaches. They're all O(digits of number), but string casting
    # is a slow way of handling numbers
    return sum(int(digit_str)**2 for digit_str in number)


cache_key = frozenset[tuple[str,int]]


def convert_str_to_cache_key(digits: str) -> cache_key:
    return frozenset(Counter(digits).items())


def cache_decorator(func):
    cache: dict[cache_key, int] = {
        convert_str_to_cache_key("89"): 89,
        convert_str_to_cache_key("1"): 1
    }
    def wrapped(number: int) -> int:
        return func(number, cache)

    return wrapped


@cache_decorator
def arrives_at_one_or_eighty_nine(number: int, cache: dict[int, int]) -> int:
    keys_not_in_cache: list[cache_key] = []
    
    # this most obviously can involve a cache, not certain best approach
    number_str = str(number)
    number_key: cache_key = convert_str_to_cache_key(number_str)
    while number_key not in cache:
        keys_not_in_cache.append(number_key)
        number: int = sum_of_squares(number_str)
        number_str: str = str(number)
        number_key: cache_key = convert_str_to_cache_key(number_str)

    result: int = cache[number_key]

    for key in keys_not_in_cache:
        cache[key] = result

    return result


def count_arrives_at_eighty_nine(threshold: int) -> int:
    return sum(1 if arrives_at_one_or_eighty_nine(number) == 89 else 0 for number in range(1, threshold))

if __name__ == "__main__":
    power = int(sys.argv[1])
    count_arrives_at_eighty_nine(10**power)
