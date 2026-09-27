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

Let \( k \) be a field, \( A := k[X_1, X_2, \dots] \) a polynomial ring, \( m_1 < m_2 < \cdots \) positive integers with \( m_{i+1} - m_i > m_i - m_{i-1} \) for \( i > 1 \). Set \[\mathfrak{p}_i := (X_{m_i+1}, \dots, X_{m_{i+1}})\] and \( S := A - \bigcup_{i \geq 1} \mathfrak{p}_i \). Show that  \( S^{-1}A \) is noetherian with infinite krull dimension.
