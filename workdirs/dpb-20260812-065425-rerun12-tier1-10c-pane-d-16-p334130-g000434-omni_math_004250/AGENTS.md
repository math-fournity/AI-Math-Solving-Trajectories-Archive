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

The Bank of Oslo issues two types of coin: aluminum (denoted A) and bronze (denoted B). Marianne has $n$ aluminum coins and $n$ bronze coins arranged in a row in some arbitrary initial order. A chain is any subsequence of consecutive coins of the same type. Given a fixed positive integer $k \leq 2n$, Gilberty repeatedly performs the following operation: he identifies the longest chain containing  the $k^{th}$ coin from the left and moves all coins in that chain to the left end of the row. For example, if $n=4$ and $k=4$, the process starting from the ordering $AABBBABA$ would be $AABBBABA \to BBBAAABA \to AAABBBBA \to BBBBAAAA \to ...$

Find all pairs $(n,k)$ with $1 \leq k \leq 2n$ such that for every initial ordering, at some moment during the process, the leftmost $n$ coins will all be of the same type.
