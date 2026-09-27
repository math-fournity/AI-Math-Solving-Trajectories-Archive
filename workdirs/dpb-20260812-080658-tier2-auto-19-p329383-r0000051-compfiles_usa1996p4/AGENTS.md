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

An n-term sequence (x₁, x₂, …, xₙ) in which each term is either 0 or 1 is called a
binary sequence of length n. Let aₙ be the number of binary sequences of length n
containing no three consecutive terms equal to 0, 1, 0 in that order. Let bₙ be the
number of binary sequences of length n that contain no four consecutive terms equal
to 0, 0, 1, 1 or 1, 1, 0, 0 in that order. Prove that bₙ₊₁ = 2aₙ for all positive
integers n.
