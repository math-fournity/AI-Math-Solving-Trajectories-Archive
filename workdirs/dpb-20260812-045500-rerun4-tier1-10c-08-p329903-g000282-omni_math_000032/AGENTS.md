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

Let $C=\{ z \in \mathbb{C} : |z|=1 \}$ be the unit circle on the complex plane. Let $z_1, z_2, \ldots, z_{240} \in C$ (not necessarily different) be $240$ complex numbers, satisfying the following two conditions:
(1) For any open arc $\Gamma$ of length $\pi$ on $C$, there are at most $200$ of $j ~(1 \le j \le 240)$ such that $z_j \in \Gamma$.
(2) For any open arc $\gamma$ of length $\pi/3$ on $C$, there are at most $120$ of  $j ~(1 \le j \le 240)$ such that $z_j \in \gamma$.

Find the maximum of $|z_1+z_2+\ldots+z_{240}|$.
