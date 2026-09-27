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

Let $n=p_1^{a_1}p_2^{a_2}\cdots p_t^{a_t}$ be the prime factorisation of $n$. Define $\omega(n)=t$ and $\Omega(n)=a_1+a_2+\ldots+a_t$. Prove or disprove:
For any fixed positive integer $k$ and positive reals $\alpha,\beta$, there exists a positive integer $n>1$ such that
i) $\frac{\omega(n+k)}{\omega(n)}>\alpha$
ii) $\frac{\Omega(n+k)}{\Omega(n)}<\beta$.
