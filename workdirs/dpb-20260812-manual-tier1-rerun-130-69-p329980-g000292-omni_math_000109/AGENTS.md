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

Find all functions $f: \mathbb{R}^2 \rightarrow \mathbb{R}$, such that
1) $f(0,x)$ is non-decreasing ;
2) for any $x,y \in \mathbb{R}$, $f(x,y)=f(y,x)$ ;
3) for any $x,y,z \in \mathbb{R}$, $(f(x,y)-f(y,z))(f(y,z)-f(z,x))(f(z,x)-f(x,y))=0$ ;
4) for any $x,y,a \in \mathbb{R}$, $f(x+a,y+a)=f(x,y)+a$ .
