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

Let \( A \) be a Noetherian complete local ring of dimension \( d \), of mixed characteristic (i.e., $\mathrm{Char} A = 0$ and $\mathrm{Char} A / \mathfrak{m}$), and let \( p = \text{char}(A/\mathfrak{m}) \). Assume that \( \text{ht}(p \cdot A) = 1 \). Prove that \( A \) is a finitely generated module over a subring \( B \subset A \) such that
\[
B \cong C[[x_1, \dots, x_{d-1}]],
\]
where \( C \) is a discrete valuation ring (DVR).
