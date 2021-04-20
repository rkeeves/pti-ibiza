## pti-ibiza

This project contains Python code for all algorithms that IBIZA course covered so far.

These algorithms are MEANT TO BE SLOW. Their main purpose is not to just solve the problem, but give textual output to the user on stdout.
All the algoirthms pretty print the answer in a really verbose manner.

An example output of fastexp is like this:

```
Solve 3^123 mod 51
1. Compute partial results
[ 0]        123 (1) =>    3^(2^ 0) ==      3 mod   51 ==    3 mod   51
[ 1]         61 (1) =>    3^(2^ 1) ==      9 mod   51 ==    9 mod   51
[ 2]         30 (0) =>    3^(2^ 2) ==     81 mod   51 ==   30 mod   51
[ 3]         15 (1) =>    3^(2^ 3) ==    900 mod   51 ==   33 mod   51
[ 4]          7 (1) =>    3^(2^ 4) ==   1089 mod   51 ==   18 mod   51
[ 5]          3 (1) =>    3^(2^ 5) ==    324 mod   51 ==   18 mod   51
[ 6]          1 (1) =>    3^(2^ 6) ==    324 mod   51 ==   18 mod   51
2. Compute final product
3 ^ 123 mod 51 == 3 * 9 * 33 * 18 * 18 * 18 mod 51 = 24
```

The output of a Miller-Rabin test is like this:

```
CASE prime_candidate = 197, testnumbers=[7, 11]
1. Compute S, such that
   S =
  = max( {r| 2^r divides (n - 1)} ) =
  = max( {r| 2^r divides (197 - 1)} ) =
  = max( {r| 2^r divides (196)} ) =
  = max([0, 1, 2])
  = 2
2. Compute d, such that
  d =
  = (n-1) * (2 ^ S)
  = (197-1) * (2 ^ 2)
  = 196 * (2 ^ 2)
  = 196 * 4
  = 49
3. Thus S=2 and d=49.
4. We loop through all bases from [7, 11] and checl the following:
  If 197 is prime and gcd(base, 197) = 1
  Then either
    - base^49 == 1 mod 197
    - there exists r in [0, 1] such that base^(49^(2^r)) == -1 mod 197
    Base 7
      First Check: 7^49 == 1 mod 197 = 196 ?== 1
      Failed, so we continue checking different r values from [0, 1]
        Check r = 0
        7 ^ (49*(2^0)) = 7 ^ (49*1) = 7 ^ 49 = 196 ?== -1 mod 197
        Passed so it can be a prime
    Base 11
      First Check: 11^49 == 1 mod 197 = 183 ?== 1
      Failed, so we continue checking different r values from [0, 1]
        Check r = 0
        11 ^ (49*(2^0)) = 11 ^ (49*1) = 11 ^ 49 = 183 ?== -1 mod 197
        Failed so we continue checking
        Check r = 1
        11 ^ (49*(2^1)) = 11 ^ (49*2) = 11 ^ 98 = 196 ?== -1 mod 197
        Passed so it can be a prime
```
