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

On some planet, there are $2^N$ countries $(N \geq 4).$ Each country has a flag $N$ units wide and one unit high composed of $N$ fields of size $1 \times 1,$ each field being either yellow or blue. No two countries have the same flag. We say that a set of $N$ flags is diverse if these flags can be arranged into an $N \times N$ square so that all $N$ fields on its main diagonal will have the same color. Determine the smallest positive integer $M$ such that among any $M$ distinct flags, there exist $N$ flags forming a diverse set.

[i]
