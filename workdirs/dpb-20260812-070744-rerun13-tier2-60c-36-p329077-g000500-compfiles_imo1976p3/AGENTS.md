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

A rectangular box can be completely filled with unit cubes. If one places
as many cubes as possible, each with volume 2, in the box, with their edges
parallel to the edges of the box, one can fill exactly 40% of the box.
Determine the possible dimensions of the box.
The box has integer dimensions `a ≤ b ≤ c`. A cube of volume `2` has side
length `k = ∛2` (the real cube root of two). A placement of such cubes in the
box, with edges parallel to the edges of the box, is formalized as a finite set
`P` of corner positions satisfying `IsPacking a b c P`: every cube lies inside
the box and distinct cubes have disjoint interiors (`NonOverlapping`).
The maximal number of cubes that fit is
`maxNumCubes a b c = ⌊a / k⌋₊ * ⌊b / k⌋₊ * ⌊c / k⌋₊`: along an edge of
integer length `n` exactly `⌊n / k⌋₊` cubes fit. The maximality is proved
formally rather than asserted: `packing_card_le` shows that no packing has more
cubes (the map sending a cube at `(x, y, z)` to the triple
`(⌊x / k⌋₊, ⌊y / k⌋₊, ⌊z / k⌋₊)` is injective on a packing), and
`exists_packing` shows that the grid arrangement attains the bound.
The "exactly 40%" condition is stated explicitly as
`2 * P.card = 40 / 100 * (a * b * c)` for a maximal packing `P`: the total
volume of the cubes is 40% of the box volume. Since a maximal packing has
`P.card = maxNumCubes a b c`, this is equivalent to
`a * b * c = 5 * (⌊a / k⌋₊ * ⌊b / k⌋₊ * ⌊c / k⌋₊)`, which is the form used
by the integer-arithmetic core of the proof.
