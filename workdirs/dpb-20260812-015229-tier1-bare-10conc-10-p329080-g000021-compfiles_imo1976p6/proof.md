# IMO 1976 Problem 6 — Solution

## Problem

The sequence $u_0, u_1, u_2, \ldots$ is defined by
$$u_0 = 2,\qquad u_1 = \tfrac{5}{2},\qquad u_{n+1} = u_n\bigl(u_{n-1}^2 - 2\bigr) - u_1 \quad (n \ge 1).$$
Prove that $\lfloor u_n \rfloor = 2^{(2^n - (-1)^n)/3}$ for all positive $n$.

## Key idea

Define
$$b_n = \frac{2^n - (-1)^n}{3}\qquad(n \ge 0).$$
We claim that for every $n \ge 0$,
$$\boxed{\,u_n = 2^{b_n} + 2^{-b_n}\,} \tag{$\star$}$$
and that $b_n$ is a non-negative integer with $b_n \ge 1$ for $n \ge 1$. Since $0 < 2^{-b_n} < 1$ whenever $b_n \ge 1$, this immediately gives
$$\lfloor u_n \rfloor = 2^{b_n} = 2^{(2^n-(-1)^n)/3},$$
which is exactly the desired formula.

## Step 1. $b_n$ is a non-negative integer, and $b_n \ge 1$ for $n \ge 1$

Since $2 \equiv -1 \pmod{3}$, we have $2^n \equiv (-1)^n \pmod{3}$, so $3 \mid \bigl(2^n - (-1)^n\bigr)$; hence $b_n \in \mathbb{Z}$.

For $n \ge 1$: $2^n - (-1)^n \ge 2^n - 1 \ge 1$, so $b_n \ge 1$. Also $b_0 = (1-1)/3 = 0$.

## Step 2. Two identities for $b_n$

**Identity A:** $\;b_n + 2b_{n-1} = b_{n+1}$.

*Proof.* Using $(-1)^{n-1} = -(-1)^n$,
$$b_{n-1} = \frac{2^{n-1} - (-1)^{n-1}}{3} = \frac{2^{n-1} + (-1)^n}{3},\qquad 2b_{n-1} = \frac{2^n + 2(-1)^n}{3}.$$
Therefore
$$b_n + 2b_{n-1} = \frac{2^n - (-1)^n + 2^n + 2(-1)^n}{3} = \frac{2^{n+1} + (-1)^n}{3}.$$
On the other hand $(-1)^{n+1} = -(-1)^n$, so
$$b_{n+1} = \frac{2^{n+1} - (-1)^{n+1}}{3} = \frac{2^{n+1} + (-1)^n}{3}.$$
Hence $b_n + 2b_{n-1} = b_{n+1}$. $\square$

**Identity B:** $\;b_n - 2b_{n-1} = -(-1)^n$, i.e. $\bigl|b_n - 2b_{n-1}\bigr| = 1$.

*Proof.*
$$b_n - 2b_{n-1} = \frac{2^n - (-1)^n - 2^n - 2(-1)^n}{3} = \frac{-3(-1)^n}{3} = -(-1)^n. \qquad\square$$

Consequently:
- if $n$ is odd, $b_n - 2b_{n-1} = 1$ and $-b_n + 2b_{n-1} = -1$;
- if $n$ is even, $b_n - 2b_{n-1} = -1$ and $-b_n + 2b_{n-1} = 1$.

In **both** cases the pair of "cross exponents" $\{b_n - 2b_{n-1},\; -b_n + 2b_{n-1}\}$ equals $\{1, -1\}$.

## Step 3. The recurrence preserves $(\star)$

Assume $(\star)$ holds for $u_n$ and $u_{n-1}$ (with $n \ge 1$). We prove it for $u_{n+1}$.

From $u_{n-1} = 2^{b_{n-1}} + 2^{-b_{n-1}}$ we get
$$u_{n-1}^2 - 2 = 2^{2b_{n-1}} + 2 + 2^{-2b_{n-1}} - 2 = 2^{2b_{n-1}} + 2^{-2b_{n-1}}.$$

Then
$$
\begin{aligned}
u_n\bigl(u_{n-1}^2 - 2\bigr)
&= \bigl(2^{b_n} + 2^{-b_n}\bigr)\bigl(2^{2b_{n-1}} + 2^{-2b_{n-1}}\bigr)\\
&= 2^{b_n + 2b_{n-1}} + 2^{b_n - 2b_{n-1}} + 2^{-b_n + 2b_{n-1}} + 2^{-b_n - 2b_{n-1}}.
\end{aligned}
$$

By Identity A, $b_n + 2b_{n-1} = b_{n+1}$, so the first and last terms are $2^{b_{n+1}}$ and $2^{-b_{n+1}}$. By Identity B (and the discussion following it), the two middle terms are $2^{1} + 2^{-1} = \tfrac{5}{2} = u_1$. Hence
$$u_n\bigl(u_{n-1}^2 - 2\bigr) = 2^{b_{n+1}} + 2^{-b_{n+1}} + u_1.$$

Subtracting $u_1$ as the recurrence dictates,
$$u_{n+1} = u_n\bigl(u_{n-1}^2 - 2\bigr) - u_1 = 2^{b_{n+1}} + 2^{-b_{n+1}},$$
which is $(\star)$ for $n+1$. $\square$

## Step 4. Base cases

$b_0 = 0,\; b_1 = 1$, so
$$2^{b_0} + 2^{-b_0} = 1 + 1 = 2 = u_0,\qquad 2^{b_1} + 2^{-b_1} = 2 + \tfrac{1}{2} = \tfrac{5}{2} = u_1.$$
Thus $(\star)$ holds for $n=0,1$, and by Step 3 it holds for all $n \ge 0$ by induction.

## Step 5. Conclusion

For every $n \ge 1$, $b_n$ is a positive integer (Step 1), so $0 < 2^{-b_n} < 1$ and $2^{b_n}$ is an integer. Therefore
$$\lfloor u_n \rfloor = \Bigl\lfloor 2^{b_n} + 2^{-b_n}\Bigr\rfloor = 2^{b_n} = 2^{(2^n - (-1)^n)/3}.$$

$\blacksquare$ (QED)

## Verification (numerical)

| $n$ | $b_n$ | $u_n$ (exact) | $\lfloor u_n\rfloor$ | $2^{b_n}$ |
|---|---|---|---|---|
| 1 | 1 | $5/2$ | 2 | 2 |
| 2 | 1 | $5/2$ | 2 | 2 |
| 3 | 3 | $65/8$ | 8 | 8 |
| 4 | 5 | $1025/32$ | 32 | 32 |
| 5 | 11 | $4194305/2048$ | 2048 | 2048 |
| 6 | 21 | $4398046511105/2097152$ | 2097152 | 2097152 |
| 7 | 43 | $77371252455336267181195265/8796093022208$ | 8796093022208 | 8796093022208 |

All entries match $u_n = 2^{b_n} + 2^{-b_n}$ and $\lfloor u_n\rfloor = 2^{b_n}$, confirming the proof.
