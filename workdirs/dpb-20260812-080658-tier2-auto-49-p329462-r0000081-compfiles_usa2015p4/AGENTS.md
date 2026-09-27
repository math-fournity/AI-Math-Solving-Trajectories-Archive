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

Steve is piling m ≥ 1 indistinguishable stones on the squares of an n × n grid.
Each square can have an arbitrarily high pile of stones. After he finished piling
his stones in some manner, he can then perform stone moves, defined as follows.
Consider any four grid squares, which are corners of a rectangle, i.e. in positions
(i, k), (i, l), (j, k), (j, l) for some 1 ≤ i, j, k, l ≤ n, such that i < j and
k < l. A stone move consists of either removing one stone from each of (i, k) and
(j, l) and moving them to (i, l) and (j, k) respectively, or removing one stone
from each of (i, l) and (j, k) and moving them to (i, k) and (j, l) respectively.
Two ways of piling the stones are equivalent if they can be obtained from one
another by a sequence of stone moves. How many different non-equivalent ways can
Steve pile the stones on the grid?
