"""
This assumes it's being run in the virtual env - I'm doing it like this in an
attempt to stop the cache from being preserved between runs.

It'll mess the timings up a little cos it's going to be relaunching a Python
session each time, but what can you do?
"""
import json
import statistics

from invoke import task


@task
def time_run(c, file="cache_digit", power="5"):

    execution_times: list[float] = []

    for _ in range(5):
        result = c.run(f"time -p python {file}.py {power}")
        execution_times.append(
            float(result.stderr.split("\n")[1].split(" ")[1])
        )

    avg_run_time = statistics.mean(execution_times)
    print(avg_run_time)
    return avg_run_time


@task
def time_all(c):

    files_exps = {
        "naive": [4, 5, 6],
        "cache_number": [4, 5, 6, 7],
        "cache_digit": [4, 5, 6, 7],
    }

    timings: dict[str, dict[str, float]] = {}

    for f in files_exps:
        print()
        print(f"Running {f}")
        timings[f] = {}
        for exp in files_exps[f]:
            print(f"10**{exp}")
            time_taken = time_run(c, f, exp)
            timings[f][exp] = time_taken
            print(f"time: {time_taken}")

    with open("timings.json", "w") as fh:
        json.dump(timings, fh)
