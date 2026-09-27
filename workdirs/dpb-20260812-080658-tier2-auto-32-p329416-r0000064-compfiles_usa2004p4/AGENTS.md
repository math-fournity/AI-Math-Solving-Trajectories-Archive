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

Alice and Bob play a game on a 6 by 6 grid. On his turn, a player chooses
a rational number not yet appearing in the grid and writes it in an empty square
of the grid. Alice goes first and then the players alternate. When all squares
have numbers written in them, in each row, the square with the greatest number in
that row is colored black. Alice wins if he can then draw a line from the top of
the grid to the bottom of the grid that stays in black squares, and Bob wins if
he can't. (If two squares share a vertex, Alice can draw a line from one to the
other that stays in those two squares.) Find, with proof, a winning strategy for
one of the players.
