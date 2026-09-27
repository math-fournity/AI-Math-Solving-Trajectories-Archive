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

Suppose that $R$ is a commutative ring with identity. For a subset $S$ of $R$, let $\operatorname{Span}(S)$ be the minimal ideal containing elements in $S$. Prove that

$\operatorname{Span}(S)=\left\{\sum_{s\in S'}r_ss|S'\text{ is a finite subset of }S,r_s\in R\ \forall s\in S'\right\}.$

In other words, prove that the latter one is an ideal and any ideal containing $S$ also contains the right-hand-side.
