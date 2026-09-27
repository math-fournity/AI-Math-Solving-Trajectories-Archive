"""Explore pattern for part (c): infinitely many n with S(n) = n^2 - 14."""
import math
from functools import lru_cache

def is_square(n):
    if n < 0: return False
    s = int(math.isqrt(n))
    return s * s == n

def is_representable(e):
    if e < 0: return False
    if e == 0: return True
    b = 0
    while 8 * b <= e:
        if (e - 8 * b) % 3 == 0: return True
        b += 1
    return False

def min_summands(e):
    if e == 0: return 0
    best = None
    b = 0
    while 8 * b <= e:
        rem = e - 8 * b
        if rem % 3 == 0:
            a = rem // 3
            if best is None or a + b < best: best = a + b
        b += 1
    return best

@lru_cache(maxsize=None)
def is_sum_k_pos_squares_bounded(N, k, maxval):
    if k == 0: return N == 0
    if k == 1: return is_square(N) and 1 <= int(math.isqrt(N)) <= maxval and N >= 1
    if N < k: return False
    if N > k * maxval * maxval: return False
    hi = min(maxval, math.isqrt(N - (k - 1)))
    lo = max(1, math.isqrt(N // k))
    if lo * lo < N / k: lo += 1
    lo = max(1, lo)
    for ak in range(hi, lo - 1, -1):
        rem = N - ak * ak
        if is_sum_k_pos_squares_bounded(rem, k - 1, ak): return True
    return False

def achievable(n, k):
    N = n * n
    if k < 1 or k > N: return False
    if k == N: return True
    e = N - k
    if is_representable(e):
        ms = min_summands(e)
        if ms is not None and ms <= k: return True
    if k <= 200:
        return is_sum_k_pos_squares_bounded(N, k, n)
    return False

def check_S(n):
    """Check if S(n) = n^2 - 14. Returns (True, first_fail_k) or (True, None)."""
    N = n * n
    target = N - 14
    for k in range(1, target + 1):
        if not achievable(n, k):
            return False, k
    if achievable(n, N - 13):
        return False, N - 13  # S(n) > n^2-14
    return True, None

# Find all working n up to 80
working = []
not_working = []
for n in range(4, 80):
    ok, fail = check_S(n)
    if ok:
        working.append(n)
    else:
        not_working.append((n, fail))

print("Working n (S(n)=n^2-14):", working)
print()
print("Not working, first failure k:")
for n, fail in not_working:
    N = n * n
    print(f"  n={n}: fails at k={fail} (defect e={N-fail})")
