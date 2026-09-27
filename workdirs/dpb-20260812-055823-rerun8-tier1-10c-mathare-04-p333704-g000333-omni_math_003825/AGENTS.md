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

The leader of an IMO team chooses positive integers $n$ and $k$ with $n > k$, and announces them to the deputy leader and a contestant. The leader then secretly tells the deputy leader an $n$-digit binary string, and the deputy leader writes down all $n$-digit binary strings which differ from the leader’s in exactly $k$ positions. (For example, if $n = 3$ and $k = 1$, and if the leader chooses $101$, the deputy leader would write down $001, 111$ and $100$.) The contestant is allowed to look at the strings written by the deputy leader and guess the leader’s string. What is the minimum number of guesses (in terms of $n$ and $k$) needed to guarantee the correct answer?
