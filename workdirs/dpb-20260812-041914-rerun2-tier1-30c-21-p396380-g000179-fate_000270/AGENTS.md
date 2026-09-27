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

Let $F$ be a field and let $f(x) \in F[x]$ be an irreducible polynomial. Suppose that $K$ is a splitting field for $f(x)$ over $F$ and assume that there exists an element $\alpha \in K$ such that both $\alpha$ and $\alpha+1$ are roots of $f(x)$. Prove that there exists an intermediate field $E$ between $K$ and $F$ such that $[K:E]$ is equal to the characteristic of $F$. (In particular, the characteristic of $F$ is not zero)
