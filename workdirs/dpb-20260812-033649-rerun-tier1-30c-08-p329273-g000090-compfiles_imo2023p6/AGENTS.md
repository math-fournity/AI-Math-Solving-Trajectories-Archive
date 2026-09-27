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

Let ABC be an equilateral triangle. Let A₁,B₁,C₁ be interior points of
ABC such that BA₁=A₁C, CB₁ = B₁A, AC₁=C₁B, and
∠BA₁C + ∠CB₁A + ∠C₁B = 480°.
Let BC₁ and CB₁ meet at A₂, let CA₁ and AC₁ meet at B₂, and let AB₁ and
BA₁ meet at $C₂.
Prove that if triangle A₁B₁C₁ is scalene, then the three circumcircles
of triangles AA₁A₂, BB₁B₂ and CC₁C₂ all pass through two common points.
