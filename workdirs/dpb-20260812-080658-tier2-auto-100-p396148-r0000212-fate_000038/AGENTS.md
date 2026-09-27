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

Let $G$ be a group, and $a, b \in G$. For any positive integer $n$ we define $a^{n}$ by $a^{n}=\underbrace{a a a \cdots a}_{n \text { factors }}$

If there is an element $x \in G$ such that $a=x^{2}$, we say that $a$ has a square root in $G$. Similarly, if $a=y^{3}$ for some $y \in G$, we say $a$ has a cube root in $G$. In general, $a$ has an $n$th root in $G$ if $a=z^{n}$ for some $z \in G$. Prove
$1\left(b a b^{-1}\right)^{n}=b a^{n} b^{-1}$, for every positive integer Prove by induction.
