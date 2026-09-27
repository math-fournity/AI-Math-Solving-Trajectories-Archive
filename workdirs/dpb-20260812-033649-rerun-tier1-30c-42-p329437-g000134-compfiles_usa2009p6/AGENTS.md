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

Let $s_1, s_2, s_3, \ldots$ be an infinite, nonconstant sequence of rational numbers, meaning it
is not the case that $s_1 = s_2 = s_3 = \ldots$. Suppose that $t_1, t_2, t_3, \ldots$ is also an
infinite, nonconstant sequence of rational numbers with the property that $(s_i - s_j)(t_i - t_j)$
is an integer for all $i$ and $j$. Prove that there exists a rational number $r$ such that
$(s_i - s_j) r$ and $(t_i - t_j)/r$ are integers for all $i$ and $j$.
