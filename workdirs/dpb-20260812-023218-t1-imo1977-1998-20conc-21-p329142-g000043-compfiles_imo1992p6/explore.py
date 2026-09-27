"""
IMO 1992 P6 exploration.

S(n) = greatest integer such that for every k <= S(n), n^2 is a sum of k positive squares.

Key idea: "defect" e = n^2 - k. If n^2 = sum of k positive squares,
write a_i = 1 for most, then sum(a_i^2 - 1) = e over non-1 terms.
Non-1 term a contributes a^2-1 in {3, 8, 15, 24, ...}.
Since 15=3*5, 24=3*8, 35=8+27, etc., the representable set R = {3a+8b : a,b>=0}
= all nonneg integers except {1,2,4,5,7,10,13}.

So k = n^2 - e is achievable (via defect method, starting from all 1s and merging)
iff e in R and number of summands <= k.

For small k, need direct representation (backtracking search).
"""
import math
from functools import lru_cache

def is_square(n):
    if n < 0:
        return False
    s = int(math.isqrt(n))
    return s * s == n

# Representable set: 3a + 8b
def is_representable(e):
    """Can e be written as 3a + 8b, a,b >= 0?"""
    if e < 0:
        return False
    if e == 0:
        return True
    # try b from 0 to e//8
    b = 0
    while 8 * b <= e:
        if (e - 8 * b) % 3 == 0:
            return True
        b += 1
    return False

def min_summands(e):
    """Minimum a+b such that 3a+8b = e, a,b >= 0. Returns None if not representable."""
    if e == 0:
        return 0
    best = None
    b = 0
    while 8 * b <= e:
        rem = e - 8 * b
        if rem % 3 == 0:
            a = rem // 3
            if best is None or a + b < best:
                best = a + b
        b += 1
    return best

# Non-representable defects
non_repr = [e for e in range(50) if not is_representable(e)]
print("Non-representable defects:", non_repr)

# Direct check: is N a sum of k positive squares? (backtracking)
def is_sum_k_pos_squares(N, k):
    """Check if N = a1^2 + ... + ak^2 with all ai >= 1, ai non-decreasing."""
    if k == 0:
        return N == 0
    if k == 1:
        return is_square(N) and N >= 1
    if N < k:  # each >= 1, so sum of squares >= k
        return False
    if k == 2:
        # N = a^2 + b^2, a,b >= 1
        a = 1
        while a * a <= N - 1:
            if is_square(N - a * a):
                return True
            a += 1
        return False
    # General backtracking: choose a_k (largest) from ceil(sqrt(N/k)) to sqrt(N-(k-1))
    lo = max(1, math.isqrt((N - (k - 1)) // k) )  # rough lower bound
    # a_k^2 >= N/k (since a_k is largest, N <= k * a_k^2)
    lo = max(1, math.isqrt((N + k - 1) // k))  # ceil(sqrt(N/k))
    if lo * lo < (N + k - 1) // k:  # adjust
        lo += 1
    lo = max(1, math.isqrt(N // k))
    if lo * lo < N / k:
        lo += 1
    hi = math.isqrt(N - (k - 1))
    # Search a_k from hi down to lo, with a_k >= 1
    # We need a_1 <= ... <= a_k, so a_{k-1} <= a_k
    for ak in range(hi, lo - 1, -1):
        rem = N - ak * ak
        # need rem = sum of k-1 positive squares, each <= ak
        if is_sum_k_pos_squares_bounded(rem, k - 1, ak):
            return True
    return False

@lru_cache(maxsize=None)
def is_sum_k_pos_squares_bounded(N, k, maxval):
    """Check if N = a1^2+...+ak^2, 1 <= a_i <= maxval, non-decreasing."""
    if k == 0:
        return N == 0
    if k == 1:
        return is_square(N) and 1 <= int(math.isqrt(N)) <= maxval and N >= 1
    if N < k:
        return False
    if N > k * maxval * maxval:
        return False
    # choose largest a_k <= maxval, a_k^2 <= N - (k-1)
    hi = min(maxval, math.isqrt(N - (k - 1)))
    lo = max(1, math.isqrt(N // k))
    if lo * lo < N / k:
        lo += 1
    lo = max(1, lo)
    for ak in range(hi, lo - 1, -1):
        rem = N - ak * ak
        if is_sum_k_pos_squares_bounded(rem, k - 1, ak):
            return True
    return False

# Combined: is n^2 a sum of k positive squares?
def achievable(n, k):
    """Is n^2 a sum of k positive squares?"""
    N = n * n
    if k < 1 or k > N:
        return False
    if k == N:
        return True  # all 1s
    e = N - k
    # Defect method: e = 3a+8b, a+b <= k
    if is_representable(e):
        ms = min_summands(e)
        if ms is not None and ms <= k:
            return True
    # Direct search for small k
    if k <= 200:  # only for small k
        return is_sum_k_pos_squares_bounded(N, k, n)
    return False

# Compute S(n) for small n
def compute_S(n):
    """Find S(n): largest s such that all k from 1 to s are achievable."""
    N = n * n
    s = 0
    for k in range(1, N + 1):
        if achievable(n, k):
            s = k
        else:
            break
    return s

# Test part (a): S(n) <= n^2 - 14 for n >= 4
print("\n=== Part (a) check ===")
for n in range(4, 20):
    Sn = compute_S(n)
    print(f"n={n}, n^2={n*n}, S(n)={Sn}, n^2-14={n*n-14}, S(n)<=n^2-14: {Sn <= n*n - 14}")

print("\n=== Part (b): find n with S(n) = n^2 - 14 ===")
for n in range(4, 60):
    N = n * n
    # Check if k = n^2 - 13 fails (should always fail for n >= 4)
    # and all k from 1 to n^2 - 14 succeed
    target = N - 14
    all_ok = True
    first_fail = -1
    for k in range(1, target + 1):
        if not achievable(n, k):
            all_ok = False
            first_fail = k
            break
    # Also check k = n^2 - 13 fails
    k_check = N - 13
    fails_at_13 = not achievable(n, k_check)
    if all_ok and fails_at_13:
        print(f"n={n}: S(n) = n^2 - 14 = {target}  *** FOUND ***")
    elif all_ok and not fails_at_13:
        print(f"n={n}: all k<=n^2-14 work but k=n^2-13 also works?? S(n) > n^2-14")
    # else:
    #     print(f"n={n}: fails at k={first_fail}")
