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

Let $a, b, c, p, q, r$ be positive integers with $p, q, r \ge 2$. Denote
\[Q=\{(x, y, z)\in \mathbb{Z}^3 : 0 \le x \le a, 0 \le y \le b , 0 \le z \le c \}. \]
Initially, some pieces are put on the each point in $Q$, with a total of $M$ pieces. Then, one can perform the following three types of operations repeatedly:
(1) Remove $p$ pieces on $(x, y, z)$ and place a piece on $(x-1, y, z)$ ;
(2) Remove $q$ pieces on $(x, y, z)$ and place a piece on $(x, y-1, z)$ ;
(3) Remove $r$ pieces on $(x, y, z)$ and place a piece on $(x, y, z-1)$.

Find the smallest positive integer $M$ such that one can always perform a sequence of operations, making a piece placed on $(0,0,0)$, no matter how the pieces are distributed initially.
