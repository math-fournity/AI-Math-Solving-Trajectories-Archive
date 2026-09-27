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

Two squirrels, Bushy and Jumpy, have collected 2001 walnuts for winter.
Jumpy numbers the walnuts from 1 to 2021, and digs 2021 little holes
in a circular pattern around their favorite tree. The next morning,
Jumpy notices that Bushy had placed one walnut into each hole, but
had paid no attention to the numbering. Unhappy, Jumpy decides to
reorder the walnuts by performing a sequence of 2021 moves. In the kth
move, Jump swaps the positions of the two walnuts adjacent to walnut k.
Prove that there exists a value of k such that, on the kth move, Jumpy
swaps some walnuts a and b such that a < k < b.
