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

A pack of n cards, including three aces, is well shuffled. Cards are turned
over in turn. Show that the expected number of cards that must be turned over
to reach the second ace is (n+1)/2.
We model the well-shuffled pack by the set of positions occupied by the three
aces, which is uniformly distributed over the 3-element subsets of
`{1, ..., n}`. The number of cards that must be turned over to reach the
second ace is then the middle (second-smallest) of the three ace positions,
and the expected number of cards is the average of this quantity over all
3-element subsets.
