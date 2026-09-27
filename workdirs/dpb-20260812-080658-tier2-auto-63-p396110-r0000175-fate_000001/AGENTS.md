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

Let $G$ be a cyclic group with generator $a$, and let $G^{\prime}$ be a group isomorphic to $G$. If $\phi: G \rightarrow G^{\prime}$ is an isomorphism, show that, for every $x \in G, \phi(x)$ is completely determined by the value $\phi(a)$. That is, if $\phi: G \rightarrow G^{\prime}$ and $\psi: G \rightarrow G^{\prime}$ are two isomophisms such that $\phi(a)=\psi(a)$, then $\phi(x)=\psi(x)$ for all $x \in G$.
