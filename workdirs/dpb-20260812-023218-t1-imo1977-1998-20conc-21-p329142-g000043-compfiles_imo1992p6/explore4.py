"""Compute exact defect method coverage for n=13."""
import math

def is_representable(e):
    if e < 0: return False
    if e == 0: return True
    b = 0
    while 8 * b <= e:
        if (e - 8 * b) % 3 == 0: return True
        b += 1
    return False

def min_summands(e):
    """Minimum a+b such that 3a+8b = e, a,b >= 0."""
    if e == 0: return 0
    if not is_representable(e): return None
    best = None
    # Try b from e//8 down to 0, find first that works (gives min a+b since 8>3)
    for b in range(e // 8, -1, -1):
        rem = e - 8 * b
        if rem % 3 == 0:
            a = rem // 3
            return a + b  # first found from top is minimum
    return None

n = 13
N = 169

# For each k from 1 to 155, check if defect method works
defect_covered = set()
defect_not_covered = set()
for k in range(1, N - 13):
    e = N - k
    if is_representable(e):
        ms = min_summands(e)
        if ms is not None and ms <= k:
            defect_covered.add(k)
        else:
            defect_not_covered.add(k)
    else:
        defect_not_covered.add(k)  # e not representable

print(f"Defect method covers k in: {sorted(defect_covered)[:20]}...{sorted(defect_covered)[-5:]}")
print(f"Defect method does NOT cover: {sorted(defect_not_covered)}")
print(f"Defect covers {len(defect_covered)} values, misses {len(defect_not_covered)} values")

# Now check which of the missed values are covered by splitting method
# From 169 = 5^2 + 12^2, split 12^2
print("\n=== Splitting from 169 = 5^2 + 12^2 ===")
a, b = 12, 5  # split the larger one
split_covered = set()
for t in range(0, a):  # replace 12^2 by (12-t)^2 + (24t - t^2) ones
    num_ones = 2 * a * t - t * t if t > 0 else 0
    if t == 0:
        kt = 2  # 12^2 + 5^2
    else:
        if num_ones <= 0:
            continue
        kt = 1 + 1 + num_ones  # (12-t)^2 + 5^2 + num_ones ones
    # From kt, decrease by 3a+8b with 4a+9b <= num_ones
    for bb in range(num_ones // 9 + 1):
        for aa in range((num_ones - 9 * bb) // 4 + 1):
            if 4 * aa + 9 * bb <= num_ones:
                dec = 3 * aa + 8 * bb
                k = kt - dec
                if k >= 1:
                    split_covered.add(k)
    # Also can increase by splitting 5^2 or (12-t)^2 further, but let's keep it simple

print(f"Splitting (from 2sq) covers: {sorted(split_covered)[:20]}...{sorted(split_covered)[-5:]}")
print(f"Splitting covers {len(split_covered)} values")

# Also split from 169 = 3^2 + 4^2 + 12^2 (k=3)
print("\n=== Splitting from 169 = 3^2 + 4^2 + 12^2 ===")
a = 12
split3_covered = set()
for t in range(0, a):
    num_ones = 2 * a * t - t * t if t > 0 else 0
    if t == 0:
        kt = 3
    else:
        if num_ones <= 0:
            continue
        kt = 1 + 2 + num_ones  # (12-t)^2 + 3^2 + 4^2 + num_ones ones
    for bb in range(num_ones // 9 + 1):
        for aa in range((num_ones - 9 * bb) // 4 + 1):
            if 4 * aa + 9 * bb <= num_ones:
                dec = 3 * aa + 8 * bb
                k = kt - dec
                if k >= 1:
                    split3_covered.add(k)

print(f"Splitting (from 3sq) covers: {sorted(split3_covered)[:20]}...{sorted(split3_covered)[-5:]}")
print(f"Splitting (from 3sq) covers {len(split3_covered)} values")

# Also from 169 = 11^2 + 4^2 + 4^2 + 4^2 (k=4)
print("\n=== Splitting from 169 = 11^2 + 4^2 + 4^2 + 4^2 ===")
a = 11
split4_covered = set()
for t in range(0, a):
    num_ones = 2 * a * t - t * t if t > 0 else 0
    if t == 0:
        kt = 4
    else:
        if num_ones <= 0:
            continue
        kt = 1 + 3 + num_ones  # (11-t)^2 + 3*4^2 + num_ones ones
    for bb in range(num_ones // 9 + 1):
        for aa in range((num_ones - 9 * bb) // 4 + 1):
            if 4 * aa + 9 * bb <= num_ones:
                dec = 3 * aa + 8 * bb
                k = kt - dec
                if k >= 1:
                    split4_covered.add(k)

print(f"Splitting (from 4sq) covers: {sorted(split4_covered)[:20]}...{sorted(split4_covered)[-5:]}")
print(f"Splitting (from 4sq) covers {len(split4_covered)} values")

# Union of all methods
all_covered = defect_covered | split_covered | split3_covered | split4_covered
# Add k=1 (13^2), k=N (all ones)
all_covered.add(1)
all_covered.add(N)

needed = set(range(1, N - 13))  # k from 1 to 155
missing = needed - all_covered
print(f"\n=== Summary ===")
print(f"Total needed: {len(needed)} (k from 1 to {N-14})")
print(f"Total covered: {len(all_covered & needed)}")
print(f"Missing: {sorted(missing)}")
