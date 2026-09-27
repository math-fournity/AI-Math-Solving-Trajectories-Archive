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

Let $x_1, x_2, \ldots, x_n$ be real numbers satisfying
$x_1^2 + x_2^2 + \cdots + x_n^2 = 1$. Prove that for every integer $k \geq 2$
there are integers $a_1, a_2, \ldots, a_n$, not all zero, such that
$|a_i| \leq k - 1$ for all $i$, and
$$|a_1 x_1 + a_2 x_2 + \cdots + a_n x_n| \leq \frac{(k - 1)\sqrt{n}}{k^n - 1}.$$
