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

Shan-Yu and Mulan are playing a game. Let θ be an angle with 0° < θ < 180°
known to both players. Initially, Shan-Yu makes a paper triangle T with
measurements of his choice. Then, they repeatedly perform the following steps:
* If T has at least one angle measuring exactly θ, then the game stops and
Mulan wins.
* Otherwise, Mulan chooses a point P on the perimeter of T, different from its
three vertices. She then makes a straight cut from P to the opposite vertex
of T, splitting it into two triangles.
* Shan-Yu discards one of the two triangles. The remaining triangle becomes
the new T.
For which real values of θ can Mulan guarantee her victory in finitely many
steps, no matter how Shan-Yu plays?
Statement formalization adapted from AxiomMath/IMO2026; proof adapted from
Humanfia's Kimi-K3 solutions (https://github.com/humanfia/imo2026).
