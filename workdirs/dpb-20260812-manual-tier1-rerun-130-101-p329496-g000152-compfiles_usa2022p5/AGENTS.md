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

A function f : ℝ → ℝ is essentially increasing if f(s) ≤ f(t) holds
whenever s ≤ t are real numbers such that f(s) ≠ 0 and f(t) ≠ 0.
Find the smallest integer k such that for any 2022 real numbers
x₁, x₂, ..., x₂₀₂₂, there exist k essentially increasing functions
f₁, f₂, ..., fₖ such that
f₁(n) + f₂(n) + ⋯ + fₖ(n) = xₙ
for every n = 1, 2, ..., 2022.
