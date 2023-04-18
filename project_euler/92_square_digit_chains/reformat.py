import json


with open("timings.json", "r") as fh:
    timings: dict[str, dict[str, int]] = json.load(fh)

exps: set[str] = set()

for _, exps_t in timings.items():
    for e in exps_t:
        exps.add(e)
exps.discard("4")

num_cols = len(exps) + 1

print(
    "| Module | Timing/s" + " |" * (num_cols - 1)
)
print("|" + "-|"*num_cols )
timings_row = "| |"
for e in sorted(exps):
    timings_row += f" **10<sup>{e}</sup>** |"
print(timings_row)

from math import floor, log10

def round_to_2(x):
    return  round(x, -int(floor(log10(abs(x))) - 1))

for f, exps_t in timings.items():
    file_row = f"| {f} |"
    for e in sorted(exps):
        if e in exps_t:
            file_row += f" {round_to_2(exps_t[e])}"
        file_row += " |"
    print(file_row)
