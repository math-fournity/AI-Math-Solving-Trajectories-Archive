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

Three nonnegative real numbers r₁, r₂, r₃ are written on a blackboard.
These numbers have the property that there exist integers a₁, a₂, a₃,
not all zero, satisfying a₁r₁ + a₂r₂ + a₃r₃ = 0. We are permitted to
perform the following operation: find two numbers x, y on the
blackboard with x ≤ y, then erase y and write y − x in its place.
Prove that after a finite number of such operations, we can end up
with at least one 0 on the blackboard.
