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

Define the sequences $(a_n),(b_n)$ by
\begin{align*}
& a_n, b_n > 0, \forall n\in\mathbb{N_+} \\ 
& a_{n+1} = a_n - \frac{1}{1+\sum_{i=1}^n\frac{1}{a_i}} \\ 
& b_{n+1} = b_n + \frac{1}{1+\sum_{i=1}^n\frac{1}{b_i}}
\end{align*}
1) If $a_{100}b_{100} = a_{101}b_{101}$, find the value of $a_1-b_1$;
2) If $a_{100} = b_{99}$, determine which is larger between $a_{100}+b_{100}$ and $a_{101}+b_{101}$.
