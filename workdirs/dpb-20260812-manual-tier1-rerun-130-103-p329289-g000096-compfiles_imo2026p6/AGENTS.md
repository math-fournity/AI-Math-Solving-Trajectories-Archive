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

Let a₁, a₂, a₃, … be an infinite sequence of positive integers greater
than 1. Suppose that for all positive integers n, the number a_{n+1} is the
smallest positive integer greater than a_n such that gcd(a_{n+1}, a_i) > 1
for every i = 1, 2, …, n.
Prove that there exist positive integers T and L such that a_{n+T} = a_n + L
for every positive integer n.
(Note that gcd(x, y) denotes the greatest common divisor of positive integers
x and y.)
Statement formalization adapted from AxiomMath/IMO2026; proof adapted from Humanfia's Kimi-K3 solutions (https://github.com/humanfia/imo2026).
