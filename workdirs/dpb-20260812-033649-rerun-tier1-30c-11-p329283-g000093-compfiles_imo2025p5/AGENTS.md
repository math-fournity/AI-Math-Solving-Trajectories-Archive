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

Alice and Bazza are playing the *inekoalaty game*, a two-player game
whose rules depend on a positive number λ known to both players. On
the nth turn of the game (starting with n = 1) the following happens:
* If n is odd, Alice chooses a nonnegative real number xₙ such that
x₁ + x₂ + ... + xₙ ≤ λn
* If n is even, Bazza chooses a nonnegative real number xₙ such that
x₁² + x₂² + .. + xₙ² ≤ n.
If a player cannot choose a suitable n, the game ends and the other
player wins. If the game goes forever, neither player wins. All
chosen numbers are known to both players.
Determine all values of λ for which Alice has a winning strategy
and all those for which Bazza has a winning strategy.
