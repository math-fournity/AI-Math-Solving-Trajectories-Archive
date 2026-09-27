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

Given a positive integer $n \ge 2$. Find all $n$-tuples of positive integers $(a_1,a_2,\ldots,a_n)$, such that $1<a_1 \le a_2 \le a_3 \le \cdots \le a_n$, $a_1$ is odd, and
(1) $M=\frac{1}{2^n}(a_1-1)a_2 a_3 \cdots a_n$ is a positive integer;
(2) One can pick $n$-tuples of integers $(k_{i,1},k_{i,2},\ldots,k_{i,n})$ for $i=1,2,\ldots,M$ such that for any $1 \le i_1 <i_2 \le M$, there exists $j \in \{1,2,\ldots,n\}$ such that $k_{i_1,j}-k_{i_2,j} \not\equiv 0, \pm 1 \pmod{a_j}$.
