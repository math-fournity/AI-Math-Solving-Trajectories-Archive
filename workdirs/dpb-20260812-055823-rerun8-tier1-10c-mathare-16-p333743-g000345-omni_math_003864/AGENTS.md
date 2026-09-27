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

There is an integer $n > 1$. There are $n^2$ stations on a slope of a mountain, all at different altitudes. Each of two cable car companies, $A$ and $B$, operates $k$ cable cars; each cable car provides a transfer from one of the stations to a higher one (with no intermediate stops). The $k$ cable cars of $A$ have $k$ different starting points and $k$ different finishing points, and a cable car which starts higher also finishes higher. The same conditions hold for $B$. We say that two stations are linked by a company if one can start from the lower station and reach the higher one by using one or more cars of that company (no other movements between stations are allowed). Determine the smallest positive integer $k$ for which one can guarantee that there are two stations that are linked by both companies.

[i]
