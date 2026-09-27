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

Let n be a positive integer. There are n(n+1)/2 tokens, each with a black
side and a white side, arranged into an equilateral triangle, with the
biggest row containing n tokens. Initially, each token has the white side
up. An operation is to choose a line parallel to the sides of the triangle,
and flip all the tokens on that line. A configuration is called admissible
if it can be obtained from the initial configuration by performing a finite
number of operations. For each admissible configuration C, let f(C) denote
the smallest number of operations required to obtain C from the initial
configuration. Find the maximum value of f(C), where C varies over all
admissible configurations.
