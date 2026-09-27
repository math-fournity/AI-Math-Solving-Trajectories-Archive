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

a₁, a₂, ... , aₙ is a sequence of 0s and 1s. T is the number of triples
(aᵢ, aⱼ, aₖ) with i < j < k which are not equal to (0, 1, 0) or (1, 0, 1).
For 1 ≤ i ≤ n, f(i) is the number of j < i with aⱼ = aᵢ plus the number of
j > i with aⱼ ≠ aᵢ. Show that
T = f(1)(f(1) - 1)/2 + f(2)(f(2) - 1)/2 + ... + f(n)(f(n) - 1)/2.
If n is odd, what is the smallest value of T?
