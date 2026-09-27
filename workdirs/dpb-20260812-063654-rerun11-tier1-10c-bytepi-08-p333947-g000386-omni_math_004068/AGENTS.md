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

Let $ n \geq 2$ be a positive integer and $ \lambda$ a positive real number. Initially there are $ n$ fleas on a horizontal line, not all at the same point. We define a move as choosing two fleas at some points $ A$ and $ B$, with $ A$ to the left of $ B$, and letting the flea from $ A$ jump over the flea from $ B$ to the point $ C$ so that $ \frac {BC}{AB} \equal{} \lambda$. 

Determine all values of $ \lambda$ such that, for any point $ M$ on the line and for any initial position of the $ n$ fleas, there exists a sequence of moves that will take them all to the position right of $ M$.
