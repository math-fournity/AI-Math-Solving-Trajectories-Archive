# Problem

Find (in closed form) the difference between the number of positive integers at most $2^{2017}$ with even weight and the number of positive integers at most $2^{2017}$ with odd weight.

Here, the **weight** of a positive integer is the number of $1$s in its binary representation (Hamming weight / popcount).

## Answer

$$\boxed{-2}$$

## Proof

### Setup and notation

For a positive integer $m$, define $w(m) = \text{number of 1s in the binary representation of } m$. We say $m$ has **even weight** if $w(m)$ is even, and **odd weight** if $w(m)$ is odd.

We seek:
$$D = \#\{m : 1 \le m \le 2^{2017},\; w(m) \text{ even}\} - \#\{m : 1 \le m \le 2^{2017},\; w(m) \text{ odd}\}.$$

### Key lemma

**Lemma.** *For any $n \ge 1$, among the integers $\{0, 1, 2, \ldots, 2^n - 1\}$, exactly $2^{n-1}$ have even weight and exactly $2^{n-1}$ have odd weight.*

**Proof of Lemma.** Every integer in $\{0, 1, \ldots, 2^n - 1\}$ can be uniquely represented as an $n$-bit binary string (padding with leading zeros as needed). Consider the map $\phi$ that flips the last bit of an $n$-bit string. This is a bijection on the set of $n$-bit strings, and it changes the weight by exactly $\pm 1$, thus toggling the parity of the weight. Therefore $\phi$ pairs every even-weight string with a unique odd-weight string, proving the counts are equal. Since there are $2^n$ strings total, each count is $2^{n-1}$. $\square$

### Applying the lemma

**Step 1: Numbers from $0$ to $2^{2017} - 1$.**

By the Lemma with $n = 2017$:
- Even weight count: $2^{2016}$
- Odd weight count: $2^{2016}$

Note that $0$ (represented as $00\ldots0$) has weight $0$, which is even.

**Step 2: The number $2^{2017}$.**

The number $2^{2017}$ in binary is $1\underbrace{00\ldots0}_{2017 \text{ zeros}}$, so $w(2^{2017}) = 1$, which is **odd**.

**Step 3: Restrict to positive integers.**

The positive integers at most $2^{2017}$ are $\{1, 2, \ldots, 2^{2017}\}$, which equals $\{0, 1, \ldots, 2^{2017}\} \setminus \{0\}$.

From Step 1, among $\{0, 1, \ldots, 2^{2017}-1\}$:
- Even weight: $2^{2016}$ (including $0$)
- Odd weight: $2^{2016}$

Removing $0$ (which has even weight):
- Even weight positive integers in $\{1, \ldots, 2^{2017}-1\}$: $2^{2016} - 1$
- Odd weight positive integers in $\{1, \ldots, 2^{2017}-1\}$: $2^{2016}$

**Step 4: Add $2^{2017}$.**

Since $w(2^{2017}) = 1$ is odd:
- Total even weight count: $2^{2016} - 1$
- Total odd weight count: $2^{2016} + 1$

### Final computation

$$D = \underbrace{(2^{2016} - 1)}_{\text{even weight}} - \underbrace{(2^{2016} + 1)}_{\text{odd weight}} = -2.$$

### Numerical verification

For small values of $n$, direct computation confirms:

| $n$ | $2^n$ | Even weight count | Odd weight count | Difference |
|-----|-------|--------------------|-------------------|------------|
| 1   | 2     | 0                  | 2                 | $-2$       |
| 2   | 4     | 1                  | 3                 | $-2$       |
| 3   | 8     | 3                  | 5                 | $-2$       |
| 4   | 16    | 7                  | 9                 | $-2$       |
| 5   | 32    | 15                 | 17                | $-2$       |
| 6   | 64    | 31                 | 33                | $-2$       |
| 7   | 128   | 63                 | 65                | $-2$       |

The pattern holds universally, independent of $n$.

### Conclusion

The difference between the number of positive integers at most $2^{2017}$ with even weight and the number with odd weight is:

$$\boxed{-2}$$

QED.
