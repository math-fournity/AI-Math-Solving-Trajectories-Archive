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

Let n > 2 be an integer and let ℓ ∈ {1, 2, ..., n}. A collection A₁, ..., Aₖ
of (not necessarily distinct) subsets of {1, 2, ..., n} is called ℓ-large if
|Aᵢ| ≥ ℓ for all 1 ≤ i ≤ k. Find, in terms of n and ℓ, the largest real
number c such that the inequality
∑ᵢ ∑ⱼ xᵢ xⱼ |Aᵢ ∩ Aⱼ|²/(|Aᵢ|·|Aⱼ|) ≥ c (∑ᵢ xᵢ)²
holds for all positive integers k, all nonnegative real numbers x₁, ..., xₖ,
and all ℓ-large collections A₁, ..., Aₖ of subsets of {1, ..., n}.
