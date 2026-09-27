"""
Explore the functional equation f(f(n)) = f(n) + n, f(1)=2, f strictly increasing.

Strategy: greedy construction. At each position n, if f(n) is forced by the
functional equation, use that. Otherwise, pick the smallest valid value
that maintains strict monotonicity and doesn't create contradictions.
"""

def construct_f(N, verbose=False):
    """
    Try to construct f(1..N) greedily.
    f is a dict: n -> f(n).
    forced: dict of n -> f(n) that are forced by the functional equation.
    """
    f = {}
    # f(1) = 2 is given
    f[1] = 2

    # Process: at each n from 1 to N, if f(n) is known, derive f(f(n)) = f(n) + n.
    # If f(n) is not known, pick the smallest value > f(n-1) that is consistent.

    changed = True
    while changed:
        changed = False
        # Propagate forced values
        for n in sorted(f.keys()):
            fn = f[n]
            target_idx = fn  # f(f(n)) = f(n) + n
            target_val = fn + n
            if target_idx <= N:
                if target_idx in f:
                    if f[target_idx] != target_val:
                        return None, f"Contradiction: f({target_idx}) should be {target_val} but is {f[target_idx]}"
                else:
                    f[target_idx] = target_val
                    changed = True

    # Now fill in gaps greedily
    for n in range(1, N+1):
        if n in f:
            continue
        # Find smallest value for f(n) that is > f(n-1) and < f(n+1) if f(n+1) known
        lo = f.get(n-1, 0) + 1  # must be > f(n-1)
        # Check upper bound from next known f value
        hi = None
        for m in range(n+1, N+1):
            if m in f:
                hi = f[m] - (m - n)  # f(n) < f(m) - (m-n) + 1, i.e. f(n) <= f(m) - (m-n) - 1 + 1
                # Actually f(n) < f(n+1) < ... < f(m), so f(n) < f(m) - (m - n)
                # So f(n) <= f(m) - (m - n) - 1
                hi = f[m] - (m - n) - 1
                break
        if hi is not None and lo > hi:
            return None, f"Cannot fill f({n}): need > {lo-1} and <= {hi}, contradiction"

        # Pick smallest value = lo
        val = lo
        f[n] = val
        changed = True

        # Propagate
        while changed:
            changed = False
            for k in sorted(f.keys()):
                fk = f[k]
                tidx = fk
                tval = fk + k
                if tidx <= N:
                    if tidx in f:
                        if f[tidx] != tval:
                            return None, f"Contradiction: f({tidx}) should be {tval} but is {f[tidx]} (from f({k})={fk})"
                    else:
                        f[tidx] = tval
                        changed = True

    # Verify
    for n in range(1, N+1):
        if f[n] <= N:
            if f.get(f[n]) is not None:
                if f[f[n]] != f[n] + n:
                    return None, f"Verification failed: f(f({n})) = f({f[n]}) = {f[f[n]]} != {f[n]+n}"
    for n in range(1, N):
        if f[n+1] <= f[n]:
            return None, f"Not increasing: f({n})={f[n]} >= f({n+1})={f[n+1]}"

    return f, "OK"


def main():
    for N in [20, 50, 100, 200, 500]:
        f, msg = construct_f(N)
        if f is None:
            print(f"N={N}: FAILED - {msg}")
            break
        vals = [f[n] for n in range(1, N+1)]
        print(f"N={N}: OK")
        if N <= 50:
            print(f"  f(1..{N}) = {vals}")
            diffs = [vals[i+1]-vals[i] for i in range(len(vals)-1)]
            print(f"  diffs     = {diffs}")

    # Check the range and complement
    N = 200
    f, msg = construct_f(N)
    if f:
        S = set(f[n] for n in range(1, N+1) if f[n] <= 1000)
        comp = set(range(1, max(S)+1)) - S
        print(f"\nRange S (first 30): {sorted(S)[:30]}")
        print(f"Complement (first 30): {sorted(comp)[:30]}")

        # Check ratio f(n)/n
        print(f"\nf(n)/n for n=10,50,100,200: {f[10]/10:.4f}, {f[50]/50:.4f}, {f[100]/100:.4f}, {f[200]/200:.4f}")
        print(f"phi = {(1+5**0.5)/2:.4f}")

        # Check if range matches Beatty sequence
        import math
        phi = (1+math.sqrt(5))/2
        beatty_phi = set(int(n*phi) for n in range(1, 200))
        beatty_phi2 = set(int(n*phi**2) for n in range(1, 200))
        S_set = set(f[n] for n in range(1, N+1))
        print(f"\n|S ∩ Beatty(phi)| = {len(S_set & beatty_phi)}, |S \\ Beatty(phi)| = {len(S_set - beatty_phi)}")
        print(f"S - Beatty(phi) (first 20): {sorted(S_set - beatty_phi)[:20]}")
        print(f"Beatty(phi) - S (first 20): {sorted(beatty_phi - S_set)[:20]}")

if __name__ == "__main__":
    main()
