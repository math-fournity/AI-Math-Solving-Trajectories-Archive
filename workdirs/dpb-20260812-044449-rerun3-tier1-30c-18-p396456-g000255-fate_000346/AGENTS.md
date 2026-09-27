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

If $k$ is a field of characteristic zero, $n \in \mathbb{N}$, $n \ne 0$, and $\phi \colon k[x_1, \dots, x_n] \to k[x_1, \dots, x_n]$ is given by $(x_1, \dots, x_n) \mapsto (f_1(x_1), \dots, f_n(x_n))$, where $f_i(x_i) \in k[x_i]$ having degree at least two, then there is a point $a \in k^n$ such that for any non-zero polyminal $p \in k[x_1, \dots, x_n]$, there exists $m \in \mathbb{N}$ such that $p(\phi^m(a)) \ne 0$.
