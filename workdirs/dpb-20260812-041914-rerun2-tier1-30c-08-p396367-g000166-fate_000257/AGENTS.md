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

Let $A, B \in \mathbb{Q}^\times$ be rational numbers. Consider the quaternion ring
$$
D_{A, B, \mathbb{R}} = \{a+b\boldsymbol{i} +c\boldsymbol{j}+d\boldsymbol{k}\;|\; a,b,c,d \in \mathbb{R}\}
$$
in which the multiplication satisfies relations: $\boldsymbol{i}^2 = A$, $\boldsymbol{j}^ 2 = B$, and $\boldsymbol{i}\boldsymbol{j}= -\boldsymbol{j}\boldsymbol{i} = \boldsymbol{k}$.

Show that $D_{A, B, \mathbb{R}}$ is either isomorphic to $\mathbb{H}$ (Hamilton quaternion) or isomorphic to $\mathrm{Mat}_{2\times 2}(\mathbb{R})$ as $\mathbb{R}$-algebras.
