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

A hunter and an invisible rabbit play a game in the Euclidean plane.
The rabbit's starting point, A₀, and the hunter's starting point, B₀,
are the same. After n − 1 rounds of the game, the rabbit is at point
A_{n−1} and the hunter is at point B_{n−1}. In the n-th round of the game,
three things occur in order:
(i) The rabbit moves invisibly to a point Aₙ such that the distance
between A_{n−1} and Aₙ is exactly 1.
(ii) A tracking device reports a point Pₙ to the hunter. The only
guarantee provided by the tracking device to the hunter is that the
distance between Pₙ and Aₙ is at most 1.
(iii) The hunter moves visibly to a point Bₙ such that the distance
between B_{n−1} and Bₙ is exactly 1.
Is it always possible, no matter how the rabbit moves, and no matter what
points are reported by the tracking device, for the hunter to choose her
moves so that after 10⁹ rounds she can ensure that the distance between
her and the rabbit is at most 100?
The answer is **no**: we show that for every valid hunter strategy there
is a rabbit path and a sequence of reported points such that after `10⁹`
rounds the distance between the hunter and the rabbit exceeds `100`.
The construction formalized here follows Evan Chen's notes
(https://web.evanchen.cc/exams/IMO-2017-notes.pdf): the rabbit repeatedly
increases the square of its distance from the hunter by `1/2` per "phase"
of `400` rounds, using a two-worlds trick (it runs to one of two points
`X`, `Y` symmetric about the line through the current positions, while the
tracking device reports points on that line, so the hunter cannot tell
which point the rabbit went to).
