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

Find all positive real solutions to:
(x_1^2 - x_3x_5)(x_2^2 - x_3x_5) ≤ 0
(x_2^2 - x_4x_1)(x_3^2 - x_4x_1) ≤ 0
(x_3^2 - x_5x_2)(x_4^2 - x_5x_2) ≤ 0
(x_4^2 - x_1x_3)(x_5^2 - x_1x_3) ≤ 0
(x_5^2 - x_2x_4)(x_1^2 - x_2x_4) ≤ 0
