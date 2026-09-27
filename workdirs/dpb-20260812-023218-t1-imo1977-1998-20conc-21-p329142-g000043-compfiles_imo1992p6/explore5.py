"""Find explicit representations of 169 as sum of k positive squares for k=1..20."""
import math
from functools import lru_cache

def is_square(n):
    if n < 0: return False
    s = int(math.isqrt(n))
    return s * s == n

@lru_cache(maxsize=None)
def find_rep(N, k, maxval):
    """Find a representation of N as sum of k positive squares, each <= maxval, non-decreasing."""
    if k == 0:
        return () if N == 0 else None
    if k == 1:
        if is_square(N) and 1 <= int(math.isqrt(N)) <= maxval and N >= 1:
            return (int(math.isqrt(N)),)
        return None
    if N < k:
        return None
    if N > k * maxval * maxval:
        return None
    hi = min(maxval, math.isqrt(N - (k - 1)))
    lo = max(1, math.isqrt(N // k))
    if lo * lo < N / k: lo += 1
    lo = max(1, lo)
    for ak in range(hi, lo - 1, -1):
        rem = N - ak * ak
        sub = find_rep(rem, k - 1, ak)
        if sub is not None:
            return sub + (ak,)
    return None

N = 169
for k in range(1, 21):
    rep = find_rep(N, k, 13)
    if rep:
        squares = [x*x for x in rep]
        assert sum(squares) == N, f"Sum mismatch for k={k}"
        assert all(x >= 1 for x in rep), f"Non-positive for k={k}"
        print(f"k={k:2d}: {rep}  squares={squares}  sum={sum(squares)}")
    else:
        print(f"k={k:2d}: NOT FOUND")

# Also verify defect method boundary: for k=21, e=148
print("\n=== Defect method verification for k=21..25 ===")
for k in range(21, 26):
    e = N - k
    # Find min summands
    best = None
    best_ab = None
    for b in range(e // 8, -1, -1):
        rem = e - 8 * b
        if rem % 3 == 0 and rem >= 0:
            a = rem // 3
            if best is None or a + b < best:
                best = a + b
                best_ab = (a, b)
    print(f"k={k}, e={e}, 3a+8b: a={best_ab[0]}, b={best_ab[1]}, summands={best}, <=k: {best <= k}")
