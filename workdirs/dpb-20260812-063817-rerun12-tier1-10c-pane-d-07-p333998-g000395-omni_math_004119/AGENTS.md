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

Let $r>1$ be a rational number. Alice plays a solitaire game on a number line. Initially there is a red bead at $0$ and a blue bead at $1$. In a move, Alice chooses one of the beads and an integer $k \in \mathbb{Z}$. If the chosen bead is at $x$, and the other bead is at $y$, then the bead at $x$ is moved to the point $x'$ satisfying $x'-y=r^k(x-y)$.

Find all $r$ for which Alice can move the red bead to $1$ in at most $2021$ moves.
