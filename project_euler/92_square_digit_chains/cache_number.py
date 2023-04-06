"""
This is a very simple cache, 
"""
def sum_of_squares(number: int) -> int:
    # doing this using strings and not *other* approaches. They're all O(digits of number), but string casting
    # is a slow way of handling numbers
    return sum(int(digit_str)**2 for digit_str in str(number))


def cache_decorator(func):
    cache: dict[int, int] = {
        89: 89,
        1: 1
    }
    def wrapped(number: int) -> int:
        return func(number, cache)

    return wrapped


@cache_decorator
def arrives_at_one_or_eighty_nine(number: int, cache: dict[int, int]) -> int:
    numbers_not_in_cache: list[int] = []
    
    # this most obviously can involve a cache, not certain best approach
    while number not in cache:
        numbers_not_in_cache.append(number)
        number = sum_of_squares(number)

    result: int = cache[number]

    for num_cache_miss in numbers_not_in_cache:
        cache[num_cache_miss] = result

    return result


def count_arrives_at_eighty_nine(threshold: int) -> int:
    return sum(1 if arrives_at_one_or_eighty_nine(number) == 89 else 0 for number in range(1, threshold))

if __name__ == "__main__":
    count_arrives_at_eighty_nine(10**5)
