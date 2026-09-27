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

Let n be a positive integer. A Nordic square is an n×n board containing
all the integers from 1 to n² so that each cell contains exactly one
number. Two different cells are considered adjacent if they share a
common side. Every cell that is adjacent only to cells containing larger
numbers is called a valley. An uphill path is a sequence of one or more
cells such that:
(1) the first cell in the sequence is a valley,
(2) each subsequent cell in the sequence is adjacent to the
previous cell, and
(3) the numbers written in the cells in the sequence are in
increasing order.
Find, as a function of n, the smallest possible total number of uphill
paths in a Nordic square.
