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

Let `m` and `n` be positive integers with `m ≥ n`. There are `m` cupcakes of different
flavors arranged around a circle and `n` people who like cupcakes. Each person assigns
a nonnegative real number score to each cupcake, depending on how much they like the
cupcake. Suppose that for each person `P`, it is possible to partition the circle of
`m` cupcakes into `n` groups of consecutive cupcakes so that the sum of `P`'s scores
of the cupcakes in each group is at least 1. Prove that it is possible to distribute
the `m` cupcakes to the `n` people so that each person `P` receives cupcakes of total
score at least 1 with respect to `P`.
