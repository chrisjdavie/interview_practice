import sys

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


if __name__ == "__main__":
    power = int(sys.argv[1])
    count_arrives_at_eighty_nine(10**power)
