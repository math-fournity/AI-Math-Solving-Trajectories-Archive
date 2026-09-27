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

A site is any point (x, y) in the plane for which x, y ∈ {1, . . . , 20}.
Initially, each of the 400 sites is unoccupied. Amy and Ben take turns
placing stones on unoccupied sites, with Amy going first; Amy has the
additional restriction that no two of her stones may be at a distance
equal to √5. They stop once either player cannot move. Find the greatest
K such that Amy can ensure that she places at least K stones.
* We use 0-indexed coordinates, so a site is an element of
`Fin 20 × Fin 20`.
* Two sites are at distance `√5` exactly when they are a knight's move
apart: their coordinate differences are 1 and 2 in some order
(`KnightAdj`).
* `CanEnsure K fuel red blue` says that from the position with red
stones on `red`, blue stones on `blue`, and Amy to move, Amy can
ensure that she places at least `K` stones in total. The `fuel`
parameter bounds the number of rounds left to play; every round
occupies two new sites, so `CanEnsure K 400 ∅ ∅` (with fuel exceeding
any possible length of play) is the exact game-theoretic meaning of
"Amy can ensure at least `K` stones", abbreviated `AmyEnsures K`.
The answer is `K = 100`.
