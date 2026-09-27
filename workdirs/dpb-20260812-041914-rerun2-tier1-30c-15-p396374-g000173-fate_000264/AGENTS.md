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

Let $p,q,r$ be three distinct prime numbers, $t$ a positive integer. Let $G$ be a finite group, $H$ a normal subgroup of $G$ such that the cardinality of $G/H$ is $r^{t}$. Suppose that there exists a composition series
    \[
\{e\} = H_0 \triangleleft H_1 \triangleleft \cdots \triangleleft H_n = H,
\]
of $H$ that satisfies $n=2$, $H_1/H_0 = \mathbb{Z}/p\mathbb{Z}$, $H_2/H_1 = \mathbb{Z}/q\mathbb{Z}$. Further suppose that there exists a composition series
\[
\{e\} = G_0 \triangleleft G_1 \triangleleft \cdots \triangleleft G_n = G,
\]
and positive integers $i<j\leq n$ such that $G_{i}/G_{i-1} = \mathbb{Z}/q\mathbb{Z}$, $G_{j}/G_{j-1} = \mathbb{Z}/p\mathbb{Z}$. Show that there exists a composition series
    \[
\{e\} = H_0 \triangleleft H_1 \triangleleft \cdots \triangleleft H_n = H,
\]
of $H$ that satisfies $n=2$, $H_1/H_0 = \mathbb{Z}/q\mathbb{Z}$, $H_2/H_1 = \mathbb{Z}/p\mathbb{Z}$.
