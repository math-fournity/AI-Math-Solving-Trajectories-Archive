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

Find all functions $ f: (0, \infty) \mapsto (0, \infty)$ (so $ f$ is a function from the positive real numbers) such that
\[ \frac {\left( f(w) \right)^2 \plus{} \left( f(x) \right)^2}{f(y^2) \plus{} f(z^2) } \equal{} \frac {w^2 \plus{} x^2}{y^2 \plus{} z^2}
\]
for all positive real numbers $ w,x,y,z,$ satisfying $ wx \equal{} yz.$


[i]Author: Hojoo Lee, South Korea[/i]
