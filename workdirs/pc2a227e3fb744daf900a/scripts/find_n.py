import numpy as np

# We need smallest n with pi((n+1)^2) - pi(n^2) >= 1000
# PNT estimate: count ~ (2n+1)/(2 ln n) = 1000 => n ~ 1000 ln n ~ 9117
# So (n+1)^2 up to ~ 100 million. Sieve up to a safe bound.

import math

# Upper bound: try n up to 12000 => (12001)^2 ~ 144 million
N_MAX = 12002
LIMIT = (N_MAX + 1) ** 2  # ~144 million

# Sieve of Eratosthenes up to LIMIT
sieve = np.ones(LIMIT + 1, dtype=bool)
sieve[0] = sieve[1] = False
for i in range(2, int(math.isqrt(LIMIT)) + 1):
    if sieve[i]:
        sieve[i*i::i] = False

# prefix sum of prime counts
pi = np.cumsum(sieve.astype(np.int64))

# Find smallest n with pi[(n+1)^2] - pi[n^2] >= 1000
# Note: "between n^2 and (n+1)^2" - primes p with n^2 < p < (n+1)^2
# = pi[(n+1)^2 - 1] - pi[n^2]  (strictly between)
# But conventionally "between" might include endpoints; squares aren't prime anyway for n>=2.
# n^2 is not prime (n>=2), (n+1)^2 not prime. So pi((n+1)^2) - pi(n^2) counts primes in (n^2, (n+1)^2).

answer = None
for n in range(1, N_MAX):
    lo = n * n
    hi = (n + 1) * (n + 1)
    count = int(pi[hi]) - int(pi[lo])  # primes p with lo < p <= hi; since hi not prime, = primes in (lo, hi)
    # Actually pi[hi] counts primes <= hi. pi[lo] counts primes <= lo. Difference = primes in (lo, hi].
    # hi = (n+1)^2 is not prime, so = primes in (lo, hi) = (n^2, (n+1)^2). Good.
    if count >= 1000:
        answer = n
        print(f"n={n}, count={count}, interval=({lo},{hi})")
        # also print a few before for context
        for m in range(max(1, n-3), n):
            c2 = int(pi[(m+1)**2]) - int(pi[m*m])
            print(f"  n={m}, count={c2}")
        break

print(f"\nANSWER: {answer}")
