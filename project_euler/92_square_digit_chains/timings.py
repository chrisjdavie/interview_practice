
import timeit
print(timeit.timeit("count_arrives_at_eighty_nine(10**5)", "from naive_approach import count_arrives_at_eighty_nine", number=10))
