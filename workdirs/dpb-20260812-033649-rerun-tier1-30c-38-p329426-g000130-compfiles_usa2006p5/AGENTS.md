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

A mathematical frog jumps along the number line. The frog starts at 1,
and jumps according to the following rule: if the frog is at integer n,
then it can jump either to n + 1 or to n + 2 ^ (mₙ + 1), where 2 ^ mₙ is
the largest power of 2 that is a factor of n. Show that if k ≥ 2 is a
positive integer and i is a nonnegative integer, then the minimum number
of jumps needed to reach 2 ^ i * k is greater than the minimum number of
jumps needed to reach 2 ^ i.
