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

There are 60 empty boxes $B_1,\ldots,B_{60}$ in a row on a table and an unlimited supply of pebbles. Given a positive integer $n$, Alice and Bob play the following game.
In the first round, Alice takes $n$ pebbles and distributes them into the 60 boxes as she wishes. Each subsequent round consists of two steps:
(a) Bob chooses an integer $k$ with $1\leq k\leq 59$ and splits the boxes into the two groups $B_1,\ldots,B_k$ and $B_{k+1},\ldots,B_{60}$.
(b) Alice picks one of these two groups, adds one pebble to each box in that group, and removes one pebble from each box in the other group.
Bob wins if, at the end of any round, some box contains no pebbles. Find the smallest $n$ such that Alice can prevent Bob from winning.

[i]Czech Republic[/i]
