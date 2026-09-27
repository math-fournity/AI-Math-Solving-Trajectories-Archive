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

Let $n$ be a positive integer. Two players $A$ and $B$ play a game in which they take turns choosing positive integers $k \le n$. The rules of the game are:

(i) A player cannot choose a number that has been chosen by either player on any previous turn.
(ii) A player cannot choose a number consecutive to any of those the player has already chosen on any previous turn.
(iii) The game is a draw if all numbers have been chosen; otherwise the player who cannot choose a number anymore loses the game.

The player $A$ takes the first turn. Determine the outcome of the game, assuming that both players use optimal strategies.

[i]
