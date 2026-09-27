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

Let $n > 1$ be a given integer. An $n \times n \times n$ cube is composed of $n^3$ unit cubes. Each unit cube is painted with one colour. For each $n \times n \times 1$ box consisting of $n^2$ unit cubes (in any of the three possible orientations), we consider the set of colours present in that box (each colour is listed only once). This way, we get $3n$ sets of colours, split into three groups according to the orientation.

It happens that for every set in any group, the same set appears in both of the other groups. Determine, in terms of $n$, the maximal possible number of colours that are present.
