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

In each square of a garden shaped like a $2022 \times 2022$ board, there is initially a tree of height $0$. A gardener and a lumberjack alternate turns playing the following game, with the gardener taking the first turn:
[list]
[*] The gardener chooses a square in the garden. Each tree on that square and all the surrounding squares (of which there are at most eight) then becomes one unit taller.
[*] The lumberjack then chooses four different squares on the board. Each tree of positive height on those squares then becomes one unit shorter.
[/list]
We say that a tree is [i]majestic[/i] if its height is at least $10^6$. Determine the largest $K$ such that the gardener can ensure there are eventually $K$ majestic trees on the board, no matter how the lumberjack plays.
