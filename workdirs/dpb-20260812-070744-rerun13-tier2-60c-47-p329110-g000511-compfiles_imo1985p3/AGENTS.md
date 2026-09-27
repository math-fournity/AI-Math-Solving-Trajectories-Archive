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

For any polynomial $P(x) = a_0 + a_1x + \dots + a_kx^k$ with integer coefficients, the
number of odd coefficients is denoted by $o(P)$. For $i = 0, 1, 2, \dots$ let
$Q_i(x) = (1 + x)^i$. Prove that if $i_1, i_2, \dots, i_n$ are integers satisfying
$0 \le i_1 < i_2 < \dots < i_n$, then
$$o(Q_{i_1} + Q_{i_2} + \dots + Q_{i_n}) \ge o(Q_{i_1}).$$
