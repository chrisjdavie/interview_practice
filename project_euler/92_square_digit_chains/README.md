# Project Euler 92 - Square digit chains

https://projecteuler.net/problem=92

## Why I'm looking at this

Had an interview where I didn't solve this super well. There were two sides to it, though I'd been practicing leetcode style problems, I hadn't been practicing as if I was solving it in the context of an interview, and that threw me.

The other was once I calmed myself down, I didn't really come up with the optimal solution, but as it's not one of those ones that has an *obvious* O analysis, it's not super clear what optimisations are actual optimisations.

I wouldn't be keen on this sort of question in an interview, seems like people could very easily stumble on it, but don't really have insight into the process that led to this decision (or if there was a thoughtful process at all!)

This is addressing the second problem, and partly curiousity on my part - it seems like there could be a lot of optimisations, and I don't know that they're all obvious or how the current CPython implementation of things occurs. I'll document more as I go

## Timings

**THESE TIMINGS ARE NOT VALID AS `timeit` PRESERVES THE CACHE BETWEEN RUNS, GOING TO LOOK AT THIS TOMORROW WITH BASH**

```
avg_time() {
    #
    # usage: avg_time n command ...
    #
    n=$1; shift
    (($# > 0)) || return                   # bail if no command given
    for ((i = 0; i < n; i++)); do
        { time -p "$@" &>/dev/null; } 2>&1 # ignore the output of the command
                                           # but collect time's output in stdout
    done | awk '
        /real/ { real = real + $2; nr++ }
        /user/ { user = user + $2; nu++ }
        /sys/  { sys  = sys  + $2; ns++}
        END    {
                 if (nr>0) printf("real %f\n", real/nr);
                 if (nu>0) printf("user %f\n", user/nu);
                 if (ns>0) printf("sys %f\n",  sys/ns)
               }'
}
```

Calculations run using timings.py, command with `<module>` and `<count>` set as in the table below, on my personal laptop (an aging Dell XPS 13)

```
import statistics
import timeit

print(
    statistics.mean(
        timeit.repeat(
            "count_arrives_at_eighty_nine(<count>)",
            "from <module> import count_arrives_at_eighty_nine",
            repeat=10,
            number=1
        )
    )
)
```

| One    | Two | Three | Four    | Five  | Six
|-|-|-|-|-|-
| Span <td colspan=3>triple  <td colspan=2>double

| Module | Timing/s | | |
|-|-|-|-|
| | **10<sup>5</sup>**  | **10<sup>6</sup>** | **10<sup>7</sup>** |
| naive        | 0.37   | 4.3                | |
| cache_number | 0.029  | 0.28               | 3.3 |
| cache_digit  | 2.98   |
