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

Let P₁, P₂, ..., P_{2n} be 2n distinct points on the unit circle x² + y² = 1, other than
(1, 0). Each point is colored either red or blue, with exactly n red points and n blue
points. Let R₁, R₂, ..., Rₙ be any ordering of the red points. Let B₁ be the nearest
blue point to R₁ traveling counterclockwise around the circle starting from R₁. Then let
B₂ be the nearest of the remaining blue points to R₂ traveling counterclockwise around
the circle from R₂, and so on, until we have labeled all of the blue points B₁, ..., Bₙ.
Show that the number of counterclockwise arcs of the form Rᵢ → Bᵢ that contain the point
(1, 0) is independent of the way we chose the ordering R₁, ..., Rₙ of the red points.
