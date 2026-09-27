# Solver Task

You are a mathematical problem solver. Solve the problem completely.
Do not search for this exact problem, its official answer, or its solution.
You may use computation for exploration or verification.

Output your complete proof directly in your response (in this TUI).
Do NOT write any files — do not use write/edit tools.
End your proof with a line containing exactly: ### PROOF COMPLETE
Your full reasoning and output are automatically captured by the system.

## Answer Leak Self-Check (MANDATORY before solving)

Before you start solving, check the problem text below for any leaked answers, solutions, solution sketches, or formalization notes that would give away the answer or proof strategy.

If you find ANY of the following in the problem text, do NOT solve the problem. Instead output exactly:
### ANSWER LEAK DETECTED: <brief description of what leaked>

Then stop. Do not attempt to solve a problem whose answer has been leaked.

Watch for:
- Phrases like "The proof follows...", "solution sketch", "Formalization notes"
- Official solutions or answer values embedded in the problem statement
- Lean theorem statements that reveal the answer (e.g. `determine SolutionSet := {n | ...}`)

## Problem

For positive integer $k>1$, let $f(k)$ be the number of ways of factoring $k$ into product of positive integers greater than $1$ (The order of factors are not countered, for example $f(12)=4$, as $12$ can be factored in these $4$ ways: $12,2\cdot 6,3\cdot 4, 2\cdot 2\cdot 3$.
Prove: If $n$ is a positive integer greater than $1$, $p$ is a prime factor of $n$, then $f(n)\leq \frac{n}{p}$
