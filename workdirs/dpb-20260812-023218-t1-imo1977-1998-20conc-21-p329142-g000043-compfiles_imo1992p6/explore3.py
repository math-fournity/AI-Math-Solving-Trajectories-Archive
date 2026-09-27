"""
Smarter achievable check using splitting method for intermediate k.
If n^2 = a^2 + b^2 (k=2), then by replacing a^2 with (a-t)^2 + (2at-t^2) ones,
we get k = 2 + 2at - t^2, and can merge ones to decrease k.
"""
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

# Find a 2-square representation of n^2
def find_two_squares(n):
    N = n * n
    for a in range(1, n):
        if is_square(N - a * a):
            return (a, int(math.isqrt(N - a * a)))
    return None

# Find a 3-square representation of n^2
def find_three_squares(n):
    N = n * n
    for a in range(1, n):
        for b in range(1, a + 1):
            c2 = N - a * a - b * b
            if c2 > 0 and is_square(c2):
                return (a, b, int(math.isqrt(c2)))
    return None

# Find a 4-square representation
def find_four_squares(n):
    N = n * n
    for a in range(1, n):
        for b in range(1, a + 1):
            for c in range(1, b + 1):
                d2 = N - a*a - b*b - c*c
                if d2 > 0 and is_square(d2):
                    return (a, b, c, int(math.isqrt(d2)))
    return None

# Check achievable via splitting method
# From n^2 = a^2 + b^2, replace a^2 by (a-t)^2 + ones, then merge.
def achievable_splitting(n, k):
    """Check if n^2 is sum of k positive squares using splitting from 2-square rep."""
    rep2 = find_two_squares(n)
    if rep2 is None:
        return False
    a, b = max(rep2), min(rep2)
    # Use the larger square for splitting
    # k = 2 + 2*a*t - t^2 for t = 0..a-1, then merge ones
    # Also try splitting from 3-square rep
    reps = []
    reps.append(('2sq', a, b))  # a^2 + b^2
    rep3 = find_three_squares(n)
    if rep3:
        reps.append(('3sq', max(rep3), sorted(rep3, reverse=True)))
    rep4 = find_four_squares(n)
    if rep4:
        reps.append(('4sq', max(rep4), sorted(rep4, reverse=True)))

    for rep in reps:
        if rep[0] == '2sq':
            big = rep[1]
            small_terms = [rep[2]]  # the other square
            base_k = 1 + 1  # big^2 + small^2
            for t in range(0, big):
                # Replace big^2 by (big-t)^2 + (2*big*t - t^2) ones
                if t == 0:
                    kt = base_k  # = 2
                    num_ones = 0
                else:
                    num_ones = 2 * big * t - t * t
                    if num_ones <= 0:
                        continue
                    kt = 1 + len(small_terms) + 1 + num_ones - 1  # (big-t)^2 + small_terms + num_ones ones
                    kt = 1 + len(small_terms) + num_ones  # (big-t)^2 is 1 term, small_terms are len(small_terms), ones are num_ones
                # From kt, can decrease by 3a+8b with 4a+9b <= num_ones
                e_needed = kt - k
                if e_needed < 0:
                    continue
                if e_needed == 0:
                    return True
                # Check if e_needed = 3a+8b with 4a+9b <= num_ones
                bb = 0
                while 8 * bb <= e_needed:
                    rem = e_needed - 8 * bb
                    if rem % 3 == 0:
                        aa = rem // 3
                        if 4 * aa + 9 * bb <= num_ones:
                            return True
                    bb += 1
        elif rep[0] == '3sq':
            big = rep[1]
            small_terms = [x for x in rep[2] if x != big]
            for t in range(0, big):
                if t == 0:
                    kt = 3
                    num_ones = 0
                else:
                    num_ones = 2 * big * t - t * t
                    if num_ones <= 0:
                        continue
                    kt = 1 + len(small_terms) + num_ones
                e_needed = kt - k
                if e_needed < 0:
                    continue
                if e_needed == 0:
                    return True
                bb = 0
                while 8 * bb <= e_needed:
                    rem = e_needed - 8 * bb
                    if rem % 3 == 0:
                        aa = rem // 3
                        if 4 * aa + 9 * bb <= num_ones:
                            return True
                    bb += 1
        elif rep[0] == '4sq':
            big = rep[1]
            small_terms = [x for x in rep[2] if x != big]
            for t in range(0, big):
                if t == 0:
                    kt = 4
                    num_ones = 0
                else:
                    num_ones = 2 * big * t - t * t
                    if num_ones <= 0:
                        continue
                    kt = 1 + len(small_terms) + num_ones
                e_needed = kt - k
                if e_needed < 0:
                    continue
                if e_needed == 0:
                    return True
                bb = 0
                while 8 * bb <= e_needed:
                    rem = e_needed - 8 * bb
                    if rem % 3 == 0:
                        aa = rem // 3
                        if 4 * aa + 9 * bb <= num_ones:
                            return True
                    bb += 1
    return False

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
    # Defect method
    if is_representable(e):
        ms = min_summands(e)
        if ms is not None and ms <= k: return True
    # Direct search for small k
    if k <= 100:
        if is_sum_k_pos_squares_bounded(N, k, n): return True
    # Splitting method for intermediate k
    if achievable_splitting(n, k): return True
    return False

def check_S(n):
    N = n * n
    target = N - 14
    for k in range(1, target + 1):
        if not achievable(n, k):
            return False, k
    if achievable(n, N - 13):
        return False, N - 13
    return True, None

# Test on the "k=201 failure" cases
test_ns = [45, 50, 51, 52, 53, 55, 58, 60, 61, 65, 68, 70]
for n in test_ns:
    ok, fail = check_S(n)
    if ok:
        print(f"n={n}: S(n) = n^2 - 14 = {n*n-14}  *** WORKS ***")
    else:
        print(f"n={n}: fails at k={fail}")

# Also verify 2n pattern: if n works, 2n works
print("\n=== 2n pattern ===")
base_working = [13, 15, 17, 25, 29, 35, 37, 39, 41]
for n in base_working:
    n2 = 2 * n
    ok, fail = check_S(n2)
    print(f"n={n} -> 2n={n2}: {'WORKS' if ok else 'FAILS at k=' + str(fail)}")
