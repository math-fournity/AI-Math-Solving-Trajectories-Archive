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

Integers n and k are given, with n ≥ k ≥ 2. You play the following game against
an evil wizard. The wizard has 2n cards; for each i = 1, ..., n, there are two
cards labeled i. Initially, the wizard places all cards face down in a row, in
unknown order. You may repeatedly make moves of the following form: you point to
any k of the cards. The wizard then turns those cards face up. If any two of the
cards match, the game is over and you win. Otherwise, you must look away, while
the wizard arbitrarily permutes the k chosen cards and then turns them back
face-down. Then, it is your turn again.
We say this game is winnable if there exist some positive integer m and some
strategy that is guaranteed to win in at most m moves, no matter how the wizard
responds. For which values of n and k is the game winnable?
