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

For a given positive integer $n$ and prime number $p$, find the minimum value of positive integer $m$ that satisfies the following property: for any polynomial $$f(x)=(x+a_1)(x+a_2)\ldots(x+a_n)$$ ($a_1,a_2,\ldots,a_n$ are positive integers), and for any non-negative integer $k$, there exists a non-negative integer $k'$ such that $$v_p(f(k))<v_p(f(k'))\leq v_p(f(k))+m.$$ Note: for non-zero integer $N$,$v_p(N)$ is the largest non-zero integer $t$ that satisfies $p^t\mid N$.
