
import statistics
import timeit

print(
    statistics.mean(
        (
            timeit.timeit(
                "count_arrives_at_eighty_nine(10**5)",
                "from cache_number import count_arrives_at_eighty_nine",
                number=1
            )
            for _ in range(10)
        )
    )
)
