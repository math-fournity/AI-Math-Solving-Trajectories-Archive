"""
Test the Fibonacci successor function as a solution to f(f(n)) = f(n) + n.

The Fibonacci successor s(n): write n in Zeckendorf representation
n = F_{i1} + F_{i2} + ... + F_{ik} (non-consecutive Fibonacci numbers, indices >= 2),
then s(n) = F_{i1+1} + F_{i2+1} + ... + F_{ik+1}.

Key identity: F_{j+1} + F_j = F_{j+2}, so s(s(n)) = s(n) + n.
"""

def fib_list(upto):
    """Generate Fibonacci numbers F_1=1, F_2=1, F_3=2, ... up to <= upto."""
    fibs = [0, 1, 1]  # F_0=0, F_1=1, F_2=1
    while fibs[-1] <= upto:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def zeckendorf(n):
    """Return list of indices (>= 2) in Zeckendorf representation of n."""
    fibs = fib_list(n)
    indices = []
    i = len(fibs) - 1
    while i >= 2 and n > 0:
        if fibs[i] <= n:
            indices.append(i)
            n -= fibs[i]
            i -= 2  # skip next (non-consecutive)
        else:
            i -= 1
    return indices

def fib_successor(n):
    """Apply Fibonacci successor: shift all Zeckendorf indices up by 1."""
    indices = zeckendorf(n)
    fibs = fib_list(n * 3)  # enough room
    return sum(fibs[i+1] for i in indices)

def verify(N):
    """Verify Fibonacci successor satisfies all conditions up to N."""
    f = {n: fib_successor(n) for n in range(1, N+1)}
    
    # Condition i: f(1) = 2
    assert f[1] == 2, f"f(1) = {f[1]} != 2"
    
    # Condition ii: f(f(n)) = f(n) + n for all n
    for n in range(1, N+1):
        fn = f[n]
        # Need f(fn), which requires fn to be in range or compute directly
        ffn = fib_successor(fn)
        assert ffn == fn + n, f"f(f({n})) = f({fn}) = {ffn} != {fn}+{n}={fn+n}"
    
    # Condition iii: f(n+1) > f(n) for all n
    for n in range(1, N):
        assert f[n+1] > f[n], f"f({n+1})={f[n+1]} <= f({n})={f[n]}"
    
    print(f"All conditions verified for n = 1..{N}")
    
    # Show first 20 values
    vals = [f[n] for n in range(1, 21)]
    print(f"f(1..20) = {vals}")
    
    # Show some Zeckendorf representations and their successors
    print("\nZeckendorf representations and successors:")
    for n in range(1, 16):
        z = zeckendorf(n)
        fn = f[n]
        zf = zeckendorf(fn)
        fibs = fib_list(100)
        z_str = " + ".join(f"F_{i}({fibs[i]})" for i in z)
        zf_str = " + ".join(f"F_{i}({fibs[i]})" for i in zf)
        print(f"  {n:3d} = {z_str:30s} -> f(n) = {fn:3d} = {zf_str}")
    
    # Check ratio
    print(f"\nf(n)/n: f(100)/100 = {f[100]/100:.6f}, phi = {(1+5**0.5)/2:.6f}")
    
    # Compare with greedy solution
    print("\nComparison with greedy (first 20):")
    greedy = [2, 3, 5, 6, 8, 10, 11, 13, 14, 16, 18, 19, 21, 23, 24, 26, 27, 29, 31, 32]
    successor = [f[n] for n in range(1, 21)]
    print(f"  Greedy:    {greedy}")
    print(f"  Successor: {successor}")
    print(f"  Same? {greedy == successor}")

verify(1000)
