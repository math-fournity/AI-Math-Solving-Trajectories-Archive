# Solver Task

You are a mathematical problem solver. Solve the problem completely.
Do not search for this exact problem, its official answer, or its solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search. Do NOT read any files.
- All information you need is already in your prompt above. Do NOT read any files.
- Output your complete proof directly in your response (in this TUI).
- Do NOT write any files — do not use write/edit tools.
- End your proof with a line containing exactly: ### PROOF COMPLETE
- Your full reasoning and output are automatically captured by the system.

## Answer Leak Self-Check (MANDATORY before solving)

Before you start solving, check the problem text below for any leaked answers, solutions, solution sketches, or formalization notes that would give away the answer or proof strategy.

If you find ANY of the following in the problem text, do NOT solve the problem. Instead output exactly:
### ANSWER LEAK DETECTED: <brief description of what leaked>

Then stop. Do not attempt to solve a problem whose answer has been leaked.

Watch for:
- Phrases like "The proof follows...", "solution sketch", "Formalization notes"
- Official solutions or answer values embedded in the problem statement
- Lean theorem statements that reveal the answer (e.g. `determine SolutionSet := {{n | ...}}`)

## Problem

A table of size $n \times n$ is filled with the numbers $1, 2, \ldots, n^2$ in such a way that each number appears exactly once. We say that $n$ is a "mean-integer" number if there exists such a filling where the arithmetic mean of the numbers in every row and every column is an integer.

Let $S$ be the set of all positive integers $n \le 100$ that are "mean-integer" numbers. Calculate the sum of all elements in $S$.

=== Established vein (extracted from a previous solver's work on this problem; understand and verify it first, then continue from the stuck point) ===

The following results have already been established for this problem.

**Completed reasoning:**

1. (Reduction) The mean of a row/column is an integer iff its sum is divisible by $n$. Since a row/column sum is determined mod $n$ by the residues of its entries mod $n$, the problem reduces to: fill an $n \times n$ grid with the residues $0, 1, \ldots, n-1$, each appearing exactly $n$ times, such that every row sum and every column sum is $\equiv 0 \pmod{n}$. (Given such a residue grid, the actual numbers are assigned by placing $r+1, r+1+n, \ldots, r+1+(n-1)n$ in the $n$ cells holding residue $r$, in any order.)

2. ($n = 1$) trivially mean-integer.

3. ($n = 2$) impossible: each row would need two equal residues ($\{0,0\}$ or $\{1,1\}$), forcing every column to mix a $0$ and a $1$.

4. (Odd $n$) the circulant construction $a_{ij} = (i+j) \bmod n$ works: every row and every column is a complete residue system with sum $n(n-1)/2 \equiv 0 \pmod{n}$ when $n$ is odd.

5. ($n = 4$) an explicit residue grid exists, e.g. with rows $0\ 1\ 1\ 2\ / \ 0\ 3\ 3\ 2\ / \ 2\ 1\ 1\ 0\ / \ 2\ 3\ 3\ 0$: all row and column sums are $\equiv 0 \pmod 4$ and each residue is used exactly 4 times.

6. ($n \equiv 0 \pmod 4$) the pairing construction works: in every row place the pairs $(r, n-r)$ for $r = 1, \ldots, n/2 - 1$, plus two extra cells holding $(0,0)$ in $n/2$ of the rows and $(n/2, n/2)$ in the other $n/2$ rows. Every row sum is $\equiv 0 \pmod n$; each of the two special columns sums to $(n/2)^2$, which is $\equiv 0 \pmod n$ exactly when $n/2$ is even, i.e. $4 \mid n$.

7. (Closure) if $\gcd(a, b) = 1$ and both $a$ and $b$ are mean-integer, then $ab$ is mean-integer (explicit product arrangement: place $a^2(B_{pq} - 1) + A_{ij}$ at the composite position).

**Stuck point:** The only unresolved case is $n \equiv 2 \pmod 4$ (i.e. $n = 6, 10, 14, \ldots$). For these $n$: the pairing construction fails (the special columns sum to $(n/2)^2 \not\equiv 0 \pmod n$ when $n/2$ is odd); the product construction cannot help (it would need the factor $2$, which is not mean-integer); for $n = 6$, direct constructions were attempted — row-type matching failed on parity grounds, and the necessary conditions mod 2 and mod 3 were each individually satisfiable but could not be combined; a doubling construction ($m \times m$ arrangement to $2m \times 2m$) was explored but not completed. It is not yet known whether $n \equiv 2 \pmod 4$ is impossible or constructible; no argument has been found in either direction.

**Continue from here (direction guidance):**

When the problem is stuck in its current representation, try switching to a local representation (such as $\mathbb{Z}/p\mathbb{Z}$ or $p$-adic numbers); look for hidden algebraic structure in the local representation, and lift the local finding back to a global conclusion.
