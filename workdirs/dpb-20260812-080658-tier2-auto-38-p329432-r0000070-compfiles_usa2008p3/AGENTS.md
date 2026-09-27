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

Let n be a positive integer. Denote by Sₙ the set of points (x, y)
with integer coordinates such that
|x| + |y + 1/2| < n.
A path is a sequence of distinct points (x₁, y₁), (x₂, y₂), ..., (x_ℓ, y_ℓ)
in Sₙ such that, for i = 2, ..., ℓ, the distance between (xᵢ, yᵢ) and
(xᵢ₋₁, yᵢ₋₁) is 1. Prove that the points in Sₙ cannot be partitioned into
fewer than n paths.
