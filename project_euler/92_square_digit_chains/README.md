# Project Euler 92 - Square digit chains

https://projecteuler.net/problem=92

```
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
```

## Why I'm looking at this

There are two aspects - I didn't solve this well during an interview, and there are interesting cache dynamics in the optimised solution that I hadn't come across before.

### Interview problems

Had an interview where I didn't solve this super well. There were two sides to it, though I'd been practicing leetcode style problems, I hadn't been practicing as if I was solving it in the context of an interview, and that threw me.

The other was once I calmed myself down, I didn't really come up with the optimal solution, but as it's not one of those ones that has an *obvious* O analysis, it's not super clear what optimisations are actual optimisations.

I wouldn't be keen on this sort of question in an interview, seems like people could very easily stumble on it, but don't really have insight into the process that led to this decision (or if there was a thoughtful process at all!)

This is addressing the second problem, and partly curiousity on my part - it seems like there could be a lot of optimisations, and I don't know that they're all obvious or how the current CPython implementation of things occurs. I'll document more as I go.

### Cache behaviours

There's an optimisation for this, a common one, memoization/caching of previously caclulated results and reusing them. But the cached solution, while ~4x faster in the cases examine, was a much lower speed up than I expected looking at the examples.

It turns out, the increase in number of steps to calculate the result is much smaller as you go to big numbers, so if you just look at small number examples, less than say `162` , you get a misrepresentation of how difficult it will be to calculate larger numbers. I sumarised it in the discussion as; 

"The sum of the square of digits of big numbers is a much, much smaller number, so calculating it won't take as long as you'd expect if you only think of small number examples."

I do a more mathsy thing below that says that, but it isn't a complete analysis, I just wanted to get a feel for the cache behaviour.

## Approaches

### Direct computation, `naive.py`

A more or less direct computation of the problem in project Euler - for each number, calculate the sum of squares of the digits until it reaches 1 or 89, return the value

### Memoization (caching) of each number, `cache_number.py`

While calculating the sum of the squares, there are two obvious optimisations - the calculation for sum of the squares of each digit is repeated multiple times. For instance, for `4` , the sum of the squares until it reaches 89 is

```
4 → 16 → 37 → 58 → 89
```

And so we have already calculated the sum of the squares for `16` , `37` and `58` . Of course, we also know that the result of the calculation for each of these is `89` , so after we find that this tends to 89, we simply cache that the results for `4` , `16` , `37` and `59` are `89` . And of course, for say `200` , the sum of the squares of the digits is `4` , so when we hit `4` in the cache, we know the answer is `89` , saving recalculating. (and of course mapping `200` to the result `89` in the cache.)

### Memoization (caching) of the digits, `cache_digit.py`

A final optimisation I tried was rather than caching on the number, I cached on the combination of the digits. Obviously, the sum of the squares of the digits for `58` and `85` will be the same, so there's no need to recalculate the digits here.

I did not want to calculate the permutations of each number - calculating the permutations should be the same complexity as calculating the square of the digits, for each permutation linear with respect to number of digits. But there are unordered objects that are equivalent - sets.

Sets in Python are mutable so not hashable, and thus cannot be keys for a cache. But Python also has `frozenset` , which is immuatable and thus hashable, is appropriate in this case as the digits of a number are unchaning.

A complication is that sets only take unique entries, so `99` would be stored as `{9,}` . Tuples are hashable, so a solution is having the key be a `frozenset` of a tuple representation of the number, so the cache key for `9` is `(9, 1)` and the cache key for `99` is `(9, 2)` .

In code, this can be expressed as 

```
def convert_str_to_cache_key(digits: str) -> cache_key:
    return frozenset(Counter(digits).items())
```

This is *not* a simple data structure, but as you get increasing numbers, the proportion of numbers that are permutations of others probably increases ( `12` and `21` , compared to `123` , `132` , `213` , `231` , `312` and `321` ). So although calculating this takes time, I was expecting that the decrease in duplicate computation would mean this solution was a *lot* faster. (Spoilers - I was wrong!)

## Timings

Calculations run using timings.py, command with `<module>` and `<count>` set as in the file `tasks.py` , on my personal laptop (an aging Dell XPS 13). I initially did this internally in Python, but the caches didn't clear.

| Module | Timing/s | | |
|-|-|-|-|
| | **10<sup>5</sup>** | **10<sup>6</sup>** | **10<sup>7</sup>** |
| naive | 0.4 | 4.7 | |
| cache_number | 0.15 | 1.5 | 15.0 |
| cache_digit | 0.19 | 1.9 | 20.0 |

This is interesting - the cache was signifcantly faster (not as much as I expected), but caching the digits was slower than caching the number, which I wasn't expecting. 

## Analysis

I investigated this a little, and believe both the caching not being the speed up I expected and the digit caching being slower than the number caching is due to the dynamics of the problem.

Let us take, for example, **10<sup>7</sup>**. The biggest sum of digits will be `10**7 - 1` , or `9999999` (as any other number will have at least one smaller digit). The sum of the square of the digits here is `(9**2)*7` , `567` . So this suggests that the complexity of the naive problem is perhaps of the form `O(N) + A(N)*m*N^(1/2)*N` - `m` being the worst case length of the digits, `N` being the number of numbers, and of course `N = 10**m` , so `m = log10(N)` , so the final complexity is something like

```
O(N)*log(n) + A(N)*log(n)*N^(1/2)*N
```

Where `A(N)` is the number of average steps it takes to get to `89` or `1` for numbers below `567` (more generally `(10**m - 1)^(1/2)` ), which isn't immedately obvious (might be of log form, but I wouldn't be confident. Might also not be analytically calculable).

All this is a very maths way of saying "the sum of the square of digits of big numbers is a much smaller number, so calculating it won't take as long as you'd expect if you only think of small number examples".

So this explains why the caching isn't so much faster than I thought it would be. But it also explains why caching on the digits isn't faster - once you've populated the cache for `567` (in this example), all higher cached values are never used, and so in both cases, above this number, cache storing and access will be linear, and, as stated above, `567` is much smaller than `10**7` .

(This is limited to `m` > 2, as `(9**2)*2` is `162` greater than `99` , so the cache needs to be populated fully).

## Further optimisations

I'm not going to do these, but it'd make it faster.

I could can populate the cache up to `sum_of_squares((9**2)*m)` , and then abandon populating the cache and the cache key, which wouldn't change the complexity of the problem but would wipe out most of the time and memory spent populating the cache.

It's also straightforwardly parallelisable - for any number of cores `L` , have each core calc the cache up to `sum_of_squares((9**2)*m)` , and then only calc the result for steps of `L` on each core, and sum the results on completion (of course dealing with each core having calculated the cache).

And of course, we can do simple, repeated computations in a lower level compiled language that should take a lot less time than calculating this in a Python virtual machine.
