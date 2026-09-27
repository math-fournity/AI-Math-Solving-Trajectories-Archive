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

I have an n×n sheet of stamps, from which I've been asked to tear out blocks
of three adjacent stamps in a single row or column. (I can only tear along the
perforations separating adjacent stamps, and each block must come out of the
sheet in one piece.) Let b(n) be the smallest number of blocks I can tear out
and make it impossible to tear out any more blocks. Prove that there are real
constants c and d such that
(1/7)n² - cn ≤ b(n) ≤ (1/5)n² - dn
for all n > 0.
