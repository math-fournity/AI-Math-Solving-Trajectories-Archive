import sympy
import math

# Verify n=8715 and n=8714 independently using sympy.primepi
for n in [8713, 8714, 8715, 8716]:
    lo = n*n
    hi = (n+1)**2
    count = sympy.primepi(hi) - sympy.primepi(lo)
    print(f"n={n}: pi({hi}) - pi({lo}) = {count}  [interval ({lo},{hi})]")

# Also double-check no earlier n reaches 1000 by scanning a window below 8715
print("\nScanning n=8700..8715:")
for n in range(8700, 8716):
    lo = n*n
    hi = (n+1)**2
    count = sympy.primepi(hi) - sympy.primepi(lo)
    print(f"  n={n}: {count}")
