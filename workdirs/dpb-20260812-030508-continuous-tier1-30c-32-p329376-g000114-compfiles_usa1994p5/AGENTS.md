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

Let |U|, σ(U) and π(U) denote the number of elements, the sum, and the
product, respectively, of a finite set U of positive integers. (If U is the
empty set, |U| = 0, σ(U) = 0, π(U) = 1.) Let S be a finite set of positive
integers. As usual, we define (n k) = n! / (k! (n-k)!) for 0 ≤ k ≤ n and
(n k) = 0 otherwise. Prove that
∑_{U ⊆ S} (-1)^{|U|} (m - σ(U) choose |S|) = π(S)
for all integers m ≥ σ(S).
