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

Let n ≥ 2 be an integer. Let x₁ ≥ x₂ ≥ ⋯ ≥ xₙ and y₁ ≥ y₂ ≥ ⋯ ≥ yₙ be 2n real
numbers such that
0 = x₁ + x₂ + ⋯ + xₙ = y₁ + y₂ + ⋯ + yₙ,
and
1 = x₁² + x₂² + ⋯ + xₙ² = y₁² + y₂² + ⋯ + yₙ².
Prove that
∑_{i=1}^{n} (xᵢyᵢ − xᵢyₙ₊₁₋ᵢ) ≥ 2/√(n−1).
