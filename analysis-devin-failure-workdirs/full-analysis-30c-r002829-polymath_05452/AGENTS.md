# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Find all $n > 1$, $n \in \mathbb{N}$ such that for all $a \in \mathbb{N}$, if $a^n - 1$ is divisible by $n$, then $a^n - 1$ is also divisible by $n^2$.
Let $S$ be the set of all such values of $n$. Calculate the sum of all $n \in S$ such that $1 < n \le 20$.       — 题目文本
#   From the original solution, the numbers $n$ that satisfy the condition are square-free integers greater than 1 and $n = 4$.
Square-free numbers are those whose prime factorization contains no repeated factors.
For $1 < n \le 20$, the square-free numbers are: 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19.
Additionally, the number $n = 4$ is identified as a solution.
We sum these values: $2 + 3 + 4 + 5 + 6 + 7 + 10 + 11 + 13 + 14 + 15 + 17 + 19 = 126$.  — 标准解答
#   Let me analyze the problem carefully.

We need to find all $n > 1$, $n \in \mathbb{N}$ such that: for all $a \in \mathbb{N}$, if $n \mid a^n - 1$, then $n^2 \mid a^n - 1$.

Let me check for answer leaks first. The problem text doesn't contain any leaked answers or solutions. Good.

Now let me think about this problem. We need $n$ such that for all $a$, $n \mid a^n - 1 \implies n^2 \mid a^n - 1$.

First, note that $a$ ranges over all natural numbers. Let me think about what conditions this imposes.

Let's consider $n$ with prime factorization $n = p_1^{e_1} \cdots p_k^{e_k}$.

The condition $n \mid a^n - 1$ means $p_i^{e_i} \mid a^n - 1$ for all $i$.

The condition $n^2 \mid a^n - 1$ means $p_i^{2e_i} \mid a^n - 1$ for all $i$.

So we need: for all $a$, if $p_i^{e_i} \mid a^n - 1$ for all $i$, then $p_i^{2e_i} \mid a^n - 1$ for all $i$.

Let me think about this differently. Let's consider specific values of $a$.

First, consider $a$ such that $\gcd(a, n) = 1$. Then by Euler's theorem, $a^{\phi(n)} \equiv 1 \pmod{n}$, but we need $a^n \equiv 1 \pmod{n}$.

Actually, let's think about when $n \mid a^n - 1$ can happen. If $\gcd(a, n) > 1$, say $p \mid a$ and $p \mid n$, then $a^n \equiv 0 \pmod{p}$, so $a^n - 1 \equiv -1 \pmod{p}$, which means $p \nmid a^n - 1$, so $n \nmid a^n - 1$. So the condition $n \mid a^n - 1$ automatically implies $\gcd(a, n) = 1$.

So we only need to consider $a$ with $\gcd(a, n) = 1$.

Now, the condition becomes: for all $a$ with $\gcd(a, n) = 1$, if $a^n \equiv 1 \pmod{n}$, then $a^n \equiv 1 \pmod{n^2}$.

Hmm, but actually we need it for ALL $a \in \mathbb{N}$, and as shown, only $a$ with $\gcd(a, n) = 1$ can satisfy $n \mid a^n - 1$.

So the condition is: for all $a$ coprime to $n$, $a^n \equiv 1 \pmod{n} \implies a^n \equiv 1 \pmod{n^2}$.

Let me think about this using the structure of $(\mathbb{Z}/n^2\mathbb{Z})^*$.

Actually, let me think about it more carefully. We need: for all $a$ coprime to $n$, if $a^n \equiv 1 \pmod{n}$, then $a^n \equiv 1 \pmod{n^2}$.

Let me consider the map $\phi: (\mathbb{Z}/n^2\mathbb{Z})^* \to (\mathbb{Z}/n\mathbb{Z})^*$, the natural reduction mod $n$. The kernel of this map has order $n^2 \cdot \frac{\phi(n)}{\phi(n)} / ... $ wait let me think again.

$|(\mathbb{Z}/n^2\mathbb{Z})^*| = \phi(n^2)$ and $|(\mathbb{Z}/n\mathbb{Z})^*| = \phi(n)$. The reduction map is surjective, and the kernel has order $\phi(n^2)/\phi(n)$.

For $n = p_1^{e_1} \cdots p_k^{e_k}$, $\phi(n^2)/\phi(n) = \prod p_i^{e_i} = n$.

So the kernel $K$ of the reduction map has order $n$.

Now, the condition is: for every $a$ coprime to $n$ with $a^n \equiv 1 \pmod{n}$, we need $a^n \equiv 1 \pmod{n^2}$.

In terms of the group structure: let $\bar{a}$ be the image of $a$ in $(\mathbb{Z}/n^2\mathbb{Z})^*$. The condition $a^n \equiv 1 \pmod{n}$ means $\bar{a}^n \in K$ (the kernel). The condition $a^n \equiv 1 \pmod{n^2}$ means $\bar{a}^n = 1$ in $(\mathbb{Z}/n^2\mathbb{Z})^*$.

So the condition is: for all $\bar{a} \in (\mathbb{Z}/n^2\mathbb{Z})^*$, if $\bar{a}^n \in K$, then $\bar{a}^n = 1$.

In other words, the map $f: (\mathbb{Z}/n^2\mathbb{Z})^* \to K$ given by $f(\bar{a}) = \bar{a}^n$ should satisfy: $\ker(f) = \{\bar{a} : \bar{a}^n = 1\}$ equals $\{\bar{a} : \bar{a}^n \in K\}$... no wait.

Let me rephrase. The set of $\bar{a}$ with $\bar{a}^n \in K$ is $f^{-1}(K) = \{\bar{a} : \bar{a}^n \in K\}$. But $\bar{a}^n \in K$ iff $\bar{a}^n \equiv 1 \pmod{n}$, which is always... no. $\bar{a}^n \in K$ means $\bar{a}^n \equiv 1 \pmod{n}$, i.e., $a^n \equiv 1 \pmod n$.

Hmm wait, $K$ is the kernel of reduction mod $n$, so $K = \{x \in (\mathbb{Z}/n^2\mathbb{Z})^* : x \equiv 1 \pmod{n}\}$. So $\bar{a}^n \in K$ iff $\bar{a}^n \equiv 1 \pmod n$.

And the condition is: $\bar{a}^n \in K \implies \bar{a}^n = 1$ (in $(\mathbb{Z}/n^2\mathbb{Z})^*$).

So the image of the $n$-th power map, restricted to those elements whose $n$-th power lands in $K$, must be trivial. Equivalently, the only element of $K$ that is an $n$-th power in $(\mathbb{Z}/n^2\mathbb{Z})^*$ is the identity.

So: $K \cap \{n\text{-th powers in } (\mathbb{Z}/n^2\mathbb{Z})^*\} = \{1\}$.

Let me think about this differently. Consider the $n$-th power map on $(\mathbb{Z}/n^2\mathbb{Z})^*$. The image is the subgroup of $n$-th powers. We need this image to intersect $K$ trivially.

Since $|K| = n$, and the image of the $n$-th power map has size $|(\mathbb{Z}/n^2\mathbb{Z})^*| / |\ker(\text{$n$-th power})| = \phi(n^2) / d$ where $d = |\{x : x^n = 1\}|$.

Hmm, this is getting complicated. Let me try a more direct approach and just check small values.

Let me check $n = 2$ through $n = 20$.

For each $n$, I need: for all $a$ coprime to $n$, $a^n \equiv 1 \pmod n \implies a^n \equiv 1 \pmod{n^2}$.

**$n = 2$**: Need: for all odd $a$, $a^2 \equiv 1 \pmod 2 \implies a^2 \equiv 1 \pmod 4$. For odd $a$, $a^2 \equiv 1 \pmod 8$ (since odd squares are $\equiv 1 \pmod 8$), so certainly $a^2 \equiv 1 \pmod 4$. And $a^2 \equiv 1 \pmod 2$ is always true for odd $a$. So the condition holds. $n = 2 \in S$.

Wait, but I need to be more careful. The condition is for ALL $a \in \mathbb{N}$, if $n \mid a^n - 1$ then $n^2 \mid a^n - 1$. For $n = 2$: if $2 \mid a^2 - 1$, then $4 \mid a^2 - 1$. $2 \mid a^2 - 1$ iff $a$ is odd. For odd $a$, $a^2 \equiv 1 \pmod 8$, so $4 \mid a^2 - 1$. ✓. So $n = 2 \in S$.

**$n = 3$**: Need: if $3 \mid a^3 - 1$, then $9 \mid a^3 - 1$. $3 \mid a^3 - 1$ iff $a \equiv 1 \pmod 3$ (since $a^3 \equiv a \pmod 3$ by Fermat). So $a \equiv 1 \pmod 3$. Then $a = 3k + 1$. $a^3 = 27k^3 + 27k^2 + 9k + 1$, so $a^3 - 1 = 9k(3k^2 + 3k + 1)$. So $9 \mid a^3 - 1$. ✓. So $n = 3 \in S$.

**$n = 4$**: Need: if $4 \mid a^4 - 1$, then $16 \mid a^4 - 1$. $4 \mid a^4 - 1$ requires $a$ odd (since if $a$ even, $a^4 - 1$ is odd, not divisible by 2, let alone 4). For odd $a$, $a^4 \equiv 1 \pmod{16}$? Let's check: $a = 1$: $1 - 1 = 0$, $16 \mid 0$. ✓. $a = 3$: $3^4 = 81$, $81 - 1 = 80$, $16 \mid 80$? $80/16 = 5$. ✓. $a = 5$: $5^4 = 625$, $625 - 1 = 624$, $624/16 = 39$. ✓. Actually, for odd $a$, $a^2 \equiv 1 \pmod 8$, so $a^4 \equiv 1 \pmod{16}$... let me verify. $a = 2k+1$, $a^2 = 4k^2 + 4k + 1 = 4k(k+1) + 1$. Since $k(k+1)$ is even, $a^2 = 8m + 1$ for some $m$. Then $a^4 = (8m+1)^2 = 64m^2 + 16m + 1 = 16(4m^2 + m) + 1$. So $a^4 \equiv 1 \pmod{16}$. ✓. So for all odd $a$, $16 \mid a^4 - 1$. And $4 \mid a^4 - 1$ is automatic for odd $a$. So $n = 4 \in S$.

**$n = 5$**: Need: if $5 \mid a^5 - 1$, then $25 \mid a^5 - 1$. $5 \mid a^5 - 1$ iff $a \equiv 1 \pmod 5$ (by Fermat, $a^5 \equiv a \pmod 5$). So $a = 5k + 1$. $a^5 = (5k+1)^5 = 1 + 5 \cdot 5k + \binom{5}{2}(5k)^2 + \ldots = 1 + 25k + 250k^2 + \ldots$. So $a^5 - 1 = 25k + 250k^2 + \ldots = 25(k + 10k^2 + \ldots)$. So $25 \mid a^5 - 1$. ✓. So $n = 5 \in S$.

Hmm, it seems like for primes $p$, this might always work. Let me think about why.

For prime $p$: $p \mid a^p - 1$ iff $a \equiv 1 \pmod p$ (by Fermat's little theorem, $a^p \equiv a \pmod p$, so $a^p - 1 \equiv a - 1 \pmod p$). So $a = kp + 1$. Then $a^p = (1 + kp)^p = 1 + p \cdot kp + \binom{p}{2}(kp)^2 + \ldots = 1 + kp^2 + \ldots$. The second term is $kp^2$, and all subsequent terms have at least $p^2$ (actually $(kp)^2 = k^2 p^2$ times $\binom{p}{2}$, so at least $p^2$). So $a^p - 1 \equiv kp^2 \pmod{p^3}$, which means $p^2 \mid a^p - 1$. ✓.

So all primes are in $S$. That gives us 2, 3, 5, 7, 11, 13, 17, 19.

Now let me check composite numbers.

**$n = 6 = 2 \cdot 3$**: Need: if $6 \mid a^6 - 1$, then $36 \mid a^6 - 1$. $6 \mid a^6 - 1$ means $2 \mid a^6 - 1$ and $3 \mid a^6 - 1$. $2 \mid a^6 - 1$ iff $a$ odd. $3 \mid a^6 - 1$: by Fermat, $a^3 \equiv a \pmod 3$, so $a^6 \equiv a^2 \pmod 3$. So $3 \mid a^6 - 1$ iff $a^2 \equiv 1 \pmod 3$ iff $a \not\equiv 0 \pmod 3$, i.e., $\gcd(a, 3) = 1$.

So $6 \mid a^6 - 1$ iff $a$ is odd and $\gcd(a, 3) = 1$, i.e., $\gcd(a, 6) = 1$.

Now need $36 \mid a^6 - 1$, i.e., $4 \mid a^6 - 1$ and $9 \mid a^6 - 1$.

For odd $a$: $a^2 \equiv 1 \pmod 8$, so $a^6 = (a^2)^3 \equiv 1 \pmod 8$, so $4 \mid a^6 - 1$. ✓.

For $\gcd(a, 3) = 1$: $a^6 - 1 = (a^3 - 1)(a^3 + 1)$. We need $9 \mid a^6 - 1$. If $a \equiv 1 \pmod 3$, then $a^3 \equiv 1 \pmod 9$ (by the same argument as $n = 3$ case: $a = 3k+1$, $a^3 = 27k^3 + 27k^2 + 9k + 1$, so $a^3 \equiv 1 \pmod 9$). So $9 \mid a^3 - 1$, hence $9 \mid a^6 - 1$. ✓.

If $a \equiv 2 \pmod 3$, then $a^3 \equiv 8 \equiv -1 \pmod 9$? Let me check: $a = 2$: $2^3 = 8$, $8 \equiv -1 \pmod 9$. So $9 \mid a^3 + 1$, hence $9 \mid a^6 - 1$. ✓.

Actually, let me verify more carefully. $a \equiv 2 \pmod 3$, so $a = 3k + 2$. $a^3 = (3k+2)^3 = 27k^3 + 54k^2 + 36k + 8 = 9(3k^3 + 6k^2 + 4k) + 8$. So $a^3 \equiv 8 \equiv -1 \pmod 9$. So $9 \mid a^3 + 1$, and $a^6 - 1 = (a^3-1)(a^3+1)$, so $9 \mid a^6 - 1$. ✓.

So $n = 6 \in S$.

**$n = 7$**: Prime, so in $S$ (as shown above).

**$n = 8 = 2^3$**: Need: if $8 \mid a^8 - 1$, then $64 \mid a^8 - 1$. $8 \mid a^8 - 1$ requires $a$ odd. For odd $a$, $a^2 \equiv 1 \pmod 8$, so $a^8 = (a^2)^4 \equiv 1 \pmod 8$. So $8 \mid a^8 - 1$ for all odd $a$.

Now need $64 \mid a^8 - 1$ for all odd $a$. $a^2 \equiv 1 \pmod 8$, so $a^2 = 8m + 1$. $a^8 = (8m+1)^4 = 1 + 4 \cdot 8m + 6 \cdot 64m^2 + \ldots = 1 + 32m + 384m^2 + \ldots$. So $a^8 - 1 = 32m + 384m^2 + \ldots = 32(m + 12m^2 + \ldots)$. For $64 \mid a^8 - 1$, we need $2 \mid m + 12m^2 + \ldots$, i.e., $m$ even.

But $m$ might not be even. Let's check $a = 3$: $3^2 = 9 = 8 \cdot 1 + 1$, so $m = 1$ (odd). $3^8 = 6561$. $6561 - 1 = 6560$. $6560 / 64 = 102.5$. So $64 \nmid 6560$. Let me verify: $6560 = 64 \cdot 102 + 32$. So $64 \nmid 6560$.

So $n = 8 \notin S$.

**$n = 9 = 3^2$**: Need: if $9 \mid a^9 - 1$, then $81 \mid a^9 - 1$. $9 \mid a^9 - 1$ requires $\gcd(a, 3) = 1$. For $\gcd(a, 3) = 1$, $a^3 \equiv \pm 1 \pmod 9$ (as shown above). So $a^9 = (a^3)^3$. If $a^3 \equiv 1 \pmod 9$, then $a^9 \equiv 1 \pmod 9$. If $a^3 \equiv -1 \pmod 9$, then $a^9 \equiv -1 \pmod 9$, so $9 \nmid a^9 - 1$.

So $9 \mid a^9 - 1$ iff $a^3 \equiv 1 \pmod 9$, i.e., $a \equiv 1 \pmod 3$ (and more specifically, $a \equiv 1 \pmod 3$ gives $a^3 \equiv 1 \pmod 9$).

Wait, let me be more careful. $a \equiv 1 \pmod 3$: $a = 3k + 1$, $a^3 = 27k^3 + 27k^2 + 9k + 1 \equiv 1 \pmod 9$. So $a^3 \equiv 1 \pmod 9$.

$a \equiv 2 \pmod 3$: $a = 3k + 2$, $a^3 \equiv 8 \equiv -1 \pmod 9$. So $a^3 \equiv -1 \pmod 9$.

So $9 \mid a^9 - 1$ iff $a \equiv 1 \pmod 3$ (and $\gcd(a, 3) = 1$, which is automatic).

Now, for $a \equiv 1 \pmod 3$, need $81 \mid a^9 - 1$.

$a = 3k + 1$. $a^9 = (3k+1)^9 = 1 + 9 \cdot 3k + \binom{9}{2}(3k)^2 + \ldots = 1 + 27k + 36 \cdot 9k^2 + \ldots = 1 + 27k + 324k^2 + \ldots$.

$a^9 - 1 = 27k + 324k^2 + \ldots = 27(k + 12k^2 + \ldots)$.

For $81 \mid a^9 - 1$, need $3 \mid k + 12k^2 + \ldots$, i.e., $3 \mid k$ (since $12k^2 \equiv 0 \pmod 3$ and higher terms... let me check).

Actually, let me be more careful. $a^9 - 1 = \sum_{j=1}^{9} \binom{9}{j} (3k)^j = 27k + \binom{9}{2} \cdot 9k^2 + \binom{9}{3} \cdot 27k^3 + \ldots$

$= 27k + 36 \cdot 9k^2 + 84 \cdot 27k^3 + \ldots$

$= 27k + 324k^2 + 2268k^3 + \ldots$

$= 27(k + 12k^2 + 84k^3 + \ldots)$

For $81 \mid a^9 - 1$, need $3 \mid k + 12k^2 + 84k^3 + \ldots$. Since $12 \equiv 0$, $84 \equiv 0 \pmod 3$, this reduces to $3 \mid k$.

But $k$ can be anything. If $k = 1$, $a = 4$, $a^9 = 4^9 = 262144$. $262144 - 1 = 262143$. $262143 / 81 = 3236.33...$. Let me compute: $81 \cdot 3236 = 262116$. $262143 - 262116 = 27$. So $81 \nmid 262143$.

So $n = 9 \notin S$.

**$n = 10 = 2 \cdot 5$**: Need: if $10 \mid a^{10} - 1$, then $100 \mid a^{10} - 1$. $10 \mid a^{10} - 1$ means $2 \mid a^{10} - 1$ (so $a$ odd) and $5 \mid a^{10} - 1$. By Fermat, $a^5 \equiv a \pmod 5$, so $a^{10} \equiv a^2 \pmod 5$. So $5 \mid a^{10} - 1$ iff $a^2 \equiv 1 \pmod 5$ iff $a \equiv \pm 1 \pmod 5$.

So $10 \mid a^{10} - 1$ iff $a$ is odd and $a \equiv \pm 1 \pmod 5$.

Need $100 \mid a^{10} - 1$, i.e., $4 \mid a^{10} - 1$ and $25 \mid a^{10} - 1$.

For odd $a$: $a^2 \equiv 1 \pmod 8$, so $a^{10} = (a^2)^5 \equiv 1 \pmod 8$, so $4 \mid a^{10} - 1$. ✓.

For $a \equiv 1 \pmod 5$: $a = 5k + 1$. $a^5 = (5k+1)^5 = 1 + 25k + \ldots \equiv 1 \pmod{25}$. So $a^{10} = (a^5)^2 \equiv 1 \pmod{25}$. ✓.

For $a \equiv -1 \pmod 5$: $a = 5k - 1$. $a^5 = (5k-1)^5 = -1 + 25k - \ldots \equiv -1 \pmod{25}$? Let me check: $(5k-1)^5 = \sum_{j=0}^{5} \binom{5}{j}(5k)^j(-1)^{5-j} = -1 + 5 \cdot 5k - 10 \cdot 25k^2 + 10 \cdot 125k^3 - 5 \cdot 625k^4 + 3125k^5 = -1 + 25k - 250k^2 + 1250k^3 - 3125k^4 + 3125k^5$. So $a^5 \equiv -1 + 25k \pmod{25}$... wait, $-1 + 25k \equiv -1 \pmod{25}$. So $a^5 \equiv -1 \pmod{25}$. Then $a^{10} = (a^5)^2 \equiv 1 \pmod{25}$. ✓.

So $n = 10 \in S$.

Hmm, interesting. Let me think about the pattern. It seems like squarefree numbers might work, while numbers with squared prime factors might not (except for $n = 4$).

Wait, $n = 4 = 2^2$ worked. Let me re-examine.

For $n = 4$: $4 \mid a^4 - 1$ iff $a$ odd. For odd $a$, $a^4 \equiv 1 \pmod{16}$ (shown above). So $16 \mid a^4 - 1$. ✓.

For $n = 8 = 2^3$: $8 \mid a^8 - 1$ iff $a$ odd. But $64 \nmid a^8 - 1$ for $a = 3$. ✗.

For $n = 9 = 3^2$: ✗ (shown above).

So $n = 4$ works but $n = 8, 9$ don't. Let me think about why $n = 4$ is special.

For $n = p^e$, the condition is: for all $a$ coprime to $p$, if $p^e \mid a^{p^e} - 1$, then $p^{2e} \mid a^{p^e} - 1$.

The group $(\mathbb{Z}/p^{2e}\mathbb{Z})^*$ is cyclic for odd $p$, of order $p^{2e-1}(p-1)$. The condition $p^e \mid a^{p^e} - 1$ means $a^{p^e} \equiv 1 \pmod{p^e}$, i.e., the order of $a$ mod $p^e$ divides $p^e$.

Hmm, this is getting complicated. Let me just check all values up to 20.

I've checked: 2 ✓, 3 ✓, 4 ✓, 5 ✓, 6 ✓, 7 ✓, 8 ✗, 9 ✗, 10 ✓.

**$n = 11$**: Prime. ✓.

**$n = 12 = 4 \cdot 3 = 2^2 \cdot 3$**: Need: if $12 \mid a^{12} - 1$, then $144 \mid a^{12} - 1$.

$12 \mid a^{12} - 1$ means $4 \mid a^{12} - 1$ and $3 \mid a^{12} - 1$.

$4 \mid a^{12} - 1$: $a$ must be odd (if $a$ even, $a^{12}$ is even, $a^{12} - 1$ odd). For odd $a$, $a^2 \equiv 1 \pmod 8$, so $a^{12} = (a^2)^6 \equiv 1 \pmod 8$, so $4 \mid a^{12} - 1$. ✓.

$3 \mid a^{12} - 1$: $a^{12} \equiv a^{12} \pmod 3$. By Fermat, $a^3 \equiv a \pmod 3$, so $a^{12} = (a^3)^4 \equiv a^4 \pmod 3$. $a^4 \equiv a^2 \pmod 3$ (since $a^3 \equiv a$). So $a^{12} \equiv a^2 \pmod 3$. So $3 \mid a^{12} - 1$ iff $a^2 \equiv 1 \pmod 3$ iff $\gcd(a, 3) = 1$.

So $12 \mid a^{12} - 1$ iff $a$ is odd and $\gcd(a, 3) = 1$, i.e., $\gcd(a, 6) = 1$.

Need $144 \mid a^{12} - 1$, i.e., $16 \mid a^{12} - 1$ and $9 \mid a^{12} - 1$.

For odd $a$: $a^2 \equiv 1 \pmod 8$, so $a^{12} = (a^2)^6 \equiv 1 \pmod 8$. But we need $16 \mid a^{12} - 1$. $a^2 = 8m + 1$. $a^{12} = (8m+1)^6 = 1 + 6 \cdot 8m + 15 \cdot 64m^2 + \ldots = 1 + 48m + 960m^2 + \ldots$. So $a^{12} - 1 = 48m + 960m^2 + \ldots = 16(3m + 60m^2 + \ldots)$. So $16 \mid a^{12} - 1$ iff $3m + 60m^2 + \ldots$ is an integer, which it always is. Wait, $48m = 16 \cdot 3m$, so $16 \mid 48m$. And $960m^2 = 16 \cdot 60m^2$, so $16 \mid 960m^2$. So $16 \mid a^{12} - 1$ for all odd $a$. ✓.

Hmm wait, let me double-check with $a = 3$: $3^{12} = 531441$. $531441 - 1 = 531440$. $531440 / 16 = 33215$. ✓. $531440 / 144 = 3690.56...$. Let me check $9$: $531440 / 9 = 59048.89...$. So $9 \nmid 531440$?

Wait, but $a = 3$ and $\gcd(3, 3) = 3 \neq 1$, so $12 \nmid 3^{12} - 1$. Let me recheck: $3 \mid 3^{12} - 1$? $3^{12} \equiv 0 \pmod 3$, so $3^{12} - 1 \equiv -1 \pmod 3$. So $3 \nmid 3^{12} - 1$. Right, so $a = 3$ doesn't satisfy the hypothesis.

Let me try $a = 5$: $\gcd(5, 6) = 1$. $5^{12} = 244140625$. $244140625 - 1 = 244140624$. $244140624 / 12 = 20345052$. ✓. $244140624 / 144 = 1695421$. Let me check: $144 \cdot 1695421 = 244140624$. ✓. So $144 \mid 5^{12} - 1$.

Let me try $a = 7$: $\gcd(7, 6) = 1$. $7^{12} = 13841287201$. $-1 = 13841287200$. $/ 12 = 1153440600$. $/ 144 = 96120050$. Let me verify: $144 \cdot 96120050 = 13841287200$. ✓.

Let me try to find a counterexample. We need $a$ odd, $\gcd(a, 3) = 1$, but $144 \nmid a^{12} - 1$.

$144 = 16 \cdot 9$. We showed $16 \mid a^{12} - 1$ for all odd $a$. So we need $9 \mid a^{12} - 1$ for all $a$ with $\gcd(a, 3) = 1$.

$a^{12} = (a^3)^4$. If $a \equiv 1 \pmod 3$, $a^3 \equiv 1 \pmod 9$, so $a^{12} \equiv 1 \pmod 9$. ✓.

If $a \equiv 2 \pmod 3$, $a^3 \equiv -1 \pmod 9$, so $a^{12} = (a^3)^4 \equiv 1 \pmod 9$. ✓.

So $9 \mid a^{12} - 1$ for all $a$ with $\gcd(a, 3) = 1$. ✓.

So $n = 12 \in S$.

**$n = 13$**: Prime. ✓.

**$n = 14 = 2 \cdot 7$**: Similar to $n = 6$ and $n = 10$. $14 \mid a^{14} - 1$ iff $a$ odd and $7 \mid a^{14} - 1$. By Fermat, $a^7 \equiv a \pmod 7$, so $a^{14} \equiv a^2 \pmod 7$. So $7 \mid a^{14} - 1$ iff $a^2 \equiv 1 \pmod 7$ iff $a \equiv \pm 1 \pmod 7$.

Need $196 \mid a^{14} - 1$, i.e., $4 \mid a^{14} - 1$ and $49 \mid a^{14} - 1$.

$4 \mid a^{14} - 1$ for odd $a$: $a^2 \equiv 1 \pmod 8$, $a^{14} = (a^2)^7 \equiv 1 \pmod 8$. ✓.

$49 \mid a^{14} - 1$ for $a \equiv \pm 1 \pmod 7$:

$a \equiv 1 \pmod 7$: $a = 7k + 1$. $a^7 = (7k+1)^7 = 1 + 7 \cdot 7k + \ldots = 1 + 49k + \ldots \equiv 1 \pmod{49}$. So $a^{14} \equiv 1 \pmod{49}$. ✓.

$a \equiv -1 \pmod 7$: $a = 7k - 1$. $a^7 = (7k-1)^7 = -1 + 7 \cdot 7k - \ldots \equiv -1 \pmod{49}$. So $a^{14} \equiv 1 \pmod{49}$. ✓.

So $n = 14 \in S$.

**$n = 15 = 3 \cdot 5$**: $15 \mid a^{15} - 1$ iff $3 \mid a^{15} - 1$ and $5 \mid a^{15} - 1$.

$3 \mid a^{15} - 1$: $a^{15} \equiv a^{15} \pmod 3$. $a^3 \equiv a \pmod 3$, so $a^{15} = (a^3)^5 \equiv a^5 \equiv a^3 \cdot a^2 \equiv a \cdot a^2 = a^3 \equiv a \pmod 3$. So $3 \mid a^{15} - 1$ iff $a \equiv 1 \pmod 3$.

$5 \mid a^{15} - 1$: $a^5 \equiv a \pmod 5$, so $a^{15} = (a^5)^3 \equiv a^3 \pmod 5$. So $5 \mid a^{15} - 1$ iff $a^3 \equiv 1 \pmod 5$. The cubes mod 5: $0^3=0, 1^3=1, 2^3=3, 3^3=2, 4^3=4$. So $a^3 \equiv 1 \pmod 5$ iff $a \equiv 1 \pmod 5$.

So $15 \mid a^{15} - 1$ iff $a \equiv 1 \pmod 3$ and $a \equiv 1 \pmod 5$, i.e., $a \equiv 1 \pmod{15}$.

Need $225 \mid a^{15} - 1$, i.e., $9 \mid a^{15} - 1$ and $25 \mid a^{15} - 1$.

$a \equiv 1 \pmod{15}$, so $a = 15k + 1$.

$9 \mid a^{15} - 1$: $a \equiv 1 \pmod 3$, so $a = 3m + 1$ where $m = 5k$. $a^3 \equiv 1 \pmod 9$ (shown before). $a^{15} = (a^3)^5 \equiv 1 \pmod 9$. ✓.

$25 \mid a^{15} - 1$: $a \equiv 1 \pmod 5$, so $a = 5j + 1$ where $j = 3k$. $a^5 \equiv 1 \pmod{25}$ (shown before). $a^{15} = (a^5)^3 \equiv 1 \pmod{25}$. ✓.

So $n = 15 \in S$.

**$n = 16 = 2^4$**: Need: if $16 \mid a^{16} - 1$, then $256 \mid a^{16} - 1$. $16 \mid a^{16} - 1$ requires $a$ odd. For odd $a$, $a^2 \equiv 1 \pmod 8$, so $a^{16} = (a^2)^8 \equiv 1 \pmod 8$, but we need $16 \mid a^{16} - 1$.

Actually, for odd $a$, is $16 \mid a^{16} - 1$ always? $a = 3$: $3^{16} = 43046721$. $43046721 - 1 = 43046720$. $43046720 / 16 = 2690420$. ✓. $43046720 / 256 = 168152.03...$. $256 \cdot 168152 = 43046912 > 43046720$. So $256 \nmid 43046720$.

So $n = 16 \notin S$.

**$n = 17$**: Prime. ✓.

**$n = 18 = 2 \cdot 3^2$**: Need: if $18 \mid a^{18} - 1$, then $324 \mid a^{18} - 1$.

$18 \mid a^{18} - 1$ means $2 \mid a^{18} - 1$ (so $a$ odd) and $9 \mid a^{18} - 1$.

$9 \mid a^{18} - 1$: $a^{18} = (a^3)^6$. If $\gcd(a, 3) = 1$, then $a^3 \equiv \pm 1 \pmod 9$, so $a^{18} = (a^3)^6 \equiv 1 \pmod 9$. If $3 \mid a$, then $a^3 \equiv 0 \pmod 9$ (if $3 \mid a$ then $9 \mid a^3$), so $a^{18} \equiv 0 \pmod 9$, and $9 \nmid a^{18} - 1$.

So $9 \mid a^{18} - 1$ iff $\gcd(a, 3) = 1$.

So $18 \mid a^{18} - 1$ iff $a$ is odd and $\gcd(a, 3) = 1$, i.e., $\gcd(a, 6) = 1$.

Need $324 \mid a^{18} - 1$, i.e., $4 \mid a^{18} - 1$ and $81 \mid a^{18} - 1$.

$4 \mid a^{18} - 1$ for odd $a$: $a^2 \equiv 1 \pmod 8$, $a^{18} = (a^2)^9 \equiv 1 \pmod 8$. So $4 \mid a^{18} - 1$. ✓.

$81 \mid a^{18} - 1$ for $\gcd(a, 3) = 1$: $a^{18} = (a^9)^2$. We need $81 \mid a^{18} - 1$.

Let me think. $a$ is coprime to 3. The group $(\mathbb{Z}/81\mathbb{Z})^*$ is cyclic of order $\phi(81) = 54$. We need $a^{18} \equiv 1 \pmod{81}$ for all $a$ coprime to 3 with $a$ odd and $\gcd(a, 3) = 1$.

But wait, the condition is only for $a$ with $\gcd(a, 6) = 1$. Let me check if there's a counterexample.

$a = 5$: $\gcd(5, 6) = 1$. $5^{18} \pmod{81}$?

$5^2 = 25$. $5^3 = 125 \equiv 125 - 81 = 44 \pmod{81}$. $5^6 = 44^2 = 1936 \equiv 1936 - 23 \cdot 81 = 1936 - 1863 = 73 \pmod{81}$. $5^9 = 5^6 \cdot 5^3 = 73 \cdot 44 = 3212 \equiv 3212 - 39 \cdot 81 = 3212 - 3159 = 53 \pmod{81}$. $5^{18} = 53^2 = 2809 \equiv 2809 - 34 \cdot 81 = 2809 - 2754 = 55 \pmod{81}$.

So $5^{18} \equiv 55 \pmod{81}$, and $55 \neq 1$. So $81 \nmid 5^{18} - 1$.

So $n = 18 \notin S$.

**$n = 19$**: Prime. ✓.

**$n = 20 = 4 \cdot 5 = 2^2 \cdot 5$**: Need: if $20 \mid a^{20} - 1$, then $400 \mid a^{20} - 1$.

$20 \mid a^{20} - 1$ means $4 \mid a^{20} - 1$ and $5 \mid a^{20} - 1$.

$4 \mid a^{20} - 1$: $a$ must be odd. For odd $a$, $a^2 \equiv 1 \pmod 8$, so $a^{20} = (a^2)^{10} \equiv 1 \pmod 8$, so $4 \mid a^{20} - 1$. ✓.

$5 \mid a^{20} - 1$: $a^5 \equiv a \pmod 5$, $a^{20} = (a^5)^4 \equiv a^4 \pmod 5$. $a^4 \equiv 1 \pmod 5$ for $\gcd(a, 5) = 1$ (Fermat). So $5 \mid a^{20} - 1$ iff $\gcd(a, 5) = 1$.

So $20 \mid a^{20} - 1$ iff $a$ is odd and $\gcd(a, 5) = 1$, i.e., $\gcd(a, 10) = 1$.

Need $400 \mid a^{20} - 1$, i.e., $16 \mid a^{20} - 1$ and $25 \mid a^{20} - 1$.

$16 \mid a^{20} - 1$ for odd $a$: $a^2 \equiv 1 \pmod 8$, $a^{20} = (a^2)^{10} \equiv 1 \pmod 8$. But we need $16 \mid a^{20} - 1$.

$a = 3$: $3^{20} = 3486784401$. $3486784401 - 1 = 3486784400$. $3486784400 / 16 = 217924025$. ✓. So $16 \mid 3^{20} - 1$.

Actually, let me think more carefully. For odd $a$, $a^2 = 8m + 1$. $a^{20} = (8m+1)^{10} = 1 + 10 \cdot 8m + \binom{10}{2} \cdot 64m^2 + \ldots = 1 + 80m + 2880m^2 + \ldots$. So $a^{20} - 1 = 80m + 2880m^2 + \ldots = 16(5m + 180m^2 + \ldots)$. So $16 \mid a^{20} - 1$ for all odd $a$. ✓.

$25 \mid a^{20} - 1$ for $\gcd(a, 5) = 1$: $a^5 \equiv a \pmod 5$, but we need mod 25. $a^{20} = (a^5)^4$. 

For $a \equiv 1 \pmod 5$: $a = 5k + 1$, $a^5 \equiv 1 \pmod{25}$ (shown before). So $a^{20} \equiv 1 \pmod{25}$. ✓.

For $a \equiv 2 \pmod 5$: $a = 5k + 2$. $a^5 = (5k+2)^5 = 32 + 5 \cdot 16 \cdot 5k + \ldots = 32 + 400k + \ldots$. $32 \equiv 7 \pmod{25}$. $400k \equiv 0 \pmod{25}$. So $a^5 \equiv 7 \pmod{25}$. Then $a^{20} = (a^5)^4 \equiv 7^4 = 2401 \pmod{25}$. $2401 = 96 \cdot 25 + 1$. So $a^{20} \equiv 1 \pmod{25}$. ✓.

For $a \equiv 3 \pmod 5$: $a^5 \equiv 3^5 = 243 \equiv 243 - 9 \cdot 25 = 243 - 225 = 18 \pmod{25}$. $a^{20} = 18^4 = 104976 \pmod{25}$. $104976 / 25 = 4199.04$. $25 \cdot 4199 = 104975$. $104976 - 104975 = 1$. So $a^{20} \equiv 1 \pmod{25}$. ✓.

For $a \equiv 4 \pmod 5$: $a^5 \equiv 4^5 = 1024 \equiv 1024 - 40 \cdot 25 = 1024 - 1000 = 24 \equiv -1 \pmod{25}$. $a^{20} = (-1)^4 = 1 \pmod{25}$. ✓.

So $25 \mid a^{20} - 1$ for all $a$ with $\gcd(a, 5) = 1$. ✓.

So $n = 20 \in S$.

Now let me also double-check $n = 4$ more carefully, and reconsider the pattern.

So far: $S \cap \{2, \ldots, 20\} = \{2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17, 19, 20\}$.

Not in $S$: $\{8, 9, 16, 18\}$.

Let me verify the sum: $2 + 3 + 4 + 5 + 6 + 7 + 10 + 11 + 12 + 13 + 14 + 15 + 17 + 19 + 20$.

$= (2+3+4+5+6+7) + (10+11+12+13+14+15) + (17+19+20)$

$= 27 + 75 + 56 = 158$.

Wait, let me also check $n = 4$ again. I want to make sure.

$n = 4$: for all $a$, if $4 \mid a^4 - 1$ then $16 \mid a^4 - 1$. $4 \mid a^4 - 1$ iff $a$ odd (since for even $a$, $a^4 - 1$ is odd). For odd $a$, $a = 2k+1$, $a^2 = 4k^2 + 4k + 1 = 4k(k+1) + 1$. Since $k(k+1)$ is even, $a^2 = 8j + 1$ for some $j$. $a^4 = (8j+1)^2 = 64j^2 + 16j + 1 = 16(4j^2 + j) + 1$. So $16 \mid a^4 - 1$. ✓.

Now let me think about what the pattern is. The numbers NOT in $S$ up to 20 are: 8, 9, 16, 18.

- $8 = 2^3$
- $9 = 3^2$
- $16 = 2^4$
- $18 = 2 \cdot 3^2$

And the numbers IN $S$ with prime power factors:
- $4 = 2^2$ ✓
- $12 = 2^2 \cdot 3$ ✓
- $20 = 2^2 \cdot 5$ ✓

So $2^2$ is OK but $3^2$ is not (in $n = 9$ and $n = 18$). And $2^3, 2^4$ are not OK.

Let me think about this more carefully. The key insight is about the structure of the multiplicative group modulo $p^{2e}$.

For $n = p^e$ (prime power), the condition is: for all $a$ coprime to $p$, if $p^e \mid a^{p^e} - 1$ then $p^{2e} \mid a^{p^e} - 1$.

The group $(\mathbb{Z}/p^{2e}\mathbb{Z})^*$ for odd $p$ is cyclic of order $p^{2e-1}(p-1)$. The subgroup of elements $\equiv 1 \pmod{p^e}$ has order $p^e$ (it's the kernel of reduction mod $p^e$).

The condition $p^e \mid a^{p^e} - 1$ means $a^{p^e} \equiv 1 \pmod{p^e}$, i.e., $\text{ord}_{p^e}(a) \mid p^e$.

The condition $p^{2e} \mid a^{p^e} - 1$ means $a^{p^e} \equiv 1 \pmod{p^{2e}}$, i.e., $\text{ord}_{p^{2e}}(a) \mid p^e$.

So we need: for all $a$ coprime to $p$, $\text{ord}_{p^e}(a) \mid p^e \implies \text{ord}_{p^{2e}}(a) \mid p^e$.

Now, $\text{ord}_{p^{2e}}(a) \mid p^e$ iff $a^{p^e} \equiv 1 \pmod{p^{2e}}$. And $\text{ord}_{p^e}(a) \mid p^e$ iff $a^{p^e} \equiv 1 \pmod{p^e}$.

The question is whether there exists $a$ with $a^{p^e} \equiv 1 \pmod{p^e}$ but $a^{p^e} \not\equiv 1 \pmod{p^{2e}}$.

In the cyclic group $(\mathbb{Z}/p^{2e}\mathbb{Z})^*$ of order $p^{2e-1}(p-1)$, the $p^e$-th powers form a subgroup. The elements with $a^{p^e} \equiv 1 \pmod{p^e}$ are those whose order mod $p^e$ divides $p^e$.

Hmm, let me think about this differently using the $p$-adic valuation.

For odd prime $p$, $(\mathbb{Z}/p^k\mathbb{Z})^*$ is cyclic of order $p^{k-1}(p-1)$. Let $g$ be a primitive root mod $p^2$ (hence mod $p^k$ for all $k$). Then $g$ has order $p^{k-1}(p-1)$ mod $p^k$.

An element $a = g^j$ has $a^{p^e} \equiv 1 \pmod{p^e}$ iff $p^{e-1}(p-1) \mid j \cdot p^e$, i.e., $(p-1) \mid j \cdot p$... wait, let me be more careful.

$\text{ord}_{p^e}(g^j) = \frac{p^{e-1}(p-1)}{\gcd(j, p^{e-1}(p-1))}$.

$a^{p^e} \equiv 1 \pmod{p^e}$ iff $\text{ord}_{p^e}(a) \mid p^e$ iff $\frac{p^{e-1}(p-1)}{\gcd(j, p^{e-1}(p-1))} \mid p^e$.

Since $p^{e-1}(p-1) / \gcd(j, p^{e-1}(p-1))$ must divide $p^e$, and $p^{e-1}(p-1) / \gcd(j, p^{e-1}(p-1))$ divides $p^{e-1}(p-1)$, we need it to divide $p^e$. Since $\gcd(p^{e-1}(p-1), p^e) = p^{e-1}$, we need $p^{e-1}(p-1)/\gcd(j, p^{e-1}(p-1)) \mid p^{e-1}$, which means $(p-1) \mid \gcd(j, p^{e-1}(p-1))$, i.e., $(p-1) \mid j$.

So $a^{p^e} \equiv 1 \pmod{p^e}$ iff $(p-1) \mid j$ (where $a = g^j$).

Similarly, $a^{p^e} \equiv 1 \pmod{p^{2e}}$ iff $\text{ord}_{p^{2e}}(a) \mid p^e$, i.e., $\frac{p^{2e-1}(p-1)}{\gcd(j, p^{2e-1}(p-1))} \mid p^e$. This requires $(p-1) \mid \gcd(j, p^{2e-1}(p-1))$ and $p^{2e-1}/\gcd(j, p^{2e-1}(p-1))$... hmm, let me think again.

$\frac{p^{2e-1}(p-1)}{\gcd(j, p^{2e-1}(p-1))} \mid p^e$.

Let $d = \gcd(j, p^{2e-1}(p-1))$. We need $p^{2e-1}(p-1)/d \mid p^e$. Since $\gcd(p^{2e-1}(p-1), p^e) = p^{e}$ (for $e \geq 1$, and $p \nmid (p-1)$), we need $p^{2e-1}(p-1)/d \mid p^e$. 

Write $d = p^a \cdot b$ where $p \nmid b$ and $b \mid (p-1)$, $a \leq 2e-1$. Then $p^{2e-1}(p-1)/d = p^{2e-1-a}(p-1)/b$. For this to divide $p^e$, we need $(p-1)/b = 1$ (i.e., $(p-1) \mid b$, but $b \mid (p-1)$, so $b = p-1$) and $2e-1-a \leq e$, i.e., $a \geq e-1$.

So $a^{p^e} \equiv 1 \pmod{p^{2e}}$ iff $(p-1) \mid j$ and $p^{e-1} \mid j$ (i.e., $v_p(j) \geq e-1$), i.e., $p^{e-1}(p-1) \mid j$.

And $a^{p^e} \equiv 1 \pmod{p^e}$ iff $(p-1) \mid j$.

So the condition for $n = p^e$ (odd $p$) to be in $S$ is: for all $j$ with $(p-1) \mid j$, we have $p^{e-1}(p-1) \mid j$. But this is clearly false for $e \geq 2$ (take $j = p-1$, which satisfies $(p-1) \mid j$ but not $p^{e-1}(p-1) \mid j$ when $e \geq 2$).

Wait, but we also need $a = g^j$ to range over all elements coprime to $p$, and $j$ ranges over $0, 1, \ldots, p^{2e-1}(p-1) - 1$. The condition $(p-1) \mid j$ but $p^{e-1}(p-1) \nmid j$ is satisfiable when $e \geq 2$: take $j = p-1$. Then $a = g^{p-1}$, and $a^{p^e} \equiv 1 \pmod{p^e}$ but $a^{p^e} \not\equiv 1 \pmod{p^{2e}}$.

So for odd prime $p$ and $e \geq 2$, $n = p^e \notin S$.

For $e = 1$, $n = p$: the condition becomes $(p-1) \mid j \implies (p-1) \mid j$, which is trivially true. So $n = p \in S$ for all primes $p$. ✓ (matches our findings).

Now for $p = 2$: The group $(\mathbb{Z}/2^k\mathbb{Z})^*$ is not cyclic for $k \geq 3$. It's $\cong \mathbb{Z}/2 \times \mathbb{Z}/2^{k-2}$.

For $k = 1$: $(\mathbb{Z}/2\mathbb{Z})^* = \{1\}$, trivial.
For $k = 2$: $(\mathbb{Z}/4\mathbb{Z})^* \cong \mathbb{Z}/2$, generated by 3 (or $-1$).
For $k \geq 3$: $(\mathbb{Z}/2^k\mathbb{Z})^* \cong \mathbb{Z}/2 \times \mathbb{Z}/2^{k-2}$, generated by $-1$ and $5$ (or some element of order $2^{k-2}$).

For $n = 2^e$:
- $e = 1$: $n = 2$. Checked: ✓.
- $e = 2$: $n = 4$. Checked: ✓.
- $e = 3$: $n = 8$. Checked: ✗.
- $e = 4$: $n = 16$. Checked: ✗.

Let me understand why $e = 2$ works but $e \geq 3$ doesn't.

For $n = 2^e$, the condition is: for all odd $a$, if $2^e \mid a^{2^e} - 1$ then $2^{2e} \mid a^{2^e} - 1$.

For $e \geq 3$, $(\mathbb{Z}/2^{2e}\mathbb{Z})^* \cong \mathbb{Z}/2 \times \mathbb{Z}/2^{2e-2}$. The order of $a$ mod $2^{2e}$ divides $2^{2e-2} \cdot 2 = 2^{2e-1}$... actually the exponent of the group is $2^{2e-2}$ (lcm of 2 and $2^{2e-2}$).

Hmm, let me think about this using the 2-adic valuation of $a^{2^e} - 1$.

For odd $a$, $v_2(a^2 - 1) = v_2(a-1) + v_2(a+1) \geq 3$ (since one of $a-1, a+1$ is $\equiv 2 \pmod 4$ and the other $\equiv 0 \pmod 4$, so $v_2 \geq 1 + 2 = 3$). Actually, more precisely, for odd $a$, $v_2(a^2 - 1) \geq 3$.

By LTE (Lifting the Exponent), for odd $a$ and $n$ even, $v_2(a^n - 1) = v_2(a^2 - 1) + v_2(n) - 1$.

Wait, LTE for $p = 2$: if $2 \mid a - 1$ (i.e., $a$ odd) and $2 \mid n$, then $v_2(a^n - 1) = v_2(a - 1) + v_2(a + 1) + v_2(n) - 1$.

Hmm, actually the LTE lemma for $p = 2$ is a bit different. Let me recall:

For $p = 2$, $2 \mid a - b$, $2 \mid a + b$, and $n$ even: $v_2(a^n - b^n) = v_2(a - b) + v_2(a + b) + v_2(n) - 1$.

With $b = 1$, $a$ odd: $v_2(a^n - 1) = v_2(a - 1) + v_2(a + 1) + v_2(n) - 1$ for $n$ even.

For $n = 2^e$ ($e \geq 1$), $v_2(n) = e$. So $v_2(a^{2^e} - 1) = v_2(a-1) + v_2(a+1) + e - 1$.

The condition $2^e \mid a^{2^e} - 1$ means $v_2(a^{2^e} - 1) \geq e$, i.e., $v_2(a-1) + v_2(a+1) + e - 1 \geq e$, i.e., $v_2(a-1) + v_2(a+1) \geq 1$. This is always true for odd $a$ (since $a - 1$ and $a + 1$ are both even, so each has $v_2 \geq 1$). So $2^e \mid a^{2^e} - 1$ for all odd $a$.

The condition $2^{2e} \mid a^{2^e} - 1$ means $v_2(a-1) + v_2(a+1) + e - 1 \geq 2e$, i.e., $v_2(a-1) + v_2(a+1) \geq e + 1$.

For $e = 1$: need $v_2(a-1) + v_2(a+1) \geq 2$. For odd $a$, one of $a-1, a+1$ is $\equiv 0 \pmod 4$ and the other $\equiv 2 \pmod 4$, so $v_2(a-1) + v_2(a+1) \geq 2 + 1 = 3 \geq 2$. ✓.

For $e = 2$: need $v_2(a-1) + v_2(a+1) \geq 3$. Same argument: $\geq 3$. ✓.

For $e = 3$: need $v_2(a-1) + v_2(a+1) \geq 4$. But for $a = 3$: $v_2(2) + v_2(4) = 1 + 2 = 3 < 4$. ✗.

For $e \geq 3$: take $a = 3$, $v_2(2) + v_2(4) = 3 < e + 1$ when $e \geq 3$. ✗.

So $n = 2^e \in S$ iff $e \leq 2$, i.e., $n \in \{2, 4\}$.

Now for general $n$, let me think about the structure. Let $n = 2^{e_0} \prod p_i^{e_i}$ (odd primes $p_i$).

The condition $n \mid a^n - 1$ is equivalent to: for each prime power $q = p^e \| n$, $p^e \mid a^n - 1$.

And $n^2 \mid a^n - 1$ is equivalent to: for each $q = p^e \| n$, $p^{2e} \mid a^n - 1$.

The condition must hold for all $a$. By CRT, we can choose $a$ independently mod each prime power dividing $n^2$ (as long as $\gcd(a, n) = 1$, which is necessary as shown).

So the condition decomposes: for each prime $p \mid n$ with $p^e \| n$, we need: for all $a$ coprime to $p$, if $p^e \mid a^n - 1$ then $p^{2e} \mid a^n - 1$.

Wait, but the condition is "for all $a$, if $n \mid a^n - 1$ then $n^2 \mid a^n - 1$". The hypothesis $n \mid a^n - 1$ involves ALL prime powers simultaneously. So we can't simply decompose.

However, by CRT, we can choose $a$ such that $a$ satisfies the hypothesis for all primes simultaneously. Specifically, for each prime $p_i \mid n$, the condition $p_i^{e_i} \mid a^n - 1$ constrains $a$ mod $p_i^{e_i}$ (or mod some power of $p_i$). By CRT, we can find $a$ satisfying all these constraints simultaneously (as long as they're compatible, which they are since they're mod different primes).

But the key question is: can we find $a$ such that $n \mid a^n - 1$ but for some specific prime $p \mid n$, $p^{2e} \nmid a^n - 1$?

If for some prime $p \mid n$ with $p^e \| n$, there exists $a$ (coprime to $n$) such that $p^e \mid a^n - 1$ but $p^{2e} \nmid a^n - 1$, AND we can simultaneously satisfy $q^{e_q} \mid a^n - 1$ for all other primes $q \mid n$, then $n \notin S$.

By CRT, if we can find $a_p$ mod $p^{2e}$ such that $p^e \mid a_p^n - 1$ but $p^{2e} \nmid a_p^n - 1$, and for each other prime $q \mid n$, we can find $a_q$ mod $q^{2e_q}$ such that $q^{e_q} \mid a_q^n - 1$, then we can combine them via CRT to get $a$ mod $n^2$ with $n \mid a^n - 1$ but $n^2 \nmid a^n - 1$.

For the other primes $q$, we just need some $a_q$ with $q^{e_q} \mid a_q^n - 1$. We can always take $a_q \equiv 1 \pmod{q^{e_q}}$ (then $a_q^n \equiv 1 \pmod{q^{e_q}}$). Actually, we need $a_q$ coprime to $q$, and $a_q \equiv 1 \pmod{q^{e_q}}$ works.

So the question reduces to: for each prime $p \mid n$ with $p^e \| n$, does there exist $a$ coprime to $p$ with $p^e \mid a^n - 1$ but $p^{2e} \nmid a^n - 1$?

If such $a$ exists for any prime $p \mid n$, then $n \notin S$.

So $n \in S$ iff for every prime $p \mid n$ with $p^e \| n$, for all $a$ coprime to $p$, $p^e \mid a^n - 1 \implies p^{2e} \mid a^n - 1$.

Now, this is a condition for each prime separately, with the exponent being $n$ (not $p^e$).

Let me analyze this. For odd prime $p$ with $p^e \| n$:

The group $(\mathbb{Z}/p^{2e}\mathbb{Z})^*$ is cyclic of order $p^{2e-1}(p-1)$. Let $g$ be a generator. $a = g^j$.

$a^n \equiv 1 \pmod{p^e}$ iff $\text{ord}_{p^e}(a) \mid n$. $\text{ord}_{p^e}(g^j) = \frac{p^{e-1}(p-1)}{\gcd(j, p^{e-1}(p-1))}$. So the condition is $\frac{p^{e-1}(p-1)}{\gcd(j, p^{e-1}(p-1))} \mid n$.

$a^n \equiv 1 \pmod{p^{2e}}$ iff $\text{ord}_{p^{2e}}(a) \mid n$. $\text{ord}_{p^{2e}}(g^j) = \frac{p^{2e-1}(p-1)}{\gcd(j, p^{2e-1}(p-1))}$. So the condition is $\frac{p^{2e-1}(p-1)}{\gcd(j, p^{2e-1}(p-1))} \mid n$.

We need: for all $j$, if $\frac{p^{e-1}(p-1)}{\gcd(j, p^{e-1}(p-1))} \mid n$ then $\frac{p^{2e-1}(p-1)}{\gcd(j, p^{2e-1}(p-1))} \mid n$.

Let $d_e = \gcd(j, p^{e-1}(p-1))$ and $d_{2e} = \gcd(j, p^{2e-1}(p-1))$. Note that $d_{2e} = \gcd(j, p^{2e-1}(p-1))$ and $d_e = \gcd(j, p^{e-1}(p-1))$. Since $p^{e-1}(p-1) \mid p^{2e-1}(p-1)$, we have $d_e \mid d_{2e}$. Also, $d_{2e}/d_e$ divides $p^{2e-1}/p^{e-1} = p^e$ (and is a power of $p$, since the $(p-1)$ part is the same). Actually, $d_{2e} = d_e \cdot p^{\min(v_p(j), 2e-1) - \min(v_p(j), e-1)}$ if $v_p(j) \geq e$, otherwise $d_{2e} = d_e$.

Hmm, this is getting complicated. Let me think about it differently.

The condition $\frac{p^{e-1}(p-1)}{d_e} \mid n$ means $p^{e-1}(p-1)/d_e$ divides $n$. Since $p^e \| n$, $v_p(n) = e$. Also, $p^{e-1}(p-1)/d_e$ divides $p^{e-1}(p-1)$, and $v_p(p^{e-1}(p-1)/d_e) = e - 1 - v_p(d_e)$. For this to divide $n$ (with $v_p(n) = e$), we need $e - 1 - v_p(d_e) \leq e$, i.e., $v_p(d_e) \geq -1$, always true. But we also need the $(p-1)$ part to divide $n$.

Let me write $n = p^e \cdot m$ where $\gcd(p, m) = 1$. Then $v_p(n) = e$.

$\frac{p^{e-1}(p-1)}{d_e} \mid n = p^e m$.

The $p$-part: $p^{e-1-v_p(d_e)} \mid p^e$, always true since $v_p(d_e) \leq e-1$.

The $(p-1)$-part (coprime to $p$): $\frac{p-1}{d_e/p^{v_p(d_e)}} \mid m$. Let $d_e = p^s \cdot t$ where $\gcd(t, p) = 1$ and $t \mid (p-1)$. Then the condition is $\frac{p-1}{t} \mid m$.

Similarly, $\frac{p^{2e-1}(p-1)}{d_{2e}} \mid n = p^e m$. The $p$-part: $p^{2e-1-v_p(d_{2e})} \mid p^e$, so $v_p(d_{2e}) \geq e - 1$. The $(p-1)$-part: $\frac{p-1}{t'} \mid m$ where $d_{2e} = p^{s'} \cdot t'$, $t' \mid (p-1)$, $\gcd(t', p) = 1$.

Since $d_e \mid d_{2e}$ and they share the same $(p-1)$ part (because $v_p(j)$ determines the $p$-part, and the $(p-1)$ part is $\gcd(j, p-1)$ which is the same for both), we have $t = t'$. So the $(p-1)$ conditions are the same.

The difference is in the $p$-part: for the hypothesis, we need $p^{e-1-s} \mid p^e$ (always true). For the conclusion, we need $p^{2e-1-s'} \mid p^e$, i.e., $s' \geq e - 1$.

Now, $s = \min(v_p(j), e-1)$ and $s' = \min(v_p(j), 2e-1)$.

If $v_p(j) \geq e - 1$: $s = e - 1$, $s' = \min(v_p(j), 2e-1) \geq e - 1$. So $s' \geq e - 1$. ✓.

If $v_p(j) < e - 1$: $s = v_p(j)$, $s' = v_p(j) < e - 1$. So $s' < e - 1$, and $p^{2e-1-s'} = p^{2e-1-v_p(j)}$ which has $p$-adic valuation $2e - 1 - v_p(j) > e$, so it doesn't divide $p^e$. ✗.

But wait, we also need the hypothesis to hold. The hypothesis requires $\frac{p-1}{t} \mid m$ and $p^{e-1-s} \mid p^e$ (always true). So the hypothesis holds whenever $\frac{p-1}{t} \mid m$.

If $v_p(j) < e - 1$ and $\frac{p-1}{t} \mid m$, then the hypothesis holds but the conclusion fails. So we need: there is no $j$ with $v_p(j) < e-1$ and $\frac{p-1}{\gcd(j, p-1)} \mid m$.

But $j$ can be anything. Take $j = p - 1$ (so $v_p(j) = 0 < e - 1$ for $e \geq 2$, and $\gcd(j, p-1) = p - 1$, so $\frac{p-1}{p-1} = 1 \mid m$). Then the hypothesis holds but the conclusion fails (for $e \geq 2$).

So for $e \geq 2$ (odd prime $p$ with $p^e \| n$), $n \notin S$.

For $e = 1$: $v_p(j) < e - 1 = 0$ is impossible (since $v_p(j) \geq 0$). So the condition is always satisfied. So for $e = 1$, the prime $p$ doesn't cause problems.

Wait, but I need to be more careful. For $e = 1$, $s = \min(v_p(j), 0) = 0$ and $s' = \min(v_p(j), 1)$. The hypothesis requires $p^{0} \mid p$ (true) and $\frac{p-1}{t} \mid m$. The conclusion requires $p^{1 - s'} \mid p$ (i.e., $s' \geq 0$, always true) and $\frac{p-1}{t} \mid m$ (same as hypothesis). So for $e = 1$, hypothesis $\iff$ conclusion. ✓.

So for odd primes, $p^e \| n$ causes $n \notin S$ iff $e \geq 2$.

Now for $p = 2$ with $2^{e_0} \| n$:

If $e_0 = 0$: no constraint from 2.
If $e_0 = 1$: $n$ is odd times 2. $(\mathbb{Z}/4\mathbb{Z})^* \cong \mathbb{Z}/2$. Need: for all odd $a$, if $2 \mid a^n - 1$ then $4 \mid a^n - 1$. $2 \mid a^n - 1$ for odd $a$ and $n \geq 1$: $a^n$ is odd, so $a^n - 1$ is even. ✓. Need $4 \mid a^n - 1$. For odd $a$, $a^n \equiv 1 \pmod 4$ if $n$ is even (since $a^2 \equiv 1 \pmod 4$). But $n = 2 \cdot m$ where $m$ is odd, so $n$ is even. So $a^n = (a^2)^{n/2} \equiv 1 \pmod 4$. ✓.

Wait, but what if $n$ is even? $n = 2m$ with $m$ odd. $a^n = a^{2m} = (a^2)^m \equiv 1^m = 1 \pmod 4$. ✓.

If $e_0 = 2$: $4 \| n$. Need: for all odd $a$, if $4 \mid a^n - 1$ then $16 \mid a^n - 1$.

$4 \mid a^n - 1$: $a$ odd, $n$ even (since $4 \mid n$). $a^n \equiv 1 \pmod 4$ (since $n$ even). So $4 \mid a^n - 1$ for all odd $a$. ✓ (hypothesis always holds).

Need $16 \mid a^n - 1$ for all odd $a$. $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + v_2(n) - 1$ (LTE, $n$ even). $v_2(n) \geq 2$ (since $4 \mid n$). So $v_2(a^n - 1) \geq 1 + 2 + 2 - 1 = 4$. So $16 \mid a^n - 1$. ✓.

If $e_0 = 3$: $8 \| n$. Need: for all odd $a$, if $8 \mid a^n - 1$ then $64 \mid a^n - 1$.

$8 \mid a^n - 1$: $v_2(a^n - 1) \geq 3$. $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + v_2(n) - 1$. $v_2(n) \geq 3$. So $v_2(a^n - 1) \geq 1 + 1 + 3 - 1 = 4 \geq 3$. So hypothesis always holds.

Need $64 \mid a^n - 1$: $v_2(a^n - 1) \geq 6$. $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + v_2(n) - 1$. Take $a = 3$: $v_2(2) + v_2(4) + v_2(n) - 1 = 1 + 2 + v_2(n) - 1 = 2 + v_2(n)$. Need $\geq 6$, so $v_2(n) \geq 4$. But $v_2(n) = 3$ (since $8 \| n$). So $2 + 3 = 5 < 6$. ✗.

So $e_0 = 3$ fails. Similarly, $e_0 \geq 3$ fails (take $a = 3$, $v_2(a^n - 1) = 2 + e_0$, need $\geq 2e_0$, so $e_0 \leq 2$).

So for $p = 2$: $2^{e_0} \| n$ causes $n \notin S$ iff $e_0 \geq 3$.

Combining: $n \in S$ iff:
- For every odd prime $p$, $v_p(n) \leq 1$ (i.e., $n$ is squarefree at odd primes).
- $v_2(n) \leq 2$ (i.e., $4 \nmid n$ or $8 \nmid n$... wait, $v_2(n) \leq 2$ means $8 \nmid n$).

Wait, but I need to double-check the case $e_0 = 2$ more carefully. We showed $v_2(a^n - 1) \geq 4$ when $v_2(n) \geq 2$. But we need $v_2(a^n - 1) \geq 2 \cdot 2 = 4$. So $4 \geq 4$. ✓. But this is tight. Let me verify with a specific example.

$n = 4$: $v_2(n) = 2$. $a = 3$: $v_2(3^4 - 1) = v_2(80) = 4$. $2 \cdot 2 = 4$. ✓ (just barely).

$n = 12 = 4 \cdot 3$: $v_2(n) = 2$. $a = 3$: but $\gcd(3, 12) = 3 \neq 1$, so $12 \nmid 3^{12} - 1$. Need $a$ coprime to 12. $a = 5$: $v_2(5^{12} - 1) = v_2(4) + v_2(6) + v_2(12) - 1 = 2 + 1 + 2 - 1 = 4$. Need $\geq 4$. ✓.

But wait, I should also check: is the hypothesis $8 \mid a^n - 1$ (i.e., $v_2 \geq 3$) always satisfied when $v_2(n) = 2$? $v_2(a^n - 1) \geq 1 + 1 + 2 - 1 = 3$. ✓. And we need $v_2 \geq 4$, which requires $v_2(a-1) + v_2(a+1) \geq 2$. For odd $a$, one of $a \pm 1$ is $\equiv 0 \pmod 4$, so $v_2(a-1) + v_2(a+1) \geq 2 + 1 = 3 \geq 2$. ✓.

Actually, I realize I need to be more careful. The condition is $v_2(a^n - 1) \geq 2 e_0$ where $e_0 = v_2(n)$. We have $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + v_2(n) - 1 = v_2(a-1) + v_2(a+1) + e_0 - 1$.

Need: $v_2(a-1) + v_2(a+1) + e_0 - 1 \geq 2 e_0$, i.e., $v_2(a-1) + v_2(a+1) \geq e_0 + 1$.

For odd $a$, $v_2(a-1) + v_2(a+1) \geq 3$ (as argued). So need $e_0 + 1 \leq 3$, i.e., $e_0 \leq 2$.

But wait, the hypothesis is $2^{e_0} \mid a^n - 1$, which requires $v_2(a^n - 1) \geq e_0$, i.e., $v_2(a-1) + v_2(a+1) \geq 1$. This is always true for odd $a$. So the hypothesis is always satisfied, and we need the conclusion $v_2(a^n - 1) \geq 2e_0$ for all odd $a$.

The minimum of $v_2(a-1) + v_2(a+1)$ over odd $a$ is 3 (achieved at $a = 3$: $v_2(2) + v_2(4) = 3$, or $a = 5$: $v_2(4) + v_2(6) = 3$). So we need $3 + e_0 - 1 \geq 2e_0$, i.e., $e_0 \leq 2$.

So $v_2(n) \leq 2$ is necessary and sufficient for the 2-part.

Now, combining everything: $n \in S$ iff:
1. $v_2(n) \leq 2$
2. For all odd primes $p$, $v_p(n) \leq 1$ (i.e., $n$ is squarefree at odd primes)

Equivalently, $n$ is squarefree except possibly for a factor of $4$ (i.e., $v_2(n) \in \{0, 1, 2\}$ and all odd prime exponents are 0 or 1).

Let me verify this against our computations:
- $n = 2 = 2$: $v_2 = 1 \leq 2$, squarefree. ✓
- $n = 3$: prime. ✓
- $n = 4 = 2^2$: $v_2 = 2 \leq 2$, no odd primes. ✓
- $n = 5$: prime. ✓
- $n = 6 = 2 \cdot 3$: $v_2 = 1$, squarefree. ✓
- $n = 7$: prime. ✓
- $n = 8 = 2^3$: $v_2 = 3 > 2$. ✗
- $n = 9 = 3^2$: $v_3 = 2 > 1$. ✗
- $n = 10 = 2 \cdot 5$: ✓
- $n = 11$: prime. ✓
- $n = 12 = 2^2 \cdot 3$: $v_2 = 2$, $v_3 = 1$. ✓
- $n = 13$: prime. ✓
- $n = 14 = 2 \cdot 7$: ✓
- $n = 15 = 3 \cdot 5$: ✓
- $n = 16 = 2^4$: $v_2 = 4 > 2$. ✗
- $n = 17$: prime. ✓
- $n = 18 = 2 \cdot 3^2$: $v_3 = 2 > 1$. ✗
- $n = 19$: prime. ✓
- $n = 20 = 2^2 \cdot 5$: $v_2 = 2$, $v_5 = 1$. ✓

This matches perfectly!

So $S \cap \{2, \ldots, 20\} = \{2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17, 19, 20\}$.

Sum $= 2 + 3 + 4 + 5 + 6 + 7 + 10 + 11 + 12 + 13 + 14 + 15 + 17 + 19 + 20$.

Let me compute: $2+3 = 5$, $+4 = 9$, $+5 = 14$, $+6 = 20$, $+7 = 27$, $+10 = 37$, $+11 = 48$, $+12 = 60$, $+13 = 73$, $+14 = 87$, $+15 = 102$, $+17 = 119$, $+19 = 138$, $+20 = 158$.

Sum = 158.

Now let me write up the proof properly. I need to make sure my argument is rigorous, especially the CRT decomposition part.

Let me re-examine the key steps:

1. $n \mid a^n - 1 \implies \gcd(a, n) = 1$ (since if $p \mid \gcd(a, n)$, then $p \mid a$ and $p \mid n$, so $a^n \equiv 0 \pmod p$, $a^n - 1 \equiv -1 \pmod p$, contradiction).

2. The condition is: for all $a$ with $\gcd(a, n) = 1$, $a^n \equiv 1 \pmod n \implies a^n \equiv 1 \pmod{n^2}$.

3. By CRT, this decomposes into prime power conditions. Specifically, $n \in S$ iff for every prime $p$ with $p^e \| n$, the following holds: for all $a$ coprime to $p$, $p^e \mid a^n - 1 \implies p^{2e} \mid a^n - 1$.

Wait, I need to be more careful about the decomposition. The condition "for all $a$ coprime to $n$, $a^n \equiv 1 \pmod n \implies a^n \equiv 1 \pmod{n^2}$" — does this decompose?

The forward direction: if $n \in S$, then for each prime $p \mid n$, the local condition holds. This is because if the local condition fails for some $p$, we can construct a global counterexample via CRT.

The backward direction: if each local condition holds, then $n \in S$. This is because if $a^n \equiv 1 \pmod n$, then for each $p \mid n$, $p^e \mid a^n - 1$, and the local condition gives $p^{2e} \mid a^n - 1$, so $n^2 \mid a^n - 1$.

The backward direction is clear. For the forward direction: suppose the local condition fails for prime $p$, i.e., there exists $a_0$ coprime to $p$ with $p^e \mid a_0^n - 1$ but $p^{2e} \nmid a_0^n - 1$. We need to find $a$ coprime to $n$ with $n \mid a^n - 1$ but $n^2 \nmid a^n - 1$.

For each prime $q \mid n$, $q \neq p$, we need $q^{e_q} \mid a^n - 1$. We can choose $a \equiv 1 \pmod{q^{e_q}}$ for all such $q$ (then $a^n \equiv 1 \pmod{q^{e_q}}$). And we choose $a \equiv a_0 \pmod{p^{2e}}$ (or mod some appropriate power). By CRT (since $p$ and $q$ are distinct primes), we can find such $a$.

But wait, we need $a$ to be coprime to $n$. Since $a \equiv a_0 \pmod{p^{2e}}$ and $\gcd(a_0, p) = 1$, we have $\gcd(a, p) = 1$. And $a \equiv 1 \pmod{q^{e_q}}$ for other primes, so $\gcd(a, q) = 1$. So $\gcd(a, n) = 1$. ✓.

And $a^n \equiv a_0^n \pmod{p^{2e}}$ (since $a \equiv a_0 \pmod{p^{2e}}$), so $p^e \mid a^n - 1$ but $p^{2e} \nmid a^n - 1$. And $a^n \equiv 1 \pmod{q^{e_q}}$ for all other $q$. So $n \mid a^n - 1$ but $n^2 \nmid a^n - 1$. ✓.

Great, so the decomposition is valid.

Now, for the local condition at odd prime $p$ with $p^e \| n$:

Using the cyclic group structure, I showed that for $e \geq 2$, taking $a = g^{p-1}$ (where $g$ is a primitive root mod $p^{2e}$) gives a counterexample. Let me verify this more carefully.

$g$ has order $p^{2e-1}(p-1)$ mod $p^{2e}$. $a = g^{p-1}$ has order $p^{2e-1}$ mod $p^{2e}$ and order $p^{e-1}$ mod $p^e$.

$a^n \pmod{p^e}$: order of $a$ mod $p^e$ is $p^{e-1}$. $a^n \equiv 1 \pmod{p^e}$ iff $p^{e-1} \mid n$. Since $p^e \| n$, $p^e \mid n$, so $p^{e-1} \mid n$. ✓. So hypothesis holds.

$a^n \pmod{p^{2e}}$: order of $a$ mod $p^{2e}$ is $p^{2e-1}$. $a^n \equiv 1 \pmod{p^{2e}}$ iff $p^{2e-1} \mid n$. Since $p^e \| n$ (and $e \geq 2$), $v_p(n) = e < 2e - 1$. So $p^{2e-1} \nmid n$. ✗. So conclusion fails.

So for $e \geq 2$, the local condition fails. ✓.

For $e = 1$: $a = g^{p-1}$ has order $1$ mod $p$ (i.e., $a \equiv 1 \pmod p$) and order $p$ mod $p^2$. $a^n \equiv 1 \pmod p$ always (since $a \equiv 1 \pmod p$). $a^n \equiv 1 \pmod{p^2}$ iff $p \mid n$. Since $p \| n$, $p \mid n$. ✓. So this particular $a$ works.

But we need to check ALL $a$ coprime to $p$. Let $a = g^j$ where $g$ is a primitive root mod $p^2$ (order $p(p-1)$). $a^n \equiv 1 \pmod p$ iff $(p-1) \mid jn$... wait, the order of $g$ mod $p$ is $p - 1$. So $a^n \equiv 1 \pmod p$ iff $(p-1) \mid jn$.

$a^n \equiv 1 \pmod{p^2}$: order of $g$ mod $p^2$ is $p(p-1)$. So $a^n \equiv 1 \pmod{p^2}$ iff $p(p-1) \mid jn$.

Since $p \| n$, $v_p(n) = 1$. So $p(p-1) \mid jn$ iff $(p-1) \mid jn$ and $p \mid jn / \gcd(jn, p(p-1))$... hmm, let me think differently.

$p(p-1) \mid jn$: since $\gcd(p, p-1) = 1$, this is equivalent to $p \mid jn$ and $(p-1) \mid jn$. Since $p \mid n$ (as $p \| n$), $p \mid jn$ is automatic. And $(p-1) \mid jn$ is the hypothesis. So $p(p-1) \mid jn$ iff $(p-1) \mid jn$. So hypothesis $\iff$ conclusion. ✓.

So for $e = 1$ (odd prime), the local condition always holds. ✓.

For $p = 2$ with $2^{e_0} \| n$:

Using LTE: for odd $a$ and even $n$, $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + v_2(n) - 1$.

The hypothesis is $v_2(a^n - 1) \geq e_0$, which is $v_2(a-1) + v_2(a+1) \geq e_0 - v_2(n) + 1 = 1$ (since $v_2(n) = e_0$). This is always true for odd $a$.

The conclusion is $v_2(a^n - 1) \geq 2e_0$, which is $v_2(a-1) + v_2(a+1) \geq e_0 + 1$.

The minimum of $v_2(a-1) + v_2(a+1)$ for odd $a$ is 3 (at $a = \pm 3 \pmod 8$... actually, for $a = 3$: $v_2(2) + v_2(4) = 1 + 2 = 3$; for $a = 5$: $v_2(4) + v_2(6) = 2 + 1 = 3$; for $a = 7$: $v_2(6) + v_2(8) = 1 + 3 = 4$; for $a = 1$: $v_2(0) + v_2(2) = \infty + 1 = \infty$). So the minimum is 3.

So the conclusion holds for all odd $a$ iff $3 \geq e_0 + 1$, i.e., $e_0 \leq 2$.

Wait, but I need to be careful about $e_0 = 0$ (i.e., $n$ odd). If $e_0 = 0$, there's no 2-part, so no constraint from $p = 2$.

And for $e_0 = 1$: $n$ is even, $v_2(n) = 1$. LTE applies (since $n$ is even). $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + 1 - 1 = v_2(a-1) + v_2(a+1) \geq 3$. Need $\geq 2 \cdot 1 = 2$. ✓.

For $e_0 = 2$: $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + 2 - 1 = v_2(a-1) + v_2(a+1) + 1 \geq 4$. Need $\geq 4$. ✓.

For $e_0 = 3$: $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + 2 \geq 5$. Need $\geq 6$. $5 < 6$. ✗ (at $a = 3$).

So $v_2(n) \leq 2$ is the condition.

But wait, I also need to handle the case $e_0 = 0$ but $n$ even... no, $e_0 = 0$ means $n$ is odd. And if $n$ is odd, the hypothesis $2 \mid a^n - 1$ requires $a$ odd, and then $a^n \equiv a \pmod 2$... actually if $n$ is odd and $a$ is odd, $a^n$ is odd, $a^n - 1$ is even, so $2 \mid a^n - 1$. But $e_0 = 0$ means $2 \nmid n$, so there's no 2-part in the condition. The condition only involves primes dividing $n$.

OK so the complete characterization is:

$n \in S$ iff $v_2(n) \leq 2$ and $v_p(n) \leq 1$ for all odd primes $p$.

Equivalently, $n$ is squarefree at all odd primes, and $v_2(n) \in \{0, 1, 2\}$.

Now let me list all $n \in S$ with $1 < n \leq 20$:

- $n = 2 = 2$: ✓
- $n = 3 = 3$: ✓
- $n = 4 = 2^2$: ✓
- $n = 5 = 5$: ✓
- $n = 6 = 2 \cdot 3$: ✓
- $n = 7 = 7$: ✓
- $n = 8 = 2^3$: ✗ ($v_2 = 3$)
- $n = 9 = 3^2$: ✗ ($v_3 = 2$)
- $n = 10 = 2 \cdot 5$: ✓
- $n = 11 = 11$: ✓
- $n = 12 = 2^2 \cdot 3$: ✓
- $n = 13 = 13$: ✓
- $n = 14 = 2 \cdot 7$: ✓
- $n = 15 = 3 \cdot 5$: ✓
- $n = 16 = 2^4$: ✗ ($v_2 = 4$)
- $n = 17 = 17$: ✓
- $n = 18 = 2 \cdot 3^2$: ✗ ($v_3 = 2$)
- $n = 19 = 19$: ✓
- $n = 20 = 2^2 \cdot 5$: ✓

$S \cap \{2, \ldots, 20\} = \{2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17, 19, 20\}$.

Sum $= 2 + 3 + 4 + 5 + 6 + 7 + 10 + 11 + 12 + 13 + 14 + 15 + 17 + 19 + 20 = 158$.

Let me now write up the proof.

Actually, wait. I want to double-check the LTE application. LTE for $p = 2$ says: if $2 \mid a - b$ and $2 \mid a + b$ (i.e., $a, b$ both odd) and $n$ is even, then $v_2(a^n - b^n) = v_2(a - b) + v_2(a + b) + v_2(n) - 1$.

With $b = 1$, $a$ odd, $n$ even: $v_2(a^n - 1) = v_2(a - 1) + v_2(a + 1) + v_2(n) - 1$. ✓.

But what if $n$ is odd? Then LTE doesn't apply in this form. If $n$ is odd and $a$ is odd, $v_2(a^n - 1) = v_2(a - 1)$ (by the simpler form of LTE for $p = 2$ when $n$ is odd: $v_2(a^n - b^n) = v_2(a - b)$).

But in our case, if $e_0 \geq 1$, then $n$ is even, so LTE applies. If $e_0 = 0$, $n$ is odd, and there's no 2-part to worry about. So we're fine.

Also, I should handle the case $e_0 = 0$ more carefully. If $n$ is odd, the condition from $p = 2$ is vacuous (2 doesn't divide $n$). So we only need to check odd primes.

Let me also verify the case $n = 1$ is excluded (the problem says $n > 1$). ✓.

Now, one more        — AI历史解题过程（thinking）
#   polymath_05452         — 题目ID

# Solver Task

You are a mathematical problem analysis assistant. You will NOT solve any problems.
You will analyze the relationship between a standard solution and an AI's attempted solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search.
- All information you need is in this AGENTS.md file.
- Output your analysis directly in your response (in this TUI).
- End your analysis with a line containing exactly: `### ANALYSIS COMPLETE`

## Analysis Task

You are given three inputs:
1. **Problem** — a math competition problem
2. **Standard Solution** — the correct solution from the problem bank
3. **AI's Thinking** — an AI's attempted solution process (its reasoning when it tried to solve the problem, but failed)

Your task: analyze WHY the AI failed, by comparing its thinking with the standard solution.

### Dimension 1: Failure Type

Compare the standard solution's key approach with the AI's thinking:

- **DIRECTION_ERROR**: The AI's thinking went in a fundamentally wrong direction. The standard solution uses a specific mathematical approach that the AI never considered. The AI was exploring a completely different strategy. The failure is about *which direction to explore*, not about running out of time.

- **TOKEN_LIMIT**: The AI's thinking was going in the RIGHT direction — it was using the same key approach as the standard solution (or a valid alternative) — but ran out of tokens before completing the proof. The failure is about *not enough time*, not about *wrong direction*.

- **CONNECTION_ERROR**: The AI didn't really attempt the problem. The thinking is very short, contains connection errors, or has no meaningful mathematical content. This is a technical failure, not a mathematical one.

- **PARTIAL_PROGRESS**: The AI's thinking was partially in the right direction — it identified some key ideas from the standard solution — but missed the crucial turning point. The AI was on the right track but took a wrong turn at a critical juncture.

### Dimension 2: Key Turning Point Type

If the verdict is DIRECTION_ERROR or PARTIAL_PROGRESS, identify what type of key turning point the standard solution uses:

1. **mod_p_grouping**: The standard solution uses modular arithmetic (mod p, where p is small/obvious like 4, 8) to group/categorize objects and find a contradiction or hidden structure.

2. **mod_p_non_obvious**: The standard solution uses modular arithmetic where the prime p is NOT obvious from the problem statement (e.g., mod 11, mod p where p needs to be discovered through analysis).

3. **quadratic_residue_euler**: The standard solution uses quadratic residues, Legendre symbols, or Euler's criterion.

4. **lte_lemma**: The standard solution uses the Lifting The Exponent (LTE) lemma.

5. **p_adic_valuation**: The standard solution uses p-adic valuation (v_p) analysis.

6. **multi_step_mod_p**: The standard solution uses multiple steps of modular arithmetic analysis (not just one mod operation).

7. **crt**: The standard solution uses the Chinese Remainder Theorem (combining information from multiple moduli).

8. **permutation_polynomial**: The standard solution uses properties of permutation polynomials over finite fields.

9. **finite_field_structure**: The standard solution exploits the structure of finite fields (Z/pZ, F_p, F_p^k).

10. **other**: None of the above categories fit. Describe the technique in dimension2_explanation.

### Output Format

Output your analysis in this EXACT XML format. The XML must be well-formed and parseable.

```xml
<analysis>
  <problem_id>polymath_05452</problem_id>
  <dimension1_verdict>DIRECTION_ERROR|TOKEN_LIMIT|CONNECTION_ERROR|PARTIAL_PROGRESS</dimension1_verdict>
  <dimension1_explanation>1-3 sentences explaining the verdict</dimension1_explanation>
  <dimension2_turning_point_type>mod_p_grouping|mod_p_non_obvious|quadratic_residue_euler|lte_lemma|p_adic_valuation|multi_step_mod_p|crt|permutation_polynomial|finite_field_structure|other</dimension2_turning_point_type>
  <dimension2_explanation>1-3 sentences describing the key turning point in the standard solution</dimension2_explanation>
  <ai_direction_summary>1 sentence describing what direction the AI's thinking went</ai_direction_summary>
  <standard_solution_key_technique>1 sentence describing the key technique in the standard solution</standard_solution_key_technique>
  <confidence>high|medium|low</confidence>
</analysis>
```

After the XML block, output exactly: `### ANALYSIS COMPLETE`

**Rules:**
- The XML must be inside a ```xml code block
- Do NOT add any text before or after the XML block (except ### ANALYSIS COMPLETE)
- If the AI's thinking is too short to analyze (< 500 chars of mathematical content), output CONNECTION_ERROR
- If you cannot determine the turning point type, use "other" and explain in dimension2_explanation

## Problem

Find all $n > 1$, $n \in \mathbb{N}$ such that for all $a \in \mathbb{N}$, if $a^n - 1$ is divisible by $n$, then $a^n - 1$ is also divisible by $n^2$.
Let $S$ be the set of all such values of $n$. Calculate the sum of all $n \in S$ such that $1 < n \le 20$.

## Standard Solution

From the original solution, the numbers $n$ that satisfy the condition are square-free integers greater than 1 and $n = 4$.
Square-free numbers are those whose prime factorization contains no repeated factors.
For $1 < n \le 20$, the square-free numbers are: 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19.
Additionally, the number $n = 4$ is identified as a solution.
We sum these values: $2 + 3 + 4 + 5 + 6 + 7 + 10 + 11 + 13 + 14 + 15 + 17 + 19 = 126$.

## AI's Thinking (Attempted Solution Process)

Let me analyze the problem carefully.

We need to find all $n > 1$, $n \in \mathbb{N}$ such that: for all $a \in \mathbb{N}$, if $n \mid a^n - 1$, then $n^2 \mid a^n - 1$.

Let me check for answer leaks first. The problem text doesn't contain any leaked answers or solutions. Good.

Now let me think about this problem. We need $n$ such that for all $a$, $n \mid a^n - 1 \implies n^2 \mid a^n - 1$.

First, note that $a$ ranges over all natural numbers. Let me think about what conditions this imposes.

Let's consider $n$ with prime factorization $n = p_1^{e_1} \cdots p_k^{e_k}$.

The condition $n \mid a^n - 1$ means $p_i^{e_i} \mid a^n - 1$ for all $i$.

The condition $n^2 \mid a^n - 1$ means $p_i^{2e_i} \mid a^n - 1$ for all $i$.

So we need: for all $a$, if $p_i^{e_i} \mid a^n - 1$ for all $i$, then $p_i^{2e_i} \mid a^n - 1$ for all $i$.

Let me think about this differently. Let's consider specific values of $a$.

First, consider $a$ such that $\gcd(a, n) = 1$. Then by Euler's theorem, $a^{\phi(n)} \equiv 1 \pmod{n}$, but we need $a^n \equiv 1 \pmod{n}$.

Actually, let's think about when $n \mid a^n - 1$ can happen. If $\gcd(a, n) > 1$, say $p \mid a$ and $p \mid n$, then $a^n \equiv 0 \pmod{p}$, so $a^n - 1 \equiv -1 \pmod{p}$, which means $p \nmid a^n - 1$, so $n \nmid a^n - 1$. So the condition $n \mid a^n - 1$ automatically implies $\gcd(a, n) = 1$.

So we only need to consider $a$ with $\gcd(a, n) = 1$.

Now, the condition becomes: for all $a$ with $\gcd(a, n) = 1$, if $a^n \equiv 1 \pmod{n}$, then $a^n \equiv 1 \pmod{n^2}$.

Hmm, but actually we need it for ALL $a \in \mathbb{N}$, and as shown, only $a$ with $\gcd(a, n) = 1$ can satisfy $n \mid a^n - 1$.

So the condition is: for all $a$ coprime to $n$, $a^n \equiv 1 \pmod{n} \implies a^n \equiv 1 \pmod{n^2}$.

Let me think about this using the structure of $(\mathbb{Z}/n^2\mathbb{Z})^*$.

Actually, let me think about it more carefully. We need: for all $a$ coprime to $n$, if $a^n \equiv 1 \pmod{n}$, then $a^n \equiv 1 \pmod{n^2}$.

Let me consider the map $\phi: (\mathbb{Z}/n^2\mathbb{Z})^* \to (\mathbb{Z}/n\mathbb{Z})^*$, the natural reduction mod $n$. The kernel of this map has order $n^2 \cdot \frac{\phi(n)}{\phi(n)} / ... $ wait let me think again.

$|(\mathbb{Z}/n^2\mathbb{Z})^*| = \phi(n^2)$ and $|(\mathbb{Z}/n\mathbb{Z})^*| = \phi(n)$. The reduction map is surjective, and the kernel has order $\phi(n^2)/\phi(n)$.

For $n = p_1^{e_1} \cdots p_k^{e_k}$, $\phi(n^2)/\phi(n) = \prod p_i^{e_i} = n$.

So the kernel $K$ of the reduction map has order $n$.

Now, the condition is: for every $a$ coprime to $n$ with $a^n \equiv 1 \pmod{n}$, we need $a^n \equiv 1 \pmod{n^2}$.

In terms of the group structure: let $\bar{a}$ be the image of $a$ in $(\mathbb{Z}/n^2\mathbb{Z})^*$. The condition $a^n \equiv 1 \pmod{n}$ means $\bar{a}^n \in K$ (the kernel). The condition $a^n \equiv 1 \pmod{n^2}$ means $\bar{a}^n = 1$ in $(\mathbb{Z}/n^2\mathbb{Z})^*$.

So the condition is: for all $\bar{a} \in (\mathbb{Z}/n^2\mathbb{Z})^*$, if $\bar{a}^n \in K$, then $\bar{a}^n = 1$.

In other words, the map $f: (\mathbb{Z}/n^2\mathbb{Z})^* \to K$ given by $f(\bar{a}) = \bar{a}^n$ should satisfy: $\ker(f) = \{\bar{a} : \bar{a}^n = 1\}$ equals $\{\bar{a} : \bar{a}^n \in K\}$... no wait.

Let me rephrase. The set of $\bar{a}$ with $\bar{a}^n \in K$ is $f^{-1}(K) = \{\bar{a} : \bar{a}^n \in K\}$. But $\bar{a}^n \in K$ iff $\bar{a}^n \equiv 1 \pmod{n}$, which is always... no. $\bar{a}^n \in K$ means $\bar{a}^n \equiv 1 \pmod{n}$, i.e., $a^n \equiv 1 \pmod n$.

Hmm wait, $K$ is the kernel of reduction mod $n$, so $K = \{x \in (\mathbb{Z}/n^2\mathbb{Z})^* : x \equiv 1 \pmod{n}\}$. So $\bar{a}^n \in K$ iff $\bar{a}^n \equiv 1 \pmod n$.

And the condition is: $\bar{a}^n \in K \implies \bar{a}^n = 1$ (in $(\mathbb{Z}/n^2\mathbb{Z})^*$).

So the image of the $n$-th power map, restricted to those elements whose $n$-th power lands in $K$, must be trivial. Equivalently, the only element of $K$ that is an $n$-th power in $(\mathbb{Z}/n^2\mathbb{Z})^*$ is the identity.

So: $K \cap \{n\text{-th powers in } (\mathbb{Z}/n^2\mathbb{Z})^*\} = \{1\}$.

Let me think about this differently. Consider the $n$-th power map on $(\mathbb{Z}/n^2\mathbb{Z})^*$. The image is the subgroup of $n$-th powers. We need this image to intersect $K$ trivially.

Since $|K| = n$, and the image of the $n$-th power map has size $|(\mathbb{Z}/n^2\mathbb{Z})^*| / |\ker(\text{$n$-th power})| = \phi(n^2) / d$ where $d = |\{x : x^n = 1\}|$.

Hmm, this is getting complicated. Let me try a more direct approach and just check small values.

Let me check $n = 2$ through $n = 20$.

For each $n$, I need: for all $a$ coprime to $n$, $a^n \equiv 1 \pmod n \implies a^n \equiv 1 \pmod{n^2}$.

**$n = 2$**: Need: for all odd $a$, $a^2 \equiv 1 \pmod 2 \implies a^2 \equiv 1 \pmod 4$. For odd $a$, $a^2 \equiv 1 \pmod 8$ (since odd squares are $\equiv 1 \pmod 8$), so certainly $a^2 \equiv 1 \pmod 4$. And $a^2 \equiv 1 \pmod 2$ is always true for odd $a$. So the condition holds. $n = 2 \in S$.

Wait, but I need to be more careful. The condition is for ALL $a \in \mathbb{N}$, if $n \mid a^n - 1$ then $n^2 \mid a^n - 1$. For $n = 2$: if $2 \mid a^2 - 1$, then $4 \mid a^2 - 1$. $2 \mid a^2 - 1$ iff $a$ is odd. For odd $a$, $a^2 \equiv 1 \pmod 8$, so $4 \mid a^2 - 1$. ✓. So $n = 2 \in S$.

**$n = 3$**: Need: if $3 \mid a^3 - 1$, then $9 \mid a^3 - 1$. $3 \mid a^3 - 1$ iff $a \equiv 1 \pmod 3$ (since $a^3 \equiv a \pmod 3$ by Fermat). So $a \equiv 1 \pmod 3$. Then $a = 3k + 1$. $a^3 = 27k^3 + 27k^2 + 9k + 1$, so $a^3 - 1 = 9k(3k^2 + 3k + 1)$. So $9 \mid a^3 - 1$. ✓. So $n = 3 \in S$.

**$n = 4$**: Need: if $4 \mid a^4 - 1$, then $16 \mid a^4 - 1$. $4 \mid a^4 - 1$ requires $a$ odd (since if $a$ even, $a^4 - 1$ is odd, not divisible by 2, let alone 4). For odd $a$, $a^4 \equiv 1 \pmod{16}$? Let's check: $a = 1$: $1 - 1 = 0$, $16 \mid 0$. ✓. $a = 3$: $3^4 = 81$, $81 - 1 = 80$, $16 \mid 80$? $80/16 = 5$. ✓. $a = 5$: $5^4 = 625$, $625 - 1 = 624$, $624/16 = 39$. ✓. Actually, for odd $a$, $a^2 \equiv 1 \pmod 8$, so $a^4 \equiv 1 \pmod{16}$... let me verify. $a = 2k+1$, $a^2 = 4k^2 + 4k + 1 = 4k(k+1) + 1$. Since $k(k+1)$ is even, $a^2 = 8m + 1$ for some $m$. Then $a^4 = (8m+1)^2 = 64m^2 + 16m + 1 = 16(4m^2 + m) + 1$. So $a^4 \equiv 1 \pmod{16}$. ✓. So for all odd $a$, $16 \mid a^4 - 1$. And $4 \mid a^4 - 1$ is automatic for odd $a$. So $n = 4 \in S$.

**$n = 5$**: Need: if $5 \mid a^5 - 1$, then $25 \mid a^5 - 1$. $5 \mid a^5 - 1$ iff $a \equiv 1 \pmod 5$ (by Fermat, $a^5 \equiv a \pmod 5$). So $a = 5k + 1$. $a^5 = (5k+1)^5 = 1 + 5 \cdot 5k + \binom{5}{2}(5k)^2 + \ldots = 1 + 25k + 250k^2 + \ldots$. So $a^5 - 1 = 25k + 250k^2 + \ldots = 25(k + 10k^2 + \ldots)$. So $25 \mid a^5 - 1$. ✓. So $n = 5 \in S$.

Hmm, it seems like for primes $p$, this might always work. Let me think about why.

For prime $p$: $p \mid a^p - 1$ iff $a \equiv 1 \pmod p$ (by Fermat's little theorem, $a^p \equiv a \pmod p$, so $a^p - 1 \equiv a - 1 \pmod p$). So $a = kp + 1$. Then $a^p = (1 + kp)^p = 1 + p \cdot kp + \binom{p}{2}(kp)^2 + \ldots = 1 + kp^2 + \ldots$. The second term is $kp^2$, and all subsequent terms have at least $p^2$ (actually $(kp)^2 = k^2 p^2$ times $\binom{p}{2}$, so at least $p^2$). So $a^p - 1 \equiv kp^2 \pmod{p^3}$, which means $p^2 \mid a^p - 1$. ✓.

So all primes are in $S$. That gives us 2, 3, 5, 7, 11, 13, 17, 19.

Now let me check composite numbers.

**$n = 6 = 2 \cdot 3$**: Need: if $6 \mid a^6 - 1$, then $36 \mid a^6 - 1$. $6 \mid a^6 - 1$ means $2 \mid a^6 - 1$ and $3 \mid a^6 - 1$. $2 \mid a^6 - 1$ iff $a$ odd. $3 \mid a^6 - 1$: by Fermat, $a^3 \equiv a \pmod 3$, so $a^6 \equiv a^2 \pmod 3$. So $3 \mid a^6 - 1$ iff $a^2 \equiv 1 \pmod 3$ iff $a \not\equiv 0 \pmod 3$, i.e., $\gcd(a, 3) = 1$.

So $6 \mid a^6 - 1$ iff $a$ is odd and $\gcd(a, 3) = 1$, i.e., $\gcd(a, 6) = 1$.

Now need $36 \mid a^6 - 1$, i.e., $4 \mid a^6 - 1$ and $9 \mid a^6 - 1$.

For odd $a$: $a^2 \equiv 1 \pmod 8$, so $a^6 = (a^2)^3 \equiv 1 \pmod 8$, so $4 \mid a^6 - 1$. ✓.

For $\gcd(a, 3) = 1$: $a^6 - 1 = (a^3 - 1)(a^3 + 1)$. We need $9 \mid a^6 - 1$. If $a \equiv 1 \pmod 3$, then $a^3 \equiv 1 \pmod 9$ (by the same argument as $n = 3$ case: $a = 3k+1$, $a^3 = 27k^3 + 27k^2 + 9k + 1$, so $a^3 \equiv 1 \pmod 9$). So $9 \mid a^3 - 1$, hence $9 \mid a^6 - 1$. ✓.

If $a \equiv 2 \pmod 3$, then $a^3 \equiv 8 \equiv -1 \pmod 9$? Let me check: $a = 2$: $2^3 = 8$, $8 \equiv -1 \pmod 9$. So $9 \mid a^3 + 1$, hence $9 \mid a^6 - 1$. ✓.

Actually, let me verify more carefully. $a \equiv 2 \pmod 3$, so $a = 3k + 2$. $a^3 = (3k+2)^3 = 27k^3 + 54k^2 + 36k + 8 = 9(3k^3 + 6k^2 + 4k) + 8$. So $a^3 \equiv 8 \equiv -1 \pmod 9$. So $9 \mid a^3 + 1$, and $a^6 - 1 = (a^3-1)(a^3+1)$, so $9 \mid a^6 - 1$. ✓.

So $n = 6 \in S$.

**$n = 7$**: Prime, so in $S$ (as shown above).

**$n = 8 = 2^3$**: Need: if $8 \mid a^8 - 1$, then $64 \mid a^8 - 1$. $8 \mid a^8 - 1$ requires $a$ odd. For odd $a$, $a^2 \equiv 1 \pmod 8$, so $a^8 = (a^2)^4 \equiv 1 \pmod 8$. So $8 \mid a^8 - 1$ for all odd $a$.

Now need $64 \mid a^8 - 1$ for all odd $a$. $a^2 \equiv 1 \pmod 8$, so $a^2 = 8m + 1$. $a^8 = (8m+1)^4 = 1 + 4 \cdot 8m + 6 \cdot 64m^2 + \ldots = 1 + 32m + 384m^2 + \ldots$. So $a^8 - 1 = 32m + 384m^2 + \ldots = 32(m + 12m^2 + \ldots)$. For $64 \mid a^8 - 1$, we need $2 \mid m + 12m^2 + \ldots$, i.e., $m$ even.

But $m$ might not be even. Let's check $a = 3$: $3^2 = 9 = 8 \cdot 1 + 1$, so $m = 1$ (odd). $3^8 = 6561$. $6561 - 1 = 6560$. $6560 / 64 = 102.5$. So $64 \nmid 6560$. Let me verify: $6560 = 64 \cdot 102 + 32$. So $64 \nmid 6560$.

So $n = 8 \notin S$.

**$n = 9 = 3^2$**: Need: if $9 \mid a^9 - 1$, then $81 \mid a^9 - 1$. $9 \mid a^9 - 1$ requires $\gcd(a, 3) = 1$. For $\gcd(a, 3) = 1$, $a^3 \equiv \pm 1 \pmod 9$ (as shown above). So $a^9 = (a^3)^3$. If $a^3 \equiv 1 \pmod 9$, then $a^9 \equiv 1 \pmod 9$. If $a^3 \equiv -1 \pmod 9$, then $a^9 \equiv -1 \pmod 9$, so $9 \nmid a^9 - 1$.

So $9 \mid a^9 - 1$ iff $a^3 \equiv 1 \pmod 9$, i.e., $a \equiv 1 \pmod 3$ (and more specifically, $a \equiv 1 \pmod 3$ gives $a^3 \equiv 1 \pmod 9$).

Wait, let me be more careful. $a \equiv 1 \pmod 3$: $a = 3k + 1$, $a^3 = 27k^3 + 27k^2 + 9k + 1 \equiv 1 \pmod 9$. So $a^3 \equiv 1 \pmod 9$.

$a \equiv 2 \pmod 3$: $a = 3k + 2$, $a^3 \equiv 8 \equiv -1 \pmod 9$. So $a^3 \equiv -1 \pmod 9$.

So $9 \mid a^9 - 1$ iff $a \equiv 1 \pmod 3$ (and $\gcd(a, 3) = 1$, which is automatic).

Now, for $a \equiv 1 \pmod 3$, need $81 \mid a^9 - 1$.

$a = 3k + 1$. $a^9 = (3k+1)^9 = 1 + 9 \cdot 3k + \binom{9}{2}(3k)^2 + \ldots = 1 + 27k + 36 \cdot 9k^2 + \ldots = 1 + 27k + 324k^2 + \ldots$.

$a^9 - 1 = 27k + 324k^2 + \ldots = 27(k + 12k^2 + \ldots)$.

For $81 \mid a^9 - 1$, need $3 \mid k + 12k^2 + \ldots$, i.e., $3 \mid k$ (since $12k^2 \equiv 0 \pmod 3$ and higher terms... let me check).

Actually, let me be more careful. $a^9 - 1 = \sum_{j=1}^{9} \binom{9}{j} (3k)^j = 27k + \binom{9}{2} \cdot 9k^2 + \binom{9}{3} \cdot 27k^3 + \ldots$

$= 27k + 36 \cdot 9k^2 + 84 \cdot 27k^3 + \ldots$

$= 27k + 324k^2 + 2268k^3 + \ldots$

$= 27(k + 12k^2 + 84k^3 + \ldots)$

For $81 \mid a^9 - 1$, need $3 \mid k + 12k^2 + 84k^3 + \ldots$. Since $12 \equiv 0$, $84 \equiv 0 \pmod 3$, this reduces to $3 \mid k$.

But $k$ can be anything. If $k = 1$, $a = 4$, $a^9 = 4^9 = 262144$. $262144 - 1 = 262143$. $262143 / 81 = 3236.33...$. Let me compute: $81 \cdot 3236 = 262116$. $262143 - 262116 = 27$. So $81 \nmid 262143$.

So $n = 9 \notin S$.

**$n = 10 = 2 \cdot 5$**: Need: if $10 \mid a^{10} - 1$, then $100 \mid a^{10} - 1$. $10 \mid a^{10} - 1$ means $2 \mid a^{10} - 1$ (so $a$ odd) and $5 \mid a^{10} - 1$. By Fermat, $a^5 \equiv a \pmod 5$, so $a^{10} \equiv a^2 \pmod 5$. So $5 \mid a^{10} - 1$ iff $a^2 \equiv 1 \pmod 5$ iff $a \equiv \pm 1 \pmod 5$.

So $10 \mid a^{10} - 1$ iff $a$ is odd and $a \equiv \pm 1 \pmod 5$.

Need $100 \mid a^{10} - 1$, i.e., $4 \mid a^{10} - 1$ and $25 \mid a^{10} - 1$.

For odd $a$: $a^2 \equiv 1 \pmod 8$, so $a^{10} = (a^2)^5 \equiv 1 \pmod 8$, so $4 \mid a^{10} - 1$. ✓.

For $a \equiv 1 \pmod 5$: $a = 5k + 1$. $a^5 = (5k+1)^5 = 1 + 25k + \ldots \equiv 1 \pmod{25}$. So $a^{10} = (a^5)^2 \equiv 1 \pmod{25}$. ✓.

For $a \equiv -1 \pmod 5$: $a = 5k - 1$. $a^5 = (5k-1)^5 = -1 + 25k - \ldots \equiv -1 \pmod{25}$? Let me check: $(5k-1)^5 = \sum_{j=0}^{5} \binom{5}{j}(5k)^j(-1)^{5-j} = -1 + 5 \cdot 5k - 10 \cdot 25k^2 + 10 \cdot 125k^3 - 5 \cdot 625k^4 + 3125k^5 = -1 + 25k - 250k^2 + 1250k^3 - 3125k^4 + 3125k^5$. So $a^5 \equiv -1 + 25k \pmod{25}$... wait, $-1 + 25k \equiv -1 \pmod{25}$. So $a^5 \equiv -1 \pmod{25}$. Then $a^{10} = (a^5)^2 \equiv 1 \pmod{25}$. ✓.

So $n = 10 \in S$.

Hmm, interesting. Let me think about the pattern. It seems like squarefree numbers might work, while numbers with squared prime factors might not (except for $n = 4$).

Wait, $n = 4 = 2^2$ worked. Let me re-examine.

For $n = 4$: $4 \mid a^4 - 1$ iff $a$ odd. For odd $a$, $a^4 \equiv 1 \pmod{16}$ (shown above). So $16 \mid a^4 - 1$. ✓.

For $n = 8 = 2^3$: $8 \mid a^8 - 1$ iff $a$ odd. But $64 \nmid a^8 - 1$ for $a = 3$. ✗.

For $n = 9 = 3^2$: ✗ (shown above).

So $n = 4$ works but $n = 8, 9$ don't. Let me think about why $n = 4$ is special.

For $n = p^e$, the condition is: for all $a$ coprime to $p$, if $p^e \mid a^{p^e} - 1$, then $p^{2e} \mid a^{p^e} - 1$.

The group $(\mathbb{Z}/p^{2e}\mathbb{Z})^*$ is cyclic for odd $p$, of order $p^{2e-1}(p-1)$. The condition $p^e \mid a^{p^e} - 1$ means $a^{p^e} \equiv 1 \pmod{p^e}$, i.e., the order of $a$ mod $p^e$ divides $p^e$.

Hmm, this is getting complicated. Let me just check all values up to 20.

I've checked: 2 ✓, 3 ✓, 4 ✓, 5 ✓, 6 ✓, 7 ✓, 8 ✗, 9 ✗, 10 ✓.

**$n = 11$**: Prime. ✓.

**$n = 12 = 4 \cdot 3 = 2^2 \cdot 3$**: Need: if $12 \mid a^{12} - 1$, then $144 \mid a^{12} - 1$.

$12 \mid a^{12} - 1$ means $4 \mid a^{12} - 1$ and $3 \mid a^{12} - 1$.

$4 \mid a^{12} - 1$: $a$ must be odd (if $a$ even, $a^{12}$ is even, $a^{12} - 1$ odd). For odd $a$, $a^2 \equiv 1 \pmod 8$, so $a^{12} = (a^2)^6 \equiv 1 \pmod 8$, so $4 \mid a^{12} - 1$. ✓.

$3 \mid a^{12} - 1$: $a^{12} \equiv a^{12} \pmod 3$. By Fermat, $a^3 \equiv a \pmod 3$, so $a^{12} = (a^3)^4 \equiv a^4 \pmod 3$. $a^4 \equiv a^2 \pmod 3$ (since $a^3 \equiv a$). So $a^{12} \equiv a^2 \pmod 3$. So $3 \mid a^{12} - 1$ iff $a^2 \equiv 1 \pmod 3$ iff $\gcd(a, 3) = 1$.

So $12 \mid a^{12} - 1$ iff $a$ is odd and $\gcd(a, 3) = 1$, i.e., $\gcd(a, 6) = 1$.

Need $144 \mid a^{12} - 1$, i.e., $16 \mid a^{12} - 1$ and $9 \mid a^{12} - 1$.

For odd $a$: $a^2 \equiv 1 \pmod 8$, so $a^{12} = (a^2)^6 \equiv 1 \pmod 8$. But we need $16 \mid a^{12} - 1$. $a^2 = 8m + 1$. $a^{12} = (8m+1)^6 = 1 + 6 \cdot 8m + 15 \cdot 64m^2 + \ldots = 1 + 48m + 960m^2 + \ldots$. So $a^{12} - 1 = 48m + 960m^2 + \ldots = 16(3m + 60m^2 + \ldots)$. So $16 \mid a^{12} - 1$ iff $3m + 60m^2 + \ldots$ is an integer, which it always is. Wait, $48m = 16 \cdot 3m$, so $16 \mid 48m$. And $960m^2 = 16 \cdot 60m^2$, so $16 \mid 960m^2$. So $16 \mid a^{12} - 1$ for all odd $a$. ✓.

Hmm wait, let me double-check with $a = 3$: $3^{12} = 531441$. $531441 - 1 = 531440$. $531440 / 16 = 33215$. ✓. $531440 / 144 = 3690.56...$. Let me check $9$: $531440 / 9 = 59048.89...$. So $9 \nmid 531440$?

Wait, but $a = 3$ and $\gcd(3, 3) = 3 \neq 1$, so $12 \nmid 3^{12} - 1$. Let me recheck: $3 \mid 3^{12} - 1$? $3^{12} \equiv 0 \pmod 3$, so $3^{12} - 1 \equiv -1 \pmod 3$. So $3 \nmid 3^{12} - 1$. Right, so $a = 3$ doesn't satisfy the hypothesis.

Let me try $a = 5$: $\gcd(5, 6) = 1$. $5^{12} = 244140625$. $244140625 - 1 = 244140624$. $244140624 / 12 = 20345052$. ✓. $244140624 / 144 = 1695421$. Let me check: $144 \cdot 1695421 = 244140624$. ✓. So $144 \mid 5^{12} - 1$.

Let me try $a = 7$: $\gcd(7, 6) = 1$. $7^{12} = 13841287201$. $-1 = 13841287200$. $/ 12 = 1153440600$. $/ 144 = 96120050$. Let me verify: $144 \cdot 96120050 = 13841287200$. ✓.

Let me try to find a counterexample. We need $a$ odd, $\gcd(a, 3) = 1$, but $144 \nmid a^{12} - 1$.

$144 = 16 \cdot 9$. We showed $16 \mid a^{12} - 1$ for all odd $a$. So we need $9 \mid a^{12} - 1$ for all $a$ with $\gcd(a, 3) = 1$.

$a^{12} = (a^3)^4$. If $a \equiv 1 \pmod 3$, $a^3 \equiv 1 \pmod 9$, so $a^{12} \equiv 1 \pmod 9$. ✓.

If $a \equiv 2 \pmod 3$, $a^3 \equiv -1 \pmod 9$, so $a^{12} = (a^3)^4 \equiv 1 \pmod 9$. ✓.

So $9 \mid a^{12} - 1$ for all $a$ with $\gcd(a, 3) = 1$. ✓.

So $n = 12 \in S$.

**$n = 13$**: Prime. ✓.

**$n = 14 = 2 \cdot 7$**: Similar to $n = 6$ and $n = 10$. $14 \mid a^{14} - 1$ iff $a$ odd and $7 \mid a^{14} - 1$. By Fermat, $a^7 \equiv a \pmod 7$, so $a^{14} \equiv a^2 \pmod 7$. So $7 \mid a^{14} - 1$ iff $a^2 \equiv 1 \pmod 7$ iff $a \equiv \pm 1 \pmod 7$.

Need $196 \mid a^{14} - 1$, i.e., $4 \mid a^{14} - 1$ and $49 \mid a^{14} - 1$.

$4 \mid a^{14} - 1$ for odd $a$: $a^2 \equiv 1 \pmod 8$, $a^{14} = (a^2)^7 \equiv 1 \pmod 8$. ✓.

$49 \mid a^{14} - 1$ for $a \equiv \pm 1 \pmod 7$:

$a \equiv 1 \pmod 7$: $a = 7k + 1$. $a^7 = (7k+1)^7 = 1 + 7 \cdot 7k + \ldots = 1 + 49k + \ldots \equiv 1 \pmod{49}$. So $a^{14} \equiv 1 \pmod{49}$. ✓.

$a \equiv -1 \pmod 7$: $a = 7k - 1$. $a^7 = (7k-1)^7 = -1 + 7 \cdot 7k - \ldots \equiv -1 \pmod{49}$. So $a^{14} \equiv 1 \pmod{49}$. ✓.

So $n = 14 \in S$.

**$n = 15 = 3 \cdot 5$**: $15 \mid a^{15} - 1$ iff $3 \mid a^{15} - 1$ and $5 \mid a^{15} - 1$.

$3 \mid a^{15} - 1$: $a^{15} \equiv a^{15} \pmod 3$. $a^3 \equiv a \pmod 3$, so $a^{15} = (a^3)^5 \equiv a^5 \equiv a^3 \cdot a^2 \equiv a \cdot a^2 = a^3 \equiv a \pmod 3$. So $3 \mid a^{15} - 1$ iff $a \equiv 1 \pmod 3$.

$5 \mid a^{15} - 1$: $a^5 \equiv a \pmod 5$, so $a^{15} = (a^5)^3 \equiv a^3 \pmod 5$. So $5 \mid a^{15} - 1$ iff $a^3 \equiv 1 \pmod 5$. The cubes mod 5: $0^3=0, 1^3=1, 2^3=3, 3^3=2, 4^3=4$. So $a^3 \equiv 1 \pmod 5$ iff $a \equiv 1 \pmod 5$.

So $15 \mid a^{15} - 1$ iff $a \equiv 1 \pmod 3$ and $a \equiv 1 \pmod 5$, i.e., $a \equiv 1 \pmod{15}$.

Need $225 \mid a^{15} - 1$, i.e., $9 \mid a^{15} - 1$ and $25 \mid a^{15} - 1$.

$a \equiv 1 \pmod{15}$, so $a = 15k + 1$.

$9 \mid a^{15} - 1$: $a \equiv 1 \pmod 3$, so $a = 3m + 1$ where $m = 5k$. $a^3 \equiv 1 \pmod 9$ (shown before). $a^{15} = (a^3)^5 \equiv 1 \pmod 9$. ✓.

$25 \mid a^{15} - 1$: $a \equiv 1 \pmod 5$, so $a = 5j + 1$ where $j = 3k$. $a^5 \equiv 1 \pmod{25}$ (shown before). $a^{15} = (a^5)^3 \equiv 1 \pmod{25}$. ✓.

So $n = 15 \in S$.

**$n = 16 = 2^4$**: Need: if $16 \mid a^{16} - 1$, then $256 \mid a^{16} - 1$. $16 \mid a^{16} - 1$ requires $a$ odd. For odd $a$, $a^2 \equiv 1 \pmod 8$, so $a^{16} = (a^2)^8 \equiv 1 \pmod 8$, but we need $16 \mid a^{16} - 1$.

Actually, for odd $a$, is $16 \mid a^{16} - 1$ always? $a = 3$: $3^{16} = 43046721$. $43046721 - 1 = 43046720$. $43046720 / 16 = 2690420$. ✓. $43046720 / 256 = 168152.03...$. $256 \cdot 168152 = 43046912 > 43046720$. So $256 \nmid 43046720$.

So $n = 16 \notin S$.

**$n = 17$**: Prime. ✓.

**$n = 18 = 2 \cdot 3^2$**: Need: if $18 \mid a^{18} - 1$, then $324 \mid a^{18} - 1$.

$18 \mid a^{18} - 1$ means $2 \mid a^{18} - 1$ (so $a$ odd) and $9 \mid a^{18} - 1$.

$9 \mid a^{18} - 1$: $a^{18} = (a^3)^6$. If $\gcd(a, 3) = 1$, then $a^3 \equiv \pm 1 \pmod 9$, so $a^{18} = (a^3)^6 \equiv 1 \pmod 9$. If $3 \mid a$, then $a^3 \equiv 0 \pmod 9$ (if $3 \mid a$ then $9 \mid a^3$), so $a^{18} \equiv 0 \pmod 9$, and $9 \nmid a^{18} - 1$.

So $9 \mid a^{18} - 1$ iff $\gcd(a, 3) = 1$.

So $18 \mid a^{18} - 1$ iff $a$ is odd and $\gcd(a, 3) = 1$, i.e., $\gcd(a, 6) = 1$.

Need $324 \mid a^{18} - 1$, i.e., $4 \mid a^{18} - 1$ and $81 \mid a^{18} - 1$.

$4 \mid a^{18} - 1$ for odd $a$: $a^2 \equiv 1 \pmod 8$, $a^{18} = (a^2)^9 \equiv 1 \pmod 8$. So $4 \mid a^{18} - 1$. ✓.

$81 \mid a^{18} - 1$ for $\gcd(a, 3) = 1$: $a^{18} = (a^9)^2$. We need $81 \mid a^{18} - 1$.

Let me think. $a$ is coprime to 3. The group $(\mathbb{Z}/81\mathbb{Z})^*$ is cyclic of order $\phi(81) = 54$. We need $a^{18} \equiv 1 \pmod{81}$ for all $a$ coprime to 3 with $a$ odd and $\gcd(a, 3) = 1$.

But wait, the condition is only for $a$ with $\gcd(a, 6) = 1$. Let me check if there's a counterexample.

$a = 5$: $\gcd(5, 6) = 1$. $5^{18} \pmod{81}$?

$5^2 = 25$. $5^3 = 125 \equiv 125 - 81 = 44 \pmod{81}$. $5^6 = 44^2 = 1936 \equiv 1936 - 23 \cdot 81 = 1936 - 1863 = 73 \pmod{81}$. $5^9 = 5^6 \cdot 5^3 = 73 \cdot 44 = 3212 \equiv 3212 - 39 \cdot 81 = 3212 - 3159 = 53 \pmod{81}$. $5^{18} = 53^2 = 2809 \equiv 2809 - 34 \cdot 81 = 2809 - 2754 = 55 \pmod{81}$.

So $5^{18} \equiv 55 \pmod{81}$, and $55 \neq 1$. So $81 \nmid 5^{18} - 1$.

So $n = 18 \notin S$.

**$n = 19$**: Prime. ✓.

**$n = 20 = 4 \cdot 5 = 2^2 \cdot 5$**: Need: if $20 \mid a^{20} - 1$, then $400 \mid a^{20} - 1$.

$20 \mid a^{20} - 1$ means $4 \mid a^{20} - 1$ and $5 \mid a^{20} - 1$.

$4 \mid a^{20} - 1$: $a$ must be odd. For odd $a$, $a^2 \equiv 1 \pmod 8$, so $a^{20} = (a^2)^{10} \equiv 1 \pmod 8$, so $4 \mid a^{20} - 1$. ✓.

$5 \mid a^{20} - 1$: $a^5 \equiv a \pmod 5$, $a^{20} = (a^5)^4 \equiv a^4 \pmod 5$. $a^4 \equiv 1 \pmod 5$ for $\gcd(a, 5) = 1$ (Fermat). So $5 \mid a^{20} - 1$ iff $\gcd(a, 5) = 1$.

So $20 \mid a^{20} - 1$ iff $a$ is odd and $\gcd(a, 5) = 1$, i.e., $\gcd(a, 10) = 1$.

Need $400 \mid a^{20} - 1$, i.e., $16 \mid a^{20} - 1$ and $25 \mid a^{20} - 1$.

$16 \mid a^{20} - 1$ for odd $a$: $a^2 \equiv 1 \pmod 8$, $a^{20} = (a^2)^{10} \equiv 1 \pmod 8$. But we need $16 \mid a^{20} - 1$.

$a = 3$: $3^{20} = 3486784401$. $3486784401 - 1 = 3486784400$. $3486784400 / 16 = 217924025$. ✓. So $16 \mid 3^{20} - 1$.

Actually, let me think more carefully. For odd $a$, $a^2 = 8m + 1$. $a^{20} = (8m+1)^{10} = 1 + 10 \cdot 8m + \binom{10}{2} \cdot 64m^2 + \ldots = 1 + 80m + 2880m^2 + \ldots$. So $a^{20} - 1 = 80m + 2880m^2 + \ldots = 16(5m + 180m^2 + \ldots)$. So $16 \mid a^{20} - 1$ for all odd $a$. ✓.

$25 \mid a^{20} - 1$ for $\gcd(a, 5) = 1$: $a^5 \equiv a \pmod 5$, but we need mod 25. $a^{20} = (a^5)^4$. 

For $a \equiv 1 \pmod 5$: $a = 5k + 1$, $a^5 \equiv 1 \pmod{25}$ (shown before). So $a^{20} \equiv 1 \pmod{25}$. ✓.

For $a \equiv 2 \pmod 5$: $a = 5k + 2$. $a^5 = (5k+2)^5 = 32 + 5 \cdot 16 \cdot 5k + \ldots = 32 + 400k + \ldots$. $32 \equiv 7 \pmod{25}$. $400k \equiv 0 \pmod{25}$. So $a^5 \equiv 7 \pmod{25}$. Then $a^{20} = (a^5)^4 \equiv 7^4 = 2401 \pmod{25}$. $2401 = 96 \cdot 25 + 1$. So $a^{20} \equiv 1 \pmod{25}$. ✓.

For $a \equiv 3 \pmod 5$: $a^5 \equiv 3^5 = 243 \equiv 243 - 9 \cdot 25 = 243 - 225 = 18 \pmod{25}$. $a^{20} = 18^4 = 104976 \pmod{25}$. $104976 / 25 = 4199.04$. $25 \cdot 4199 = 104975$. $104976 - 104975 = 1$. So $a^{20} \equiv 1 \pmod{25}$. ✓.

For $a \equiv 4 \pmod 5$: $a^5 \equiv 4^5 = 1024 \equiv 1024 - 40 \cdot 25 = 1024 - 1000 = 24 \equiv -1 \pmod{25}$. $a^{20} = (-1)^4 = 1 \pmod{25}$. ✓.

So $25 \mid a^{20} - 1$ for all $a$ with $\gcd(a, 5) = 1$. ✓.

So $n = 20 \in S$.

Now let me also double-check $n = 4$ more carefully, and reconsider the pattern.

So far: $S \cap \{2, \ldots, 20\} = \{2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17, 19, 20\}$.

Not in $S$: $\{8, 9, 16, 18\}$.

Let me verify the sum: $2 + 3 + 4 + 5 + 6 + 7 + 10 + 11 + 12 + 13 + 14 + 15 + 17 + 19 + 20$.

$= (2+3+4+5+6+7) + (10+11+12+13+14+15) + (17+19+20)$

$= 27 + 75 + 56 = 158$.

Wait, let me also check $n = 4$ again. I want to make sure.

$n = 4$: for all $a$, if $4 \mid a^4 - 1$ then $16 \mid a^4 - 1$. $4 \mid a^4 - 1$ iff $a$ odd (since for even $a$, $a^4 - 1$ is odd). For odd $a$, $a = 2k+1$, $a^2 = 4k^2 + 4k + 1 = 4k(k+1) + 1$. Since $k(k+1)$ is even, $a^2 = 8j + 1$ for some $j$. $a^4 = (8j+1)^2 = 64j^2 + 16j + 1 = 16(4j^2 + j) + 1$. So $16 \mid a^4 - 1$. ✓.

Now let me think about what the pattern is. The numbers NOT in $S$ up to 20 are: 8, 9, 16, 18.

- $8 = 2^3$
- $9 = 3^2$
- $16 = 2^4$
- $18 = 2 \cdot 3^2$

And the numbers IN $S$ with prime power factors:
- $4 = 2^2$ ✓
- $12 = 2^2 \cdot 3$ ✓
- $20 = 2^2 \cdot 5$ ✓

So $2^2$ is OK but $3^2$ is not (in $n = 9$ and $n = 18$). And $2^3, 2^4$ are not OK.

Let me think about this more carefully. The key insight is about the structure of the multiplicative group modulo $p^{2e}$.

For $n = p^e$ (prime power), the condition is: for all $a$ coprime to $p$, if $p^e \mid a^{p^e} - 1$ then $p^{2e} \mid a^{p^e} - 1$.

The group $(\mathbb{Z}/p^{2e}\mathbb{Z})^*$ for odd $p$ is cyclic of order $p^{2e-1}(p-1)$. The subgroup of elements $\equiv 1 \pmod{p^e}$ has order $p^e$ (it's the kernel of reduction mod $p^e$).

The condition $p^e \mid a^{p^e} - 1$ means $a^{p^e} \equiv 1 \pmod{p^e}$, i.e., $\text{ord}_{p^e}(a) \mid p^e$.

The condition $p^{2e} \mid a^{p^e} - 1$ means $a^{p^e} \equiv 1 \pmod{p^{2e}}$, i.e., $\text{ord}_{p^{2e}}(a) \mid p^e$.

So we need: for all $a$ coprime to $p$, $\text{ord}_{p^e}(a) \mid p^e \implies \text{ord}_{p^{2e}}(a) \mid p^e$.

Now, $\text{ord}_{p^{2e}}(a) \mid p^e$ iff $a^{p^e} \equiv 1 \pmod{p^{2e}}$. And $\text{ord}_{p^e}(a) \mid p^e$ iff $a^{p^e} \equiv 1 \pmod{p^e}$.

The question is whether there exists $a$ with $a^{p^e} \equiv 1 \pmod{p^e}$ but $a^{p^e} \not\equiv 1 \pmod{p^{2e}}$.

In the cyclic group $(\mathbb{Z}/p^{2e}\mathbb{Z})^*$ of order $p^{2e-1}(p-1)$, the $p^e$-th powers form a subgroup. The elements with $a^{p^e} \equiv 1 \pmod{p^e}$ are those whose order mod $p^e$ divides $p^e$.

Hmm, let me think about this differently using the $p$-adic valuation.

For odd prime $p$, $(\mathbb{Z}/p^k\mathbb{Z})^*$ is cyclic of order $p^{k-1}(p-1)$. Let $g$ be a primitive root mod $p^2$ (hence mod $p^k$ for all $k$). Then $g$ has order $p^{k-1}(p-1)$ mod $p^k$.

An element $a = g^j$ has $a^{p^e} \equiv 1 \pmod{p^e}$ iff $p^{e-1}(p-1) \mid j \cdot p^e$, i.e., $(p-1) \mid j \cdot p$... wait, let me be more careful.

$\text{ord}_{p^e}(g^j) = \frac{p^{e-1}(p-1)}{\gcd(j, p^{e-1}(p-1))}$.

$a^{p^e} \equiv 1 \pmod{p^e}$ iff $\text{ord}_{p^e}(a) \mid p^e$ iff $\frac{p^{e-1}(p-1)}{\gcd(j, p^{e-1}(p-1))} \mid p^e$.

Since $p^{e-1}(p-1) / \gcd(j, p^{e-1}(p-1))$ must divide $p^e$, and $p^{e-1}(p-1) / \gcd(j, p^{e-1}(p-1))$ divides $p^{e-1}(p-1)$, we need it to divide $p^e$. Since $\gcd(p^{e-1}(p-1), p^e) = p^{e-1}$, we need $p^{e-1}(p-1)/\gcd(j, p^{e-1}(p-1)) \mid p^{e-1}$, which means $(p-1) \mid \gcd(j, p^{e-1}(p-1))$, i.e., $(p-1) \mid j$.

So $a^{p^e} \equiv 1 \pmod{p^e}$ iff $(p-1) \mid j$ (where $a = g^j$).

Similarly, $a^{p^e} \equiv 1 \pmod{p^{2e}}$ iff $\text{ord}_{p^{2e}}(a) \mid p^e$, i.e., $\frac{p^{2e-1}(p-1)}{\gcd(j, p^{2e-1}(p-1))} \mid p^e$. This requires $(p-1) \mid \gcd(j, p^{2e-1}(p-1))$ and $p^{2e-1}/\gcd(j, p^{2e-1}(p-1))$... hmm, let me think again.

$\frac{p^{2e-1}(p-1)}{\gcd(j, p^{2e-1}(p-1))} \mid p^e$.

Let $d = \gcd(j, p^{2e-1}(p-1))$. We need $p^{2e-1}(p-1)/d \mid p^e$. Since $\gcd(p^{2e-1}(p-1), p^e) = p^{e}$ (for $e \geq 1$, and $p \nmid (p-1)$), we need $p^{2e-1}(p-1)/d \mid p^e$. 

Write $d = p^a \cdot b$ where $p \nmid b$ and $b \mid (p-1)$, $a \leq 2e-1$. Then $p^{2e-1}(p-1)/d = p^{2e-1-a}(p-1)/b$. For this to divide $p^e$, we need $(p-1)/b = 1$ (i.e., $(p-1) \mid b$, but $b \mid (p-1)$, so $b = p-1$) and $2e-1-a \leq e$, i.e., $a \geq e-1$.

So $a^{p^e} \equiv 1 \pmod{p^{2e}}$ iff $(p-1) \mid j$ and $p^{e-1} \mid j$ (i.e., $v_p(j) \geq e-1$), i.e., $p^{e-1}(p-1) \mid j$.

And $a^{p^e} \equiv 1 \pmod{p^e}$ iff $(p-1) \mid j$.

So the condition for $n = p^e$ (odd $p$) to be in $S$ is: for all $j$ with $(p-1) \mid j$, we have $p^{e-1}(p-1) \mid j$. But this is clearly false for $e \geq 2$ (take $j = p-1$, which satisfies $(p-1) \mid j$ but not $p^{e-1}(p-1) \mid j$ when $e \geq 2$).

Wait, but we also need $a = g^j$ to range over all elements coprime to $p$, and $j$ ranges over $0, 1, \ldots, p^{2e-1}(p-1) - 1$. The condition $(p-1) \mid j$ but $p^{e-1}(p-1) \nmid j$ is satisfiable when $e \geq 2$: take $j = p-1$. Then $a = g^{p-1}$, and $a^{p^e} \equiv 1 \pmod{p^e}$ but $a^{p^e} \not\equiv 1 \pmod{p^{2e}}$.

So for odd prime $p$ and $e \geq 2$, $n = p^e \notin S$.

For $e = 1$, $n = p$: the condition becomes $(p-1) \mid j \implies (p-1) \mid j$, which is trivially true. So $n = p \in S$ for all primes $p$. ✓ (matches our findings).

Now for $p = 2$: The group $(\mathbb{Z}/2^k\mathbb{Z})^*$ is not cyclic for $k \geq 3$. It's $\cong \mathbb{Z}/2 \times \mathbb{Z}/2^{k-2}$.

For $k = 1$: $(\mathbb{Z}/2\mathbb{Z})^* = \{1\}$, trivial.
For $k = 2$: $(\mathbb{Z}/4\mathbb{Z})^* \cong \mathbb{Z}/2$, generated by 3 (or $-1$).
For $k \geq 3$: $(\mathbb{Z}/2^k\mathbb{Z})^* \cong \mathbb{Z}/2 \times \mathbb{Z}/2^{k-2}$, generated by $-1$ and $5$ (or some element of order $2^{k-2}$).

For $n = 2^e$:
- $e = 1$: $n = 2$. Checked: ✓.
- $e = 2$: $n = 4$. Checked: ✓.
- $e = 3$: $n = 8$. Checked: ✗.
- $e = 4$: $n = 16$. Checked: ✗.

Let me understand why $e = 2$ works but $e \geq 3$ doesn't.

For $n = 2^e$, the condition is: for all odd $a$, if $2^e \mid a^{2^e} - 1$ then $2^{2e} \mid a^{2^e} - 1$.

For $e \geq 3$, $(\mathbb{Z}/2^{2e}\mathbb{Z})^* \cong \mathbb{Z}/2 \times \mathbb{Z}/2^{2e-2}$. The order of $a$ mod $2^{2e}$ divides $2^{2e-2} \cdot 2 = 2^{2e-1}$... actually the exponent of the group is $2^{2e-2}$ (lcm of 2 and $2^{2e-2}$).

Hmm, let me think about this using the 2-adic valuation of $a^{2^e} - 1$.

For odd $a$, $v_2(a^2 - 1) = v_2(a-1) + v_2(a+1) \geq 3$ (since one of $a-1, a+1$ is $\equiv 2 \pmod 4$ and the other $\equiv 0 \pmod 4$, so $v_2 \geq 1 + 2 = 3$). Actually, more precisely, for odd $a$, $v_2(a^2 - 1) \geq 3$.

By LTE (Lifting the Exponent), for odd $a$ and $n$ even, $v_2(a^n - 1) = v_2(a^2 - 1) + v_2(n) - 1$.

Wait, LTE for $p = 2$: if $2 \mid a - 1$ (i.e., $a$ odd) and $2 \mid n$, then $v_2(a^n - 1) = v_2(a - 1) + v_2(a + 1) + v_2(n) - 1$.

Hmm, actually the LTE lemma for $p = 2$ is a bit different. Let me recall:

For $p = 2$, $2 \mid a - b$, $2 \mid a + b$, and $n$ even: $v_2(a^n - b^n) = v_2(a - b) + v_2(a + b) + v_2(n) - 1$.

With $b = 1$, $a$ odd: $v_2(a^n - 1) = v_2(a - 1) + v_2(a + 1) + v_2(n) - 1$ for $n$ even.

For $n = 2^e$ ($e \geq 1$), $v_2(n) = e$. So $v_2(a^{2^e} - 1) = v_2(a-1) + v_2(a+1) + e - 1$.

The condition $2^e \mid a^{2^e} - 1$ means $v_2(a^{2^e} - 1) \geq e$, i.e., $v_2(a-1) + v_2(a+1) + e - 1 \geq e$, i.e., $v_2(a-1) + v_2(a+1) \geq 1$. This is always true for odd $a$ (since $a - 1$ and $a + 1$ are both even, so each has $v_2 \geq 1$). So $2^e \mid a^{2^e} - 1$ for all odd $a$.

The condition $2^{2e} \mid a^{2^e} - 1$ means $v_2(a-1) + v_2(a+1) + e - 1 \geq 2e$, i.e., $v_2(a-1) + v_2(a+1) \geq e + 1$.

For $e = 1$: need $v_2(a-1) + v_2(a+1) \geq 2$. For odd $a$, one of $a-1, a+1$ is $\equiv 0 \pmod 4$ and the other $\equiv 2 \pmod 4$, so $v_2(a-1) + v_2(a+1) \geq 2 + 1 = 3 \geq 2$. ✓.

For $e = 2$: need $v_2(a-1) + v_2(a+1) \geq 3$. Same argument: $\geq 3$. ✓.

For $e = 3$: need $v_2(a-1) + v_2(a+1) \geq 4$. But for $a = 3$: $v_2(2) + v_2(4) = 1 + 2 = 3 < 4$. ✗.

For $e \geq 3$: take $a = 3$, $v_2(2) + v_2(4) = 3 < e + 1$ when $e \geq 3$. ✗.

So $n = 2^e \in S$ iff $e \leq 2$, i.e., $n \in \{2, 4\}$.

Now for general $n$, let me think about the structure. Let $n = 2^{e_0} \prod p_i^{e_i}$ (odd primes $p_i$).

The condition $n \mid a^n - 1$ is equivalent to: for each prime power $q = p^e \| n$, $p^e \mid a^n - 1$.

And $n^2 \mid a^n - 1$ is equivalent to: for each $q = p^e \| n$, $p^{2e} \mid a^n - 1$.

The condition must hold for all $a$. By CRT, we can choose $a$ independently mod each prime power dividing $n^2$ (as long as $\gcd(a, n) = 1$, which is necessary as shown).

So the condition decomposes: for each prime $p \mid n$ with $p^e \| n$, we need: for all $a$ coprime to $p$, if $p^e \mid a^n - 1$ then $p^{2e} \mid a^n - 1$.

Wait, but the condition is "for all $a$, if $n \mid a^n - 1$ then $n^2 \mid a^n - 1$". The hypothesis $n \mid a^n - 1$ involves ALL prime powers simultaneously. So we can't simply decompose.

However, by CRT, we can choose $a$ such that $a$ satisfies the hypothesis for all primes simultaneously. Specifically, for each prime $p_i \mid n$, the condition $p_i^{e_i} \mid a^n - 1$ constrains $a$ mod $p_i^{e_i}$ (or mod some power of $p_i$). By CRT, we can find $a$ satisfying all these constraints simultaneously (as long as they're compatible, which they are since they're mod different primes).

But the key question is: can we find $a$ such that $n \mid a^n - 1$ but for some specific prime $p \mid n$, $p^{2e} \nmid a^n - 1$?

If for some prime $p \mid n$ with $p^e \| n$, there exists $a$ (coprime to $n$) such that $p^e \mid a^n - 1$ but $p^{2e} \nmid a^n - 1$, AND we can simultaneously satisfy $q^{e_q} \mid a^n - 1$ for all other primes $q \mid n$, then $n \notin S$.

By CRT, if we can find $a_p$ mod $p^{2e}$ such that $p^e \mid a_p^n - 1$ but $p^{2e} \nmid a_p^n - 1$, and for each other prime $q \mid n$, we can find $a_q$ mod $q^{2e_q}$ such that $q^{e_q} \mid a_q^n - 1$, then we can combine them via CRT to get $a$ mod $n^2$ with $n \mid a^n - 1$ but $n^2 \nmid a^n - 1$.

For the other primes $q$, we just need some $a_q$ with $q^{e_q} \mid a_q^n - 1$. We can always take $a_q \equiv 1 \pmod{q^{e_q}}$ (then $a_q^n \equiv 1 \pmod{q^{e_q}}$). Actually, we need $a_q$ coprime to $q$, and $a_q \equiv 1 \pmod{q^{e_q}}$ works.

So the question reduces to: for each prime $p \mid n$ with $p^e \| n$, does there exist $a$ coprime to $p$ with $p^e \mid a^n - 1$ but $p^{2e} \nmid a^n - 1$?

If such $a$ exists for any prime $p \mid n$, then $n \notin S$.

So $n \in S$ iff for every prime $p \mid n$ with $p^e \| n$, for all $a$ coprime to $p$, $p^e \mid a^n - 1 \implies p^{2e} \mid a^n - 1$.

Now, this is a condition for each prime separately, with the exponent being $n$ (not $p^e$).

Let me analyze this. For odd prime $p$ with $p^e \| n$:

The group $(\mathbb{Z}/p^{2e}\mathbb{Z})^*$ is cyclic of order $p^{2e-1}(p-1)$. Let $g$ be a generator. $a = g^j$.

$a^n \equiv 1 \pmod{p^e}$ iff $\text{ord}_{p^e}(a) \mid n$. $\text{ord}_{p^e}(g^j) = \frac{p^{e-1}(p-1)}{\gcd(j, p^{e-1}(p-1))}$. So the condition is $\frac{p^{e-1}(p-1)}{\gcd(j, p^{e-1}(p-1))} \mid n$.

$a^n \equiv 1 \pmod{p^{2e}}$ iff $\text{ord}_{p^{2e}}(a) \mid n$. $\text{ord}_{p^{2e}}(g^j) = \frac{p^{2e-1}(p-1)}{\gcd(j, p^{2e-1}(p-1))}$. So the condition is $\frac{p^{2e-1}(p-1)}{\gcd(j, p^{2e-1}(p-1))} \mid n$.

We need: for all $j$, if $\frac{p^{e-1}(p-1)}{\gcd(j, p^{e-1}(p-1))} \mid n$ then $\frac{p^{2e-1}(p-1)}{\gcd(j, p^{2e-1}(p-1))} \mid n$.

Let $d_e = \gcd(j, p^{e-1}(p-1))$ and $d_{2e} = \gcd(j, p^{2e-1}(p-1))$. Note that $d_{2e} = \gcd(j, p^{2e-1}(p-1))$ and $d_e = \gcd(j, p^{e-1}(p-1))$. Since $p^{e-1}(p-1) \mid p^{2e-1}(p-1)$, we have $d_e \mid d_{2e}$. Also, $d_{2e}/d_e$ divides $p^{2e-1}/p^{e-1} = p^e$ (and is a power of $p$, since the $(p-1)$ part is the same). Actually, $d_{2e} = d_e \cdot p^{\min(v_p(j), 2e-1) - \min(v_p(j), e-1)}$ if $v_p(j) \geq e$, otherwise $d_{2e} = d_e$.

Hmm, this is getting complicated. Let me think about it differently.

The condition $\frac{p^{e-1}(p-1)}{d_e} \mid n$ means $p^{e-1}(p-1)/d_e$ divides $n$. Since $p^e \| n$, $v_p(n) = e$. Also, $p^{e-1}(p-1)/d_e$ divides $p^{e-1}(p-1)$, and $v_p(p^{e-1}(p-1)/d_e) = e - 1 - v_p(d_e)$. For this to divide $n$ (with $v_p(n) = e$), we need $e - 1 - v_p(d_e) \leq e$, i.e., $v_p(d_e) \geq -1$, always true. But we also need the $(p-1)$ part to divide $n$.

Let me write $n = p^e \cdot m$ where $\gcd(p, m) = 1$. Then $v_p(n) = e$.

$\frac{p^{e-1}(p-1)}{d_e} \mid n = p^e m$.

The $p$-part: $p^{e-1-v_p(d_e)} \mid p^e$, always true since $v_p(d_e) \leq e-1$.

The $(p-1)$-part (coprime to $p$): $\frac{p-1}{d_e/p^{v_p(d_e)}} \mid m$. Let $d_e = p^s \cdot t$ where $\gcd(t, p) = 1$ and $t \mid (p-1)$. Then the condition is $\frac{p-1}{t} \mid m$.

Similarly, $\frac{p^{2e-1}(p-1)}{d_{2e}} \mid n = p^e m$. The $p$-part: $p^{2e-1-v_p(d_{2e})} \mid p^e$, so $v_p(d_{2e}) \geq e - 1$. The $(p-1)$-part: $\frac{p-1}{t'} \mid m$ where $d_{2e} = p^{s'} \cdot t'$, $t' \mid (p-1)$, $\gcd(t', p) = 1$.

Since $d_e \mid d_{2e}$ and they share the same $(p-1)$ part (because $v_p(j)$ determines the $p$-part, and the $(p-1)$ part is $\gcd(j, p-1)$ which is the same for both), we have $t = t'$. So the $(p-1)$ conditions are the same.

The difference is in the $p$-part: for the hypothesis, we need $p^{e-1-s} \mid p^e$ (always true). For the conclusion, we need $p^{2e-1-s'} \mid p^e$, i.e., $s' \geq e - 1$.

Now, $s = \min(v_p(j), e-1)$ and $s' = \min(v_p(j), 2e-1)$.

If $v_p(j) \geq e - 1$: $s = e - 1$, $s' = \min(v_p(j), 2e-1) \geq e - 1$. So $s' \geq e - 1$. ✓.

If $v_p(j) < e - 1$: $s = v_p(j)$, $s' = v_p(j) < e - 1$. So $s' < e - 1$, and $p^{2e-1-s'} = p^{2e-1-v_p(j)}$ which has $p$-adic valuation $2e - 1 - v_p(j) > e$, so it doesn't divide $p^e$. ✗.

But wait, we also need the hypothesis to hold. The hypothesis requires $\frac{p-1}{t} \mid m$ and $p^{e-1-s} \mid p^e$ (always true). So the hypothesis holds whenever $\frac{p-1}{t} \mid m$.

If $v_p(j) < e - 1$ and $\frac{p-1}{t} \mid m$, then the hypothesis holds but the conclusion fails. So we need: there is no $j$ with $v_p(j) < e-1$ and $\frac{p-1}{\gcd(j, p-1)} \mid m$.

But $j$ can be anything. Take $j = p - 1$ (so $v_p(j) = 0 < e - 1$ for $e \geq 2$, and $\gcd(j, p-1) = p - 1$, so $\frac{p-1}{p-1} = 1 \mid m$). Then the hypothesis holds but the conclusion fails (for $e \geq 2$).

So for $e \geq 2$ (odd prime $p$ with $p^e \| n$), $n \notin S$.

For $e = 1$: $v_p(j) < e - 1 = 0$ is impossible (since $v_p(j) \geq 0$). So the condition is always satisfied. So for $e = 1$, the prime $p$ doesn't cause problems.

Wait, but I need to be more careful. For $e = 1$, $s = \min(v_p(j), 0) = 0$ and $s' = \min(v_p(j), 1)$. The hypothesis requires $p^{0} \mid p$ (true) and $\frac{p-1}{t} \mid m$. The conclusion requires $p^{1 - s'} \mid p$ (i.e., $s' \geq 0$, always true) and $\frac{p-1}{t} \mid m$ (same as hypothesis). So for $e = 1$, hypothesis $\iff$ conclusion. ✓.

So for odd primes, $p^e \| n$ causes $n \notin S$ iff $e \geq 2$.

Now for $p = 2$ with $2^{e_0} \| n$:

If $e_0 = 0$: no constraint from 2.
If $e_0 = 1$: $n$ is odd times 2. $(\mathbb{Z}/4\mathbb{Z})^* \cong \mathbb{Z}/2$. Need: for all odd $a$, if $2 \mid a^n - 1$ then $4 \mid a^n - 1$. $2 \mid a^n - 1$ for odd $a$ and $n \geq 1$: $a^n$ is odd, so $a^n - 1$ is even. ✓. Need $4 \mid a^n - 1$. For odd $a$, $a^n \equiv 1 \pmod 4$ if $n$ is even (since $a^2 \equiv 1 \pmod 4$). But $n = 2 \cdot m$ where $m$ is odd, so $n$ is even. So $a^n = (a^2)^{n/2} \equiv 1 \pmod 4$. ✓.

Wait, but what if $n$ is even? $n = 2m$ with $m$ odd. $a^n = a^{2m} = (a^2)^m \equiv 1^m = 1 \pmod 4$. ✓.

If $e_0 = 2$: $4 \| n$. Need: for all odd $a$, if $4 \mid a^n - 1$ then $16 \mid a^n - 1$.

$4 \mid a^n - 1$: $a$ odd, $n$ even (since $4 \mid n$). $a^n \equiv 1 \pmod 4$ (since $n$ even). So $4 \mid a^n - 1$ for all odd $a$. ✓ (hypothesis always holds).

Need $16 \mid a^n - 1$ for all odd $a$. $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + v_2(n) - 1$ (LTE, $n$ even). $v_2(n) \geq 2$ (since $4 \mid n$). So $v_2(a^n - 1) \geq 1 + 2 + 2 - 1 = 4$. So $16 \mid a^n - 1$. ✓.

If $e_0 = 3$: $8 \| n$. Need: for all odd $a$, if $8 \mid a^n - 1$ then $64 \mid a^n - 1$.

$8 \mid a^n - 1$: $v_2(a^n - 1) \geq 3$. $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + v_2(n) - 1$. $v_2(n) \geq 3$. So $v_2(a^n - 1) \geq 1 + 1 + 3 - 1 = 4 \geq 3$. So hypothesis always holds.

Need $64 \mid a^n - 1$: $v_2(a^n - 1) \geq 6$. $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + v_2(n) - 1$. Take $a = 3$: $v_2(2) + v_2(4) + v_2(n) - 1 = 1 + 2 + v_2(n) - 1 = 2 + v_2(n)$. Need $\geq 6$, so $v_2(n) \geq 4$. But $v_2(n) = 3$ (since $8 \| n$). So $2 + 3 = 5 < 6$. ✗.

So $e_0 = 3$ fails. Similarly, $e_0 \geq 3$ fails (take $a = 3$, $v_2(a^n - 1) = 2 + e_0$, need $\geq 2e_0$, so $e_0 \leq 2$).

So for $p = 2$: $2^{e_0} \| n$ causes $n \notin S$ iff $e_0 \geq 3$.

Combining: $n \in S$ iff:
- For every odd prime $p$, $v_p(n) \leq 1$ (i.e., $n$ is squarefree at odd primes).
- $v_2(n) \leq 2$ (i.e., $4 \nmid n$ or $8 \nmid n$... wait, $v_2(n) \leq 2$ means $8 \nmid n$).

Wait, but I need to double-check the case $e_0 = 2$ more carefully. We showed $v_2(a^n - 1) \geq 4$ when $v_2(n) \geq 2$. But we need $v_2(a^n - 1) \geq 2 \cdot 2 = 4$. So $4 \geq 4$. ✓. But this is tight. Let me verify with a specific example.

$n = 4$: $v_2(n) = 2$. $a = 3$: $v_2(3^4 - 1) = v_2(80) = 4$. $2 \cdot 2 = 4$. ✓ (just barely).

$n = 12 = 4 \cdot 3$: $v_2(n) = 2$. $a = 3$: but $\gcd(3, 12) = 3 \neq 1$, so $12 \nmid 3^{12} - 1$. Need $a$ coprime to 12. $a = 5$: $v_2(5^{12} - 1) = v_2(4) + v_2(6) + v_2(12) - 1 = 2 + 1 + 2 - 1 = 4$. Need $\geq 4$. ✓.

But wait, I should also check: is the hypothesis $8 \mid a^n - 1$ (i.e., $v_2 \geq 3$) always satisfied when $v_2(n) = 2$? $v_2(a^n - 1) \geq 1 + 1 + 2 - 1 = 3$. ✓. And we need $v_2 \geq 4$, which requires $v_2(a-1) + v_2(a+1) \geq 2$. For odd $a$, one of $a \pm 1$ is $\equiv 0 \pmod 4$, so $v_2(a-1) + v_2(a+1) \geq 2 + 1 = 3 \geq 2$. ✓.

Actually, I realize I need to be more careful. The condition is $v_2(a^n - 1) \geq 2 e_0$ where $e_0 = v_2(n)$. We have $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + v_2(n) - 1 = v_2(a-1) + v_2(a+1) + e_0 - 1$.

Need: $v_2(a-1) + v_2(a+1) + e_0 - 1 \geq 2 e_0$, i.e., $v_2(a-1) + v_2(a+1) \geq e_0 + 1$.

For odd $a$, $v_2(a-1) + v_2(a+1) \geq 3$ (as argued). So need $e_0 + 1 \leq 3$, i.e., $e_0 \leq 2$.

But wait, the hypothesis is $2^{e_0} \mid a^n - 1$, which requires $v_2(a^n - 1) \geq e_0$, i.e., $v_2(a-1) + v_2(a+1) \geq 1$. This is always true for odd $a$. So the hypothesis is always satisfied, and we need the conclusion $v_2(a^n - 1) \geq 2e_0$ for all odd $a$.

The minimum of $v_2(a-1) + v_2(a+1)$ over odd $a$ is 3 (achieved at $a = 3$: $v_2(2) + v_2(4) = 3$, or $a = 5$: $v_2(4) + v_2(6) = 3$). So we need $3 + e_0 - 1 \geq 2e_0$, i.e., $e_0 \leq 2$.

So $v_2(n) \leq 2$ is necessary and sufficient for the 2-part.

Now, combining everything: $n \in S$ iff:
1. $v_2(n) \leq 2$
2. For all odd primes $p$, $v_p(n) \leq 1$ (i.e., $n$ is squarefree at odd primes)

Equivalently, $n$ is squarefree except possibly for a factor of $4$ (i.e., $v_2(n) \in \{0, 1, 2\}$ and all odd prime exponents are 0 or 1).

Let me verify this against our computations:
- $n = 2 = 2$: $v_2 = 1 \leq 2$, squarefree. ✓
- $n = 3$: prime. ✓
- $n = 4 = 2^2$: $v_2 = 2 \leq 2$, no odd primes. ✓
- $n = 5$: prime. ✓
- $n = 6 = 2 \cdot 3$: $v_2 = 1$, squarefree. ✓
- $n = 7$: prime. ✓
- $n = 8 = 2^3$: $v_2 = 3 > 2$. ✗
- $n = 9 = 3^2$: $v_3 = 2 > 1$. ✗
- $n = 10 = 2 \cdot 5$: ✓
- $n = 11$: prime. ✓
- $n = 12 = 2^2 \cdot 3$: $v_2 = 2$, $v_3 = 1$. ✓
- $n = 13$: prime. ✓
- $n = 14 = 2 \cdot 7$: ✓
- $n = 15 = 3 \cdot 5$: ✓
- $n = 16 = 2^4$: $v_2 = 4 > 2$. ✗
- $n = 17$: prime. ✓
- $n = 18 = 2 \cdot 3^2$: $v_3 = 2 > 1$. ✗
- $n = 19$: prime. ✓
- $n = 20 = 2^2 \cdot 5$: $v_2 = 2$, $v_5 = 1$. ✓

This matches perfectly!

So $S \cap \{2, \ldots, 20\} = \{2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17, 19, 20\}$.

Sum $= 2 + 3 + 4 + 5 + 6 + 7 + 10 + 11 + 12 + 13 + 14 + 15 + 17 + 19 + 20$.

Let me compute: $2+3 = 5$, $+4 = 9$, $+5 = 14$, $+6 = 20$, $+7 = 27$, $+10 = 37$, $+11 = 48$, $+12 = 60$, $+13 = 73$, $+14 = 87$, $+15 = 102$, $+17 = 119$, $+19 = 138$, $+20 = 158$.

Sum = 158.

Now let me write up the proof properly. I need to make sure my argument is rigorous, especially the CRT decomposition part.

Let me re-examine the key steps:

1. $n \mid a^n - 1 \implies \gcd(a, n) = 1$ (since if $p \mid \gcd(a, n)$, then $p \mid a$ and $p \mid n$, so $a^n \equiv 0 \pmod p$, $a^n - 1 \equiv -1 \pmod p$, contradiction).

2. The condition is: for all $a$ with $\gcd(a, n) = 1$, $a^n \equiv 1 \pmod n \implies a^n \equiv 1 \pmod{n^2}$.

3. By CRT, this decomposes into prime power conditions. Specifically, $n \in S$ iff for every prime $p$ with $p^e \| n$, the following holds: for all $a$ coprime to $p$, $p^e \mid a^n - 1 \implies p^{2e} \mid a^n - 1$.

Wait, I need to be more careful about the decomposition. The condition "for all $a$ coprime to $n$, $a^n \equiv 1 \pmod n \implies a^n \equiv 1 \pmod{n^2}$" — does this decompose?

The forward direction: if $n \in S$, then for each prime $p \mid n$, the local condition holds. This is because if the local condition fails for some $p$, we can construct a global counterexample via CRT.

The backward direction: if each local condition holds, then $n \in S$. This is because if $a^n \equiv 1 \pmod n$, then for each $p \mid n$, $p^e \mid a^n - 1$, and the local condition gives $p^{2e} \mid a^n - 1$, so $n^2 \mid a^n - 1$.

The backward direction is clear. For the forward direction: suppose the local condition fails for prime $p$, i.e., there exists $a_0$ coprime to $p$ with $p^e \mid a_0^n - 1$ but $p^{2e} \nmid a_0^n - 1$. We need to find $a$ coprime to $n$ with $n \mid a^n - 1$ but $n^2 \nmid a^n - 1$.

For each prime $q \mid n$, $q \neq p$, we need $q^{e_q} \mid a^n - 1$. We can choose $a \equiv 1 \pmod{q^{e_q}}$ for all such $q$ (then $a^n \equiv 1 \pmod{q^{e_q}}$). And we choose $a \equiv a_0 \pmod{p^{2e}}$ (or mod some appropriate power). By CRT (since $p$ and $q$ are distinct primes), we can find such $a$.

But wait, we need $a$ to be coprime to $n$. Since $a \equiv a_0 \pmod{p^{2e}}$ and $\gcd(a_0, p) = 1$, we have $\gcd(a, p) = 1$. And $a \equiv 1 \pmod{q^{e_q}}$ for other primes, so $\gcd(a, q) = 1$. So $\gcd(a, n) = 1$. ✓.

And $a^n \equiv a_0^n \pmod{p^{2e}}$ (since $a \equiv a_0 \pmod{p^{2e}}$), so $p^e \mid a^n - 1$ but $p^{2e} \nmid a^n - 1$. And $a^n \equiv 1 \pmod{q^{e_q}}$ for all other $q$. So $n \mid a^n - 1$ but $n^2 \nmid a^n - 1$. ✓.

Great, so the decomposition is valid.

Now, for the local condition at odd prime $p$ with $p^e \| n$:

Using the cyclic group structure, I showed that for $e \geq 2$, taking $a = g^{p-1}$ (where $g$ is a primitive root mod $p^{2e}$) gives a counterexample. Let me verify this more carefully.

$g$ has order $p^{2e-1}(p-1)$ mod $p^{2e}$. $a = g^{p-1}$ has order $p^{2e-1}$ mod $p^{2e}$ and order $p^{e-1}$ mod $p^e$.

$a^n \pmod{p^e}$: order of $a$ mod $p^e$ is $p^{e-1}$. $a^n \equiv 1 \pmod{p^e}$ iff $p^{e-1} \mid n$. Since $p^e \| n$, $p^e \mid n$, so $p^{e-1} \mid n$. ✓. So hypothesis holds.

$a^n \pmod{p^{2e}}$: order of $a$ mod $p^{2e}$ is $p^{2e-1}$. $a^n \equiv 1 \pmod{p^{2e}}$ iff $p^{2e-1} \mid n$. Since $p^e \| n$ (and $e \geq 2$), $v_p(n) = e < 2e - 1$. So $p^{2e-1} \nmid n$. ✗. So conclusion fails.

So for $e \geq 2$, the local condition fails. ✓.

For $e = 1$: $a = g^{p-1}$ has order $1$ mod $p$ (i.e., $a \equiv 1 \pmod p$) and order $p$ mod $p^2$. $a^n \equiv 1 \pmod p$ always (since $a \equiv 1 \pmod p$). $a^n \equiv 1 \pmod{p^2}$ iff $p \mid n$. Since $p \| n$, $p \mid n$. ✓. So this particular $a$ works.

But we need to check ALL $a$ coprime to $p$. Let $a = g^j$ where $g$ is a primitive root mod $p^2$ (order $p(p-1)$). $a^n \equiv 1 \pmod p$ iff $(p-1) \mid jn$... wait, the order of $g$ mod $p$ is $p - 1$. So $a^n \equiv 1 \pmod p$ iff $(p-1) \mid jn$.

$a^n \equiv 1 \pmod{p^2}$: order of $g$ mod $p^2$ is $p(p-1)$. So $a^n \equiv 1 \pmod{p^2}$ iff $p(p-1) \mid jn$.

Since $p \| n$, $v_p(n) = 1$. So $p(p-1) \mid jn$ iff $(p-1) \mid jn$ and $p \mid jn / \gcd(jn, p(p-1))$... hmm, let me think differently.

$p(p-1) \mid jn$: since $\gcd(p, p-1) = 1$, this is equivalent to $p \mid jn$ and $(p-1) \mid jn$. Since $p \mid n$ (as $p \| n$), $p \mid jn$ is automatic. And $(p-1) \mid jn$ is the hypothesis. So $p(p-1) \mid jn$ iff $(p-1) \mid jn$. So hypothesis $\iff$ conclusion. ✓.

So for $e = 1$ (odd prime), the local condition always holds. ✓.

For $p = 2$ with $2^{e_0} \| n$:

Using LTE: for odd $a$ and even $n$, $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + v_2(n) - 1$.

The hypothesis is $v_2(a^n - 1) \geq e_0$, which is $v_2(a-1) + v_2(a+1) \geq e_0 - v_2(n) + 1 = 1$ (since $v_2(n) = e_0$). This is always true for odd $a$.

The conclusion is $v_2(a^n - 1) \geq 2e_0$, which is $v_2(a-1) + v_2(a+1) \geq e_0 + 1$.

The minimum of $v_2(a-1) + v_2(a+1)$ for odd $a$ is 3 (at $a = \pm 3 \pmod 8$... actually, for $a = 3$: $v_2(2) + v_2(4) = 1 + 2 = 3$; for $a = 5$: $v_2(4) + v_2(6) = 2 + 1 = 3$; for $a = 7$: $v_2(6) + v_2(8) = 1 + 3 = 4$; for $a = 1$: $v_2(0) + v_2(2) = \infty + 1 = \infty$). So the minimum is 3.

So the conclusion holds for all odd $a$ iff $3 \geq e_0 + 1$, i.e., $e_0 \leq 2$.

Wait, but I need to be careful about $e_0 = 0$ (i.e., $n$ odd). If $e_0 = 0$, there's no 2-part, so no constraint from $p = 2$.

And for $e_0 = 1$: $n$ is even, $v_2(n) = 1$. LTE applies (since $n$ is even). $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + 1 - 1 = v_2(a-1) + v_2(a+1) \geq 3$. Need $\geq 2 \cdot 1 = 2$. ✓.

For $e_0 = 2$: $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + 2 - 1 = v_2(a-1) + v_2(a+1) + 1 \geq 4$. Need $\geq 4$. ✓.

For $e_0 = 3$: $v_2(a^n - 1) = v_2(a-1) + v_2(a+1) + 2 \geq 5$. Need $\geq 6$. $5 < 6$. ✗ (at $a = 3$).

So $v_2(n) \leq 2$ is the condition.

But wait, I also need to handle the case $e_0 = 0$ but $n$ even... no, $e_0 = 0$ means $n$ is odd. And if $n$ is odd, the hypothesis $2 \mid a^n - 1$ requires $a$ odd, and then $a^n \equiv a \pmod 2$... actually if $n$ is odd and $a$ is odd, $a^n$ is odd, $a^n - 1$ is even, so $2 \mid a^n - 1$. But $e_0 = 0$ means $2 \nmid n$, so there's no 2-part in the condition. The condition only involves primes dividing $n$.

OK so the complete characterization is:

$n \in S$ iff $v_2(n) \leq 2$ and $v_p(n) \leq 1$ for all odd primes $p$.

Equivalently, $n$ is squarefree at all odd primes, and $v_2(n) \in \{0, 1, 2\}$.

Now let me list all $n \in S$ with $1 < n \leq 20$:

- $n = 2 = 2$: ✓
- $n = 3 = 3$: ✓
- $n = 4 = 2^2$: ✓
- $n = 5 = 5$: ✓
- $n = 6 = 2 \cdot 3$: ✓
- $n = 7 = 7$: ✓
- $n = 8 = 2^3$: ✗ ($v_2 = 3$)
- $n = 9 = 3^2$: ✗ ($v_3 = 2$)
- $n = 10 = 2 \cdot 5$: ✓
- $n = 11 = 11$: ✓
- $n = 12 = 2^2 \cdot 3$: ✓
- $n = 13 = 13$: ✓
- $n = 14 = 2 \cdot 7$: ✓
- $n = 15 = 3 \cdot 5$: ✓
- $n = 16 = 2^4$: ✗ ($v_2 = 4$)
- $n = 17 = 17$: ✓
- $n = 18 = 2 \cdot 3^2$: ✗ ($v_3 = 2$)
- $n = 19 = 19$: ✓
- $n = 20 = 2^2 \cdot 5$: ✓

$S \cap \{2, \ldots, 20\} = \{2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17, 19, 20\}$.

Sum $= 2 + 3 + 4 + 5 + 6 + 7 + 10 + 11 + 12 + 13 + 14 + 15 + 17 + 19 + 20 = 158$.

Let me now write up the proof.

Actually, wait. I want to double-check the LTE application. LTE for $p = 2$ says: if $2 \mid a - b$ and $2 \mid a + b$ (i.e., $a, b$ both odd) and $n$ is even, then $v_2(a^n - b^n) = v_2(a - b) + v_2(a + b) + v_2(n) - 1$.

With $b = 1$, $a$ odd, $n$ even: $v_2(a^n - 1) = v_2(a - 1) + v_2(a + 1) + v_2(n) - 1$. ✓.

But what if $n$ is odd? Then LTE doesn't apply in this form. If $n$ is odd and $a$ is odd, $v_2(a^n - 1) = v_2(a - 1)$ (by the simpler form of LTE for $p = 2$ when $n$ is odd: $v_2(a^n - b^n) = v_2(a - b)$).

But in our case, if $e_0 \geq 1$, then $n$ is even, so LTE applies. If $e_0 = 0$, $n$ is odd, and there's no 2-part to worry about. So we're fine.

Also, I should handle the case $e_0 = 0$ more carefully. If $n$ is odd, the condition from $p = 2$ is vacuous (2 doesn't divide $n$). So we only need to check odd primes.

Let me also verify the case $n = 1$ is excluded (the problem says $n > 1$). ✓.

Now, one more
