# Solver Task

You are a mathematical problem analysis assistant. You will NOT solve any problems.
You will analyze the relationship between a standard solution and an AI's attempted solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search. Do NOT read any files.
- All information you need is already in your prompt above. Do NOT read any files.
- Output your analysis directly in your response (in this TUI).
- End your analysis with a line containing exactly: `### ANALYSIS COMPLETE`

## Analysis Task

You are given three inputs:
1. **Problem** — a math competition problem
2. **Standard Solution** — the correct solution from the problem bank
3. **AI's Thinking** — an AI's attempted solution process (its reasoning when it tried to solve the problem, but failed)

Your task: analyze WHY the AI failed, by comparing its thinking with the standard solution.

### Dimension 1: Failure Type

Compare the standard solution's key approach with the AI's thinking:

- **DIRECTION_ERROR**: The AI's thinking went in a fundamentally wrong direction. The standard solution uses a specific mathematical approach that the AI never considered. The AI was exploring a completely different strategy. The failure is about *which direction to explore*, not about running out of time.

- **TOKEN_LIMIT**: The AI's thinking was going in the RIGHT direction — it was using the same key approach as the standard solution (or a valid alternative) — but ran out of tokens before completing the proof. The failure is about *not enough time*, not about *wrong direction*.

- **CONNECTION_ERROR**: The AI didn't really attempt the problem — the thinking is extremely short (< 500 chars), contains API connection errors, garbled text, or has NO mathematical content at all (e.g., only error messages or empty output). This is a technical failure, not a mathematical one. **Important**: If the AI solved a DIFFERENT problem than the one given (wrong problem, misread problem), that is DIRECTION_ERROR, not CONNECTION_ERROR. CONNECTION_ERROR is only for technical failures where no real thinking happened.

- **PARTIAL_PROGRESS**: The AI's thinking was partially in the right direction — it identified some key ideas from the standard solution — but missed the crucial turning point. The AI was on the right track but took a wrong turn at a critical juncture.

### Dimension 2: Key Turning Point Type

If the verdict is DIRECTION_ERROR or PARTIAL_PROGRESS, identify what type of key turning point the standard solution uses:

1. **mod_p_grouping**: The standard solution uses modular arithmetic (mod p, where p is small/obvious like 4, 8) to group/categorize objects and find a contradiction or hidden structure.

2. **mod_p_non_obvious**: The standard solution uses modular arithmetic where the prime p is NOT obvious from the problem statement (e.g., mod 11, mod p where p needs to be discovered through analysis).

3. **quadratic_residue_euler**: The standard solution uses quadratic residues, Legendre symbols, or Euler's criterion.

4. **lte_lemma**: The standard solution uses the Lifting The Exponent (LTE) lemma.

5. **p_adic_valuation**: The standard solution uses p-adic valuation (v_p) analysis.

6. **multi_step_mod_p**: The standard solution uses multiple steps of modular arithmetic analysis (not just one mod operation).

7. **crt**: The standard solution uses the Chinese Remainder Theorem (combining information from multiple moduli).

8. **permutation_polynomial**: The standard solution uses properties of permutation polynomials over finite fields.

9. **finite_field_structure**: The standard solution exploits the structure of finite fields (Z/pZ, F_p, F_p^k).

10. **other**: None of the above categories fit. Describe the technique in dimension2_explanation.

### Output Format

Output your analysis in this EXACT XML format. The XML must be well-formed and parseable.

```xml
<analysis>
  <problem_id>polymath_05483</problem_id>
  <dimension1_verdict>DIRECTION_ERROR|TOKEN_LIMIT|CONNECTION_ERROR|PARTIAL_PROGRESS</dimension1_verdict>
  <dimension1_explanation>1-3 sentences explaining the verdict</dimension1_explanation>
  <dimension2_turning_point_type>mod_p_grouping|mod_p_non_obvious|quadratic_residue_euler|lte_lemma|p_adic_valuation|multi_step_mod_p|crt|permutation_polynomial|finite_field_structure|other</dimension2_turning_point_type>
  <dimension2_explanation>1-3 sentences describing the key turning point in the standard solution</dimension2_explanation>
  <ai_direction_summary>1 sentence describing what direction the AI's thinking went</ai_direction_summary>
  <standard_solution_key_technique>1 sentence describing the key technique in the standard solution</standard_solution_key_technique>
  <confidence>high|medium|low</confidence>
</analysis>
```

After the XML block, output exactly: `### ANALYSIS COMPLETE`

**Rules:**
- The XML must be inside a ```xml code block
- Do NOT add any text before or after the XML block (except ### ANALYSIS COMPLETE)
- If the AI's thinking is too short to analyze (< 500 chars AND no mathematical content), output CONNECTION_ERROR. But if the AI solved a different problem or went in the wrong direction, use DIRECTION_ERROR even if the thinking is short.
- If you cannot determine the turning point type, use "other" and explain in dimension2_explanation

## Problem

Pebbles are placed on the squares of an $n \times n$ board in such a way that each square contains at most one pebble. The pebble set of a square of the board is the collection of all pebbles which are in the same row or column as this square. (A pebble belongs to the pebble set of the square in which it is placed.) Let $P(n)$ be the least possible number of pebbles on the board such that no two squares have the same pebble set. Calculate $P(2021)$.

## Standard Solution

The original solution derives that the minimum number of pebbles $P(n)$ for an $n \times n$ board is given by the formula $P(n) = n + \lfloor \frac{n}{2} \rfloor$. For $n = 2021$, we calculate $P(2021) = 2021 + \lfloor \frac{2021}{2} \rfloor = 2021 + 1010 = 3031$.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We need to find P(n), the minimum number of pebbles on an n×n board such that no two squares have the same pebble set.

First, let me understand the problem. Each square has a "pebble set" = all pebbles in the same row or column as that square. We need all n² squares to have distinct pebble sets.

Let me think about this. Let's say we place pebbles. For each square (i,j), its pebble set is the set of pebbles in row i plus the set of pebbles in column j.

Let me think about what determines the pebble set of square (i,j). It's the union of pebbles in row i and pebbles in column j.

Let r_i = set of columns where pebbles are placed in row i. Let c_j = set of rows where pebbles are placed in column j.

The pebble set of square (i,j) is the set of all pebbles (k, l) where either k=i (same row) or l=j (same column). So it's {(i, l) : l ∈ r_i} ∪ {(k, j) : k ∈ c_j}.

Note that (i,j) itself is in this set iff there's a pebble at (i,j), i.e., iff j ∈ r_i (equivalently i ∈ c_j).

Two squares (i,j) and (i',j') have the same pebble set iff:
{(i,l) : l ∈ r_i} ∪ {(k,j) : k ∈ c_j} = {(i',l) : l ∈ r_{i'}} ∪ {(k,j') : k ∈ c_{j'}}

Let me think about when two squares in the same row have the same pebble set. (i,j) and (i,j') with j≠j'. Their pebble sets are:
- (i,j): row i pebbles ∪ column j pebbles
- (i,j'): row i pebbles ∪ column j' pebbles

These are equal iff column j pebbles = column j' pebbles (since row i pebbles are common, and the column pebbles for different columns are disjoint from each other... wait, not exactly, because a pebble at (i,j) is in both row i and column j).

Hmm, let me be more careful. The pebble set of (i,j) = {pebbles in row i} ∪ {pebbles in column j}. A pebble at position (k,l) is in this set iff k=i or l=j.

For (i,j) and (i,j') in the same row (j≠j'):
- Pebble (k,l) is in set of (i,j) iff k=i or l=j
- Pebble (k,l) is in set of (i,j') iff k=i or l=j'

For these to be equal, consider a pebble at (k,j) with k≠i. This is in set of (i,j) but in set of (i,j') only if k=i (no) or l=j' (no, l=j≠j'). So it's in set of (i,j) but not (i,j'). For equality, there must be no pebble at (k,j) for any k≠i. Similarly, no pebble at (k,j') for any k≠i.

So columns j and j' must have pebbles only in row i (if any). So c_j ⊆ {i} and c_{j'} ⊆ {i}.

Also, we need the pebbles at (i,j) and (i,j') themselves to match up. If there's a pebble at (i,j), it's in both sets (since it's in row i). If there's a pebble at (i,j'), it's in both sets. So actually the pebble at (i,j) is in set of (i,j') because k=i. And pebble at (i,j') is in set of (i,j) because k=i. So these are fine.

So (i,j) and (i,j') have the same pebble set iff columns j and j' have no pebbles outside row i. I.e., c_j ⊆ {i} and c_{j'} ⊆ {i}.

Similarly, (i,j) and (i',j) in the same column have the same pebble set iff r_i ⊆ {j} and r_{i'} ⊆ {j}.

Now for (i,j) and (i',j') with i≠i' and j≠j':
- Set of (i,j) = {pebbles with row=i or col=j}
- Set of (i',j') = {pebbles with row=i' or col=j'}

A pebble at (i,j') is in set of (i,j) (row=i) and in set of (i',j') (col=j'). A pebble at (i',j) is in set of (i,j) (col=j) and in set of (i',j') (row=i').

A pebble at (i,j) is in set of (i,j) but in set of (i',j') only if row=i' (no) or col=j' (no). So pebble at (i,j) is NOT in set of (i',j'). Similarly pebble at (i',j') is NOT in set of (i,j).

So for equality: if there's a pebble at (i,j), it must also be in set of (i',j'), contradiction. So no pebble at (i,j) or (i',j').

Also, pebbles at (i, l) for l≠j,j': in set of (i,j) (row i), in set of (i',j') iff l=j' (yes if l=j'). So pebble at (i,j') is in both. Pebble at (i,l) for l≠j,j' is in set of (i,j) but not (i',j'). So no pebbles in row i except possibly at column j'. Similarly no pebbles in row i' except possibly at column j. No pebbles in column j except possibly at row i'. No pebbles in column j' except possibly at row i.

So the only possible pebbles in rows i, i' and columns j, j' are at positions (i,j') and (i',j). And we showed no pebble at (i,j) or (i',j').

For the sets to be equal, we need: set of (i,j) = set of (i',j'). 
- Set of (i,j) = {(i,j') if pebble there} ∪ {(i',j) if pebble there} ∪ {all pebbles in column j} ∪ {all pebbles in row i}
  But we said row i has pebbles only possibly at j', and column j has pebbles only possibly at i'. So set of (i,j) = {(i,j') if pebble, (i',j) if pebble}.
- Similarly set of (i',j') = {(i,j') if pebble, (i',j) if pebble}.

So they're always equal! Wait, that means (i,j) and (i',j') always have the same pebble set if the only pebbles in rows i,i' and columns j,j' are at (i,j') and (i',j)?

Hmm wait, I need to be more careful. Let me reconsider. The pebble set of (i,j) includes ALL pebbles in row i and ALL pebbles in column j. Not just those in the 2×2 sub-board.

Let me redo this. Set of (i,j) = {all pebbles in row i} ∪ {all pebbles in column j}. Set of (i',j') = {all pebbles in row i'} ∪ {all pebbles in column j'}.

A pebble at (i, l) where l ∉ {j, j'}: in set of (i,j) (row i), not in set of (i',j') (row ≠ i', col ≠ j'). So for equality, no such pebble. So r_i ⊆ {j, j'}.

A pebble at (i', l) where l ∉ {j, j'}: in set of (i',j') not in set of (i,j). So r_{i'} ⊆ {j, j'}.

A pebble at (k, j) where k ∉ {i, i'}: in set of (i,j) not in set of (i',j'). So c_j ⊆ {i, i'}.

A pebble at (k, j') where k ∉ {i, i'}: in set of (i',j') not in set of (i,j). So c_{j'} ⊆ {i, i'}.

Now, pebble at (i,j): in set of (i,j). In set of (i',j')? row ≠ i', col ≠ j'. No. So no pebble at (i,j).
Pebble at (i',j'): in set of (i',j'). In set of (i,j)? No. So no pebble at (i',j').

Pebble at (i,j'): in set of (i,j) (row i), in set of (i',j') (col j'). In both. OK.
Pebble at (i',j): in set of (i,j) (col j), in set of (i',j') (row i'). In both. OK.

So the pebbles in rows i, i' and columns j, j' can only be at (i,j') and (i',j). And set of (i,j) = {pebbles in row i} ∪ {pebbles in col j} = {(i,j') if pebble} ∪ {(i',j) if pebble} ∪ (pebbles in row i outside cols j,j' — none) ∪ (pebbles in col j outside rows i,i' — none).

Wait, I also need to account for pebbles in row i at columns other than j, j'. We showed r_i ⊆ {j, j'}, and no pebble at (i,j), so r_i ⊆ {j'}. Similarly r_{i'} ⊆ {j}, c_j ⊆ {i'}, c_{j'} ⊆ {i}.

So set of (i,j) = {(i,j') if j'∈r_i} ∪ {(i',j) if i'∈c_j} = set of (i',j') = {(i,j') if i∈c_{j'}} ∪ {(i',j) if j∈r_{i'}}.

These are the same: both are {(i,j') if pebble at (i,j'), (i',j) if pebble at (i',j)}. So yes, they're always equal!

So: (i,j) and (i',j') (with i≠i', j≠j') have the same pebble set iff:
- r_i ⊆ {j'}, r_{i'} ⊆ {j}, c_j ⊆ {i'}, c_{j'} ⊆ {i}
- No pebble at (i,j) or (i',j')

Which means: rows i and i' each have at most 1 pebble (at j' and j respectively), and columns j and j' each have at most 1 pebble (at i' and i respectively).

OK so this is getting complex. Let me think about this differently.

Let me think about the structure. Let's denote the pebble configuration. The pebble set of (i,j) is determined by (r_i, c_j) — the set of pebbled columns in row i and the set of pebbled rows in column j. Actually, it's determined by the actual pebbles, which is the union of row i's pebbles and column j's pebbles.

Two squares (i,j) and (i',j') have the same pebble set iff the union {row i pebbles} ∪ {col j pebbles} = {row i' pebbles} ∪ {col j' pebbles}.

Let me think about it in terms of a bipartite graph. Consider a bipartite graph with rows on one side and columns on the other. A pebble at (i,j) is an edge between row i and column j. The pebble set of square (i,j) corresponds to the set of edges incident to vertex i (row side) or vertex j (column side) in this bipartite graph.

So we have a bipartite graph G with parts R = {r_1, ..., r_n} and C = {c_1, ..., c_n}. For each pair (i,j), the "pebble set" is the set of edges incident to r_i or c_j. We need all n² pairs to give distinct edge sets.

The number of pebbles = number of edges = |E|.

We want to minimize |E| such that all n² pairs (r_i, c_j) have distinct "neighborhood edge sets" (edges incident to r_i or c_j).

Let me denote N(r_i) = set of edges incident to r_i, N(c_j) = set of edges incident to c_j. The pebble set of (i,j) is N(r_i) ∪ N(c_j).

We need N(r_i) ∪ N(c_j) to be distinct for all (i,j).

Note that N(r_i) ∪ N(c_j) always contains the edge (r_i, c_j) if it exists. 

Let me think about what N(r_i) ∪ N(c_j) looks like. An edge (r_a, c_b) is in this union iff a=i or b=j.

So the pebble set of (i,j) = {(i,b) : (i,b) ∈ E} ∪ {(a,j) : (a,j) ∈ E} = edges in row i ∪ edges in column j.

This is exactly the set of edges in the "cross" formed by row i and column j.

Now, two crosses (i,j) and (i',j') give the same edge set. When?

Case 1: i=i', j≠j'. Same row, different columns. Cross (i,j) = row i edges ∪ col j edges. Cross (i,j') = row i edges ∪ col j' edges. These are equal iff col j edges = col j' edges (after removing the intersection with row i, but actually we need to be careful).

Actually, row i edges ∪ col j edges = row i edges ∪ col j' edges. The edges in col j but not in row i must equal edges in col j' but not in row i. So col j \ row i = col j' \ row i (as edge sets). Since col j edges not in row i = edges (a,j) with a≠i, and similarly for j'. So we need: {(a,j) ∈ E : a≠i} = {(a,j') ∈ E : a≠i}. 

So columns j and j' have the same set of pebbles outside row i. If both columns have no pebbles outside row i, they're equal. Or if they have the same pebbles outside row i.

Case 2: i≠i', j=j'. Similar by symmetry.

Case 3: i≠i', j≠j'. As analyzed above, this requires very restrictive conditions.

Let me think about the problem from the perspective of what makes crosses distinct.

Let me think about small cases first.

P(1): 1×1 board. One square, trivially all distinct. P(1) = 0.

P(2): 2×2 board. 4 squares, need 4 distinct pebble sets. 

With 0 pebbles: all 4 squares have empty set. Not distinct.
With 1 pebble at (1,1): 
- (1,1): {(1,1)}
- (1,2): {(1,1)} (row 1)
- (2,1): {(1,1)} (col 1)
- (2,2): {} 
Not distinct (three have {(1,1)}... wait, (1,2) has row 1 pebbles = {(1,1)}, (2,1) has col 1 pebbles = {(1,1)}, (2,2) has nothing). So (1,1), (1,2), (2,1) all have {(1,1)}. Not distinct.

With 2 pebbles: Try (1,1) and (2,2):
- (1,1): row 1 = {(1,1)}, col 1 = {(1,1)}, union = {(1,1)}
- (1,2): row 1 = {(1,1)}, col 2 = {(2,2)}, union = {(1,1),(2,2)}
- (2,1): row 2 = {(2,2)}, col 1 = {(1,1)}, union = {(1,1),(2,2)}
- (2,2): row 2 = {(2,2)}, col 2 = {(2,2)}, union = {(2,2)}
(1,2) and (2,1) have the same set. Not distinct.

Try (1,1) and (1,2):
- (1,1): row 1 = {(1,1),(1,2)}, col 1 = {(1,1)}, union = {(1,1),(1,2)}
- (1,2): row 1 = {(1,1),(1,2)}, col 2 = {(1,2)}, union = {(1,1),(1,2)}
Same. Not distinct.

Try (1,1) and (2,1):
- (1,1): row 1 = {(1,1)}, col 1 = {(1,1),(2,1)}, union = {(1,1),(2,1)}
- (2,1): row 2 = {(2,1)}, col 1 = {(1,1),(2,1)}, union = {(1,1),(2,1)}
Same.

Try (1,1) and (2,1) — same issue by symmetry.

Hmm, with 2 pebbles it seems hard. Let me try (1,1) and (1,2) — nope. 

What about 3 pebbles? Try (1,1), (1,2), (2,1):
- (1,1): row1={(1,1),(1,2)}, col1={(1,1),(2,1)}, union={(1,1),(1,2),(2,1)}
- (1,2): row1={(1,1),(1,2)}, col2={(1,2)}, union={(1,1),(1,2)}
- (2,1): row2={(2,1)}, col1={(1,1),(2,1)}, union={(1,1),(2,1)}
- (2,2): row2={(2,1)}, col2={(1,2)}, union={(1,2),(2,1)}
All four distinct! So P(2) ≤ 3.

Can we do it with 2? We tried all 2-pebble configs above (up to symmetry) and none worked. Actually let me try (1,1),(2,1):
Already tried, (1,1) and (2,1) have same set.

So P(2) = 3.

Hmm, let me think about the general pattern. 

Actually, let me think about this more carefully using the bipartite graph framework.

The pebble set of (i,j) = edges incident to r_i ∪ edges incident to c_j. Let's call this S(i,j).

Note that S(i,j) is determined by the pair (N(r_i), N(c_j)) where N denotes the set of incident edges. But actually S(i,j) = N(r_i) ∪ N(c_j), and this is determined by the neighborhoods.

For S(i,j) to be distinct for all pairs, we need: if N(r_i) ∪ N(c_j) = N(r_{i'}) ∪ N(c_{j'}), then i=i' and j=j'.

Let me think about what information S(i,j) encodes. 

Key insight: S(i,j) tells us which edges are in row i or column j. From S(i,j), can we recover i and j?

If we know the graph, S(i,j) is the set of edges in the "cross" at (i,j). 

Let me think about it differently. Let d(r_i) = degree of row vertex i, d(c_j) = degree of column vertex j. The size of S(i,j) = d(r_i) + d(c_j) - [edge (i,j) exists ? 1 : 0].

Hmm, this gives us |S(i,j)| = d(r_i) + d(c_j) - a_{ij} where a_{ij} is the adjacency.

For all n² values to be distinct... well, they don't need distinct sizes, just distinct sets.

Let me think about a construction. 

Construction idea: Place pebbles to form a "staircase" or some structured pattern.

Let me think about what happens if we place pebbles on the diagonal: (i,i) for i=1,...,n. Then:
- S(i,j) = {(i,i)} ∪ {(j,j)} if i≠j, or {(i,i)} if i=j.
Wait: row i has pebble at (i,i), col j has pebble at (j,j). So S(i,j) = {(i,i), (j,j)} (if i≠j) or {(i,i)} (if i=j).

For i≠j: S(i,j) = {(i,i),(j,j)} = S(j,i). So (i,j) and (j,i) have the same set. Not good.

So diagonal alone doesn't work. We need more pebbles.

Let me think about the problem differently. 

Let me consider the "signature" of each square. S(i,j) = N(r_i) ∪ N(c_j). 

Claim: S(i,j) determines the pair (N(r_i), N(c_j)) up to some ambiguity. Actually, N(r_i) ⊆ S(i,j) and N(c_j) ⊆ S(i,j). Also, N(r_i) = edges in S(i,j) that are in row i, and N(c_j) = edges in S(i,j) that are in column j. But we don't know i and j from S(i,j) directly...

Actually, from S(i,j), we can figure out: the edges in S(i,j) are exactly those in some row i and some column j. The row edges all share the same row index, and the column edges all share the same column index. So from S(i,j), we can identify which edges are "row edges" (they all have the same first coordinate) and which are "column edges" (same second coordinate), except for the edge (i,j) itself which is both.

Hmm, but we know the graph, so we know which edges exist. Given S(i,j), we need to find (i,j) such that S = N(r_i) ∪ N(c_j).

Let me think about lower bounds. 

Lower bound approach: We need n² distinct sets. Each set S(i,j) is a subset of the edge set E. The number of distinct subsets is at most 2^|E|. So we need 2^|E| ≥ n², giving |E| ≥ 2 log₂ n. But this is very weak.

Better approach: Think about what distinguishes squares in the same row. For squares (i,j) and (i,j') in the same row, S(i,j) ≠ S(i,j') requires that the column parts differ. Specifically, {(a,j) ∈ E : a≠i} ≠ {(a,j') ∈ E : a≠i}. 

So for each row i, the n columns must give distinct "column signatures" when restricted to rows ≠ i. The column signature of column j (restricted to rows ≠ i) is the set of pebbles in column j excluding row i.

Hmm, this is getting complicated. Let me look for a pattern.

Let me think about the problem in terms of coding theory or combinatorial design.

Alternative approach: Think of each row i as having a "row code" r_i (the set of columns with pebbles in row i) and each column j as having a "column code" c_j (the set of rows with pebbles in column j). The pebble set of (i,j) is determined by (r_i, c_j) — specifically, it's the set of pebbles {(i, l) : l ∈ r_i} ∪ {(k, j) : k ∈ c_j}.

Two pairs (i,j) and (i',j') give the same pebble set iff:
{(i,l) : l ∈ r_i} ∪ {(k,j) : k ∈ c_j} = {(i',l) : l ∈ r_{i'}} ∪ {(k,j') : k ∈ c_{j'}}

Since pebbles are identified by their position (row, col), and the row-pebbles have row=i while column-pebbles have col=j, we can decompose: the pebbles in S(i,j) with row=i are exactly {(i,l) : l ∈ r_i}, and those with col=j are {(k,j) : k ∈ c_j}, with overlap at (i,j) if j ∈ r_i.

So from S(i,j), we can extract:
- The row index i: it's the unique row that appears in the "row part" (all pebbles with the same row, which is the row with the most pebbles in S... no, not necessarily).

Actually, given S(i,j), the pebbles in it are of two types: those in some row i and those in some column j. The pebbles in row i all have first coordinate i. The pebbles in column j all have second coordinate j. So from S(i,j), we can identify i as the first coordinate of the "row pebbles" and j as the second coordinate of the "column pebbles". But the edge (i,j) (if it exists) belongs to both.

So given S(i,j), we can determine i and j (and hence the pair (i,j) is determined), UNLESS there's ambiguity. The ambiguity arises when we can't tell which pebbles are "row pebbles" and which are "column pebbles".

More precisely, given the set S of edges, we need to find (i,j) such that S = {edges in row i} ∪ {edges in column j}. This means: all edges in S are either in row i or in column j. And all edges in row i or column j are in S.

So i is a row such that all edges in S not in column j are in row i, and j is a column such that all edges in S not in row i are in column j.

Given S, the possible (i,j) pairs are those where:
- Every edge in S has first coordinate i or second coordinate j.
- Every edge with first coordinate i or second coordinate j is in S.

The first condition: S ⊆ (row i ∪ col j), meaning all edges in S are in row i or col j.
The second condition: (row i ∪ col j) ⊆ S, meaning all edges in row i or col j are in S.
Together: S = row i ∪ col j (as edge sets).

So the question is: for how many pairs (i,j) can S = row_i_edges ∪ col_j_edges?

We need this to be exactly 1 for each S (i.e., each S corresponds to a unique (i,j)).

Now, given S, let R(S) = set of rows that appear in S, C(S) = set of columns that appear in S. For S = row_i ∪ col_j, every edge in S has row = i or col = j. So R(S) ⊆ {i} ∪ {rows of edges in col j} and C(S) ⊆ {j} ∪ {cols of edges in row i}.

Actually, R(S) = {i} ∪ c_j (the rows that have pebbles in column j) and C(S) = r_i ∪ {j} (the columns that have pebbles in row i).

So from S, we know R(S) and C(S). For S to correspond to a unique (i,j), we need that there's a unique way to choose i ∈ R(S) and j ∈ C(S) such that S = row_i ∪ col_j.

Given S, i must be in R(S) and j must be in C(S). For a candidate (i,j), we need:
1. All edges in S have row i or col j.
2. All edges in row i or col j are in S.

Condition 1 means: every edge (a,b) in S has a=i or b=j. So R(S) \ {i} must have all their edges in S only through column j, and C(S) \ {j} must have all their edges in S only through row i. More precisely, for any edge (a,b) in S with a≠i, we need b=j. And for any edge (a,b) in S with b≠j, we need a=i.

So: edges in S with col ≠ j must all have row = i. Edges in S with row ≠ i must all have col = j.

This means: S \ col_j ⊆ row_i and S \ row_i ⊆ col_j. Equivalently, S = (S ∩ row_i) ∪ (S ∩ col_j) and S ∩ row_i ∩ col_j = {(i,j)} if it exists.

OK let me think about this more concretely. 

Given the edge set E (the pebble placement), define for each (i,j): S(i,j) = edges in row i ∪ edges in column j. We need all S(i,j) distinct.

Let me think about a specific construction and count pebbles.

Construction: Place pebbles at positions (i, j) where i ≤ j (upper triangle including diagonal). No wait, let me think more carefully.

Let me try to think about what the answer might be. This is a competition problem asking for P(2021), so the answer is likely a nice formula in n.

Let me compute P(n) for small n.

P(1) = 0.
P(2) = 3.

Let me compute P(3).

For n=3, we need 9 distinct pebble sets. Let me try to find a good construction.

Let me try placing pebbles at: (1,1), (1,2), (1,3), (2,1), (3,1). That's 5 pebbles (first row and first column full, like an L-shape, but without (1,1) double-counted — actually it's row 1 full and column 1 full, which is 3+3-1=5 pebbles).

S(i,j) for this:
Row 1 pebbles: (1,1),(1,2),(1,3). Col 1 pebbles: (1,1),(2,1),(3,1).
- S(1,1) = {(1,1),(1,2),(1,3),(2,1),(3,1)} = all 5
- S(1,2) = row1 ∪ col2 = {(1,1),(1,2),(1,3)} (col2 has no pebbles) = {(1,1),(1,2),(1,3)}
- S(1,3) = row1 ∪ col3 = {(1,1),(1,2),(1,3)} = same as S(1,2). Not distinct!

So this doesn't work because columns 2 and 3 are empty, so S(1,2) = S(1,3).

We need each column to have a distinct "signature" when combined with each row.

Let me try a different approach. Let me think about what makes all S(i,j) distinct.

For fixed row i, S(i,j) varies with j only through the column part. S(i,j) = row_i_edges ∪ col_j_edges. For j≠j', S(i,j) ≠ S(i,j') iff col_j_edges \ row_i ≠ col_{j'}_edges \ row_i. 

So for each row i, the n columns must have distinct "residuals" col_j \ row_i (pebbles in col j not in row i).

The residual of column j w.r.t. row i is the set of pebbles in column j at rows ≠ i. For this to be distinct for all j, we need... well, if column j has pebbles at rows set c_j, then the residual is c_j \ {i} (if i ∈ c_j) or c_j (if i ∉ c_j).

For two columns j, j' to have the same residual w.r.t. row i: c_j \ {i} = c_{j'} \ {i}. This happens iff c_j and c_{j'} differ at most by whether they contain i.

So for each row i, we need: no two columns j, j' have c_j \ {i} = c_{j'} \ {i}. This means: for each row i, the multiset {c_j \ {i} : j = 1..n} has all distinct elements.

c_j \ {i} = c_{j'} \ {i} iff c_j Δ c_{j'} ⊆ {i}, i.e., c_j and c_{j'} differ only possibly at i. So for each row i, no two columns have column-sets that differ only at row i.

Similarly, for each column j, no two rows have row-sets that differ only at column j.

And for (i,j) ≠ (i',j') with i≠i' and j≠j', we need S(i,j) ≠ S(i',j'). As we analyzed, S(i,j) = S(i',j') requires very specific conditions (rows i, i' have at most 1 pebble each, columns j, j' have at most 1 pebble each, in a cross pattern).

Let me think about the cross-case more carefully. S(i,j) = S(i',j') with i≠i', j≠j' requires:
- r_i ⊆ {j'}, r_{i'} ⊆ {j}, c_j ⊆ {i'}, c_{j'} ⊆ {i}
- No pebble at (i,j) or (i',j').

So row i has pebbles only possibly at column j', row i' only possibly at column j, column j only possibly at row i', column j' only possibly at row i. And no pebble at (i,j) or (i',j').

So the pebbles in this 2×2 sub-board (rows i,i', cols j,j') can only be at (i,j') and (i',j), and there are no pebbles at (i,j) or (i',j').

Moreover, row i has no pebbles outside column j', row i' has no pebbles outside column j, column j has no pebbles outside row i', column j' has no pebbles outside row i.

So rows i and i' are "sparse" (at most 1 pebble each) and columns j and j' are "sparse" (at most 1 pebble each).

To avoid this, we can ensure that no two rows are both sparse, or no two columns are both sparse, or more precisely, that the cross-pattern condition never holds.

Let me think about a cleaner approach.

Approach: Think of the rows and columns as having "types". Let's say row i has type R_i = r_i (set of pebbled columns) and column j has type C_j = c_j (set of pebbled rows). 

The pebble set S(i,j) is determined by (R_i, C_j), and actually by (R_i, C_j) we can reconstruct S(i,j) = {(i,l): l∈R_i} ∪ {(k,j): k∈C_j}.

For S(i,j) = S(i',j') with (i,j)≠(i',j'):
- If i=i', j≠j': need C_j \ {i} = C_{j'} \ {i}, i.e., C_j and C_{j'} differ only at i.
- If i≠i', j=j': need R_i \ {j} = R_{i'} \ {j}, i.e., R_i and R_{i'} differ only at j.
- If i≠i', j≠j': need the cross-pattern condition.

So the conditions for all S(i,j) distinct are:
(A) For each row i, the sets {C_j \ {i} : j=1..n} are all distinct. Equivalently, for each i, no two columns have types differing only at i.
(B) For each column j, the sets {R_i \ {j} : i=1..n} are all distinct. Equivalently, for each j, no two rows have types differing only at j.
(C) No cross-pattern collision: there's no (i,i',j,j') with i≠i', j≠j' such that R_i ⊆ {j'}, R_{i'} ⊆ {j}, C_j ⊆ {i'}, C_{j'} ⊆ {i}, and no pebble at (i,j) or (i',j').

Hmm, condition (C) is complex. Let me think about when it can be avoided.

If every row has at least 2 pebbles, then R_i ⊆ {j'} is impossible (since |R_i| ≥ 2 > 1 ≥ |{j'}|). So condition (C) is automatically satisfied if every row has ≥ 2 pebbles. Similarly if every column has ≥ 2 pebbles.

Actually, we need R_i ⊆ {j'} meaning |R_i| ≤ 1. So if every row has ≥ 2 pebbles, condition (C) never triggers. Similarly if every column has ≥ 2 pebbles.

So a sufficient condition for all S(i,j) distinct is:
- Every row has ≥ 2 pebbles (or every column has ≥ 2 pebbles), AND
- Condition (A): for each row i, no two column types differ only at i, AND
- Condition (B): for each column j, no two row types differ only at j.

Wait, but we also need condition (A) and (B) even if (C) is satisfied. Let me re-examine.

Actually conditions (A), (B), (C) together are necessary and sufficient. If we ensure every row has ≥ 2 pebbles, (C) is automatic, and we just need (A) and (B).

Now, condition (A): for each row i, no two columns j, j' have C_j \ {i} = C_{j'} \ {i}. This means C_j and C_{j'} differ at some row other than i. In other words, for any two columns j, j', their types C_j and C_{j'} differ at some row k, and for each row i, that difference must be at a row ≠ i. 

Wait, more precisely: for a fixed i, C_j \ {i} ≠ C_{j'} \ {i} for all j≠j'. This means C_j and C_{j'} are not equal after removing i. So C_j Δ C_{j'} ⊄ {i}, i.e., C_j and C_{j'} differ at some element other than i.

For this to hold for ALL i, we need: for every pair j≠j', C_j Δ C_{j'} has size ≥ 2. Because if |C_j Δ C_{j'}| = 1, say they differ only at row i, then for that specific i, C_j \ {i} = C_{j'} \ {i}, violating (A).

Conversely, if |C_j Δ C_{j'}| ≥ 2 for all j≠j', then for any i, C_j \ {i} ≠ C_{j'} \ {i} (since they differ at some row ≠ i).

So condition (A) ⟺ all column types are pairwise at Hamming distance ≥ 2 (i.e., C_j ≠ C_{j'} and they don't differ at exactly one position).

Wait, |C_j Δ C_{j'}| ≥ 2 means they're not equal and not at distance 1. Actually |C_j Δ C_{j'}| ≥ 1 means they're distinct, and ≥ 2 means they're not "adjacent" (differing at exactly one element).

Similarly, condition (B) ⟺ all row types are pairwise at Hamming distance ≥ 2.

So the conditions become:
- All column types pairwise differ in ≥ 2 elements.
- All row types pairwise differ in ≥ 2 elements.
- Either all rows have ≥ 2 pebbles or all columns have ≥ 2 pebbles (to avoid cross-pattern).

Wait, actually I need to double-check the cross-pattern condition. Let me re-examine.

If some row has 0 or 1 pebbles, condition (C) might trigger. But it requires BOTH rows i and i' to have ≤ 1 pebble, AND both columns j and j' to have ≤ 1 pebble. So if at most one row has ≤ 1 pebble, or at most one column has ≤ 1 pebble, condition (C) can't trigger (since we need two rows and two columns with the sparse property).

Actually, we need two distinct rows i, i' with |R_i| ≤ 1 and |R_{i'}| ≤ 1, AND two distinct columns j, j' with |C_j| ≤ 1 and |C_{j'}| ≤ 1. So if at most 1 row has ≤ 1 pebble, (C) can't trigger. Or if at most 1 column has ≤ 1 pebble, (C) can't trigger.

But even then, we need the specific cross-pattern. Let me not worry about (C) for now and focus on (A) and (B), then check (C).

So the problem reduces to: find a bipartite graph on n+n vertices minimizing the number of edges, such that:
- Row types (neighborhoods of row vertices) are pairwise at distance ≥ 2.
- Column types (neighborhoods of column vertices) are pairwise at distance ≥ 2.
- No cross-pattern collision.

The number of edges = sum of row degrees = sum of column degrees.

Now, "pairwise at distance ≥ 2" for the row types means: the row neighborhoods, viewed as subsets of [n], form a code with minimum distance ≥ 2. This is equivalent to saying they form an "anticode" or more precisely a code where no two codewords are at Hamming distance 1.

A set of subsets of [n] with pairwise Hamming distance ≥ 2 is the same as a set of binary vectors of length n with minimum Hamming distance ≥ 2. This is a binary code of length n, size n (we need n row types), minimum distance 2.

The minimum distance 2 condition means the code is a "single-error-detecting" code. The maximum size of such a code of length n is 2^{n-1} (e.g., all vectors of even weight). But we only need n codewords, so this is easily achievable.

The question is: what's the minimum total weight (number of 1s) of n binary vectors of length n with pairwise Hamming distance ≥ 2?

Similarly for columns.

And we want to minimize the total number of edges, which is the sum of row degrees (= sum of column degrees). So we want to minimize the total weight of both the row code and column code, but they're constrained to be the same (since they represent the same bipartite graph).

Wait, the row types and column types are not independent — they come from the same bipartite graph. The row type R_i is the set of columns adjacent to row i, and the column type C_j is the set of rows adjacent to column j. These are related by the adjacency matrix.

So we need an n×n binary matrix A (where A_{ij} = 1 if pebble at (i,j)) such that:
- The rows of A, viewed as binary vectors, have pairwise Hamming distance ≥ 2.
- The columns of A, viewed as binary vectors, have pairwise Hamming distance ≥ 2.
- No cross-pattern collision (which we'll handle separately).
- Minimize the total number of 1s in A.

So we need a binary matrix where all rows are distinct and no two rows differ in exactly one position, and similarly for columns. And we minimize the weight.

Let me think about the minimum weight. 

First, just having all rows distinct (distance ≥ 1) requires at least... well, the rows are n binary vectors of length n, all distinct. The minimum total weight for n distinct binary vectors of length n: we can use the vectors 00...0, 10...0, 01...0, ..., 0...01 (the zero vector and the n unit vectors). But that's n+1 vectors and we only need n. So use n-1 unit vectors and the zero vector: total weight = n-1. But we need distance ≥ 2, not just ≥ 1.

For distance ≥ 2: no two rows can differ in exactly one position. So if one row is the zero vector, no other row can be a unit vector (distance 1 from zero). 

Let me think about this as a coding theory problem. We need n codewords of length n, minimum distance 2, minimizing total weight.

If all codewords have the same parity (all even weight or all odd weight), then the distance between any two is even, so ≥ 2 (as long as they're distinct). So we can use all-even-weight vectors or all-odd-weight vectors.

To minimize total weight with n codewords of the same parity:
- Even weight: the even-weight vectors of smallest weight are: weight 0 (one vector: 00...0), weight 2 (C(n,2) vectors), etc. We need n vectors. If n ≤ 1 + C(n,2), we can use the zero vector and n-1 weight-2 vectors. Total weight = 2(n-1).
- But we need the vectors to be distinct, which they are. And all even weight, so pairwise distance ≥ 2. Total weight = 0 + 2(n-1) = 2(n-1).
- Odd weight: smallest odd weight is 1 (n unit vectors), then weight 3, etc. We need n vectors. If n ≤ n (the unit vectors), we can use all n unit vectors. Total weight = n. But wait, unit vectors are at distance 2 from each other (they differ in 2 positions), so that works! Total weight = n.

Wait, let me check: unit vectors e_1, e_2, ..., e_n. Distance between e_i and e_j (i≠j) is 2 (they differ at positions i and j). So minimum distance is 2. And total weight = n. That's better than 2(n-1) for n ≥ 2.

But can we do even better? What if we use some weight-0 and some weight-2 vectors? The zero vector is at distance 2 from any weight-2 vector, and weight-2 vectors are at distance 2 or 4 from each other. So using 1 zero vector and n-1 weight-2 vectors gives total weight 2(n-1), which is worse than n for n ≥ 3.

What about mixing? We can't mix parities because then we might get distance 1. Actually, we can mix parities as long as no two vectors are at distance 1. For example, weight-0 and weight-2 vectors are fine (distance 2). Weight-1 and weight-3 vectors are fine (distance ≥ 2). But weight-0 and weight-1 are at distance 1, so can't mix those.

So the options are:
- All odd weight: minimum total weight with n vectors. The n unit vectors give total weight n. Can we do better? We need n distinct odd-weight vectors. The minimum weight odd vectors are the n unit vectors (weight 1). Any other odd-weight vector has weight ≥ 3. So using all unit vectors is optimal: total weight = n.
- All even weight: 1 zero vector + (n-1) weight-2 vectors, total weight = 2(n-1). Worse for n ≥ 3.
- Mixed: e.g., some weight-0 and some weight-2 (all even), or some weight-1 and some weight-3 (all odd). Can't do better than n with odd.

Actually wait, can we use fewer than n unit vectors and supplement with higher weight? No, that would increase total weight.

So for the row code alone, the minimum total weight is n (using unit vectors). But we also need the column code to have distance ≥ 2, and the matrix is shared.

If we use unit vectors for rows: row i = e_i (pebble at (i,i) only, i.e., the identity matrix). Then the columns are also unit vectors, which have pairwise distance 2. So the column condition is also satisfied! Total weight = n.

But we need to check condition (C) (cross-pattern). With the identity matrix, every row has exactly 1 pebble and every column has exactly 1 pebble. So |R_i| = 1 for all i, and |C_j| = 1 for all j. Condition (C) requires two rows with ≤ 1 pebble (all rows qualify) and two columns with ≤ 1 pebble (all columns qualify). So we need to check if the cross-pattern actually occurs.

With the identity matrix: R_i = {i}, C_j = {j}. Cross-pattern for (i,j) and (i',j') with i≠i', j≠j':
- R_i ⊆ {j'}: {i} ⊆ {j'} iff i = j'.
- R_{i'} ⊆ {j}: {i'} ⊆ {j} iff i' = j.
- C_j ⊆ {i'}: {j} ⊆ {i'} iff j = i'.
- C_{j'} ⊆ {i}: {j'} ⊆ {i} iff j' = i.
- No pebble at (i,j): i ≠ j.
- No pebble at (i',j'): i' ≠ j'.

So we need i = j', i' = j, i ≠ j, i' ≠ j'. Since i' = j and i = j', and i ≠ j means i ≠ i', and j ≠ j' means j ≠ i (since j' = i). So i ≠ i' and j ≠ j' are the same condition (i ≠ j). So the cross-pattern occurs whenever i ≠ j: take any i ≠ j, set j' = i, i' = j. Then S(i,j) = S(j,i).

Indeed, with the identity matrix, S(i,j) = {(i,i), (j,j)} for i≠j, and S(j,i) = {(j,j), (i,i)} = S(i,j). So (i,j) and (j,i) have the same pebble set. This confirms condition (C) is violated.

So the identity matrix doesn't work because of condition (C). We need to avoid the cross-pattern.

To avoid condition (C), we need: for all i≠i', j≠j', it's NOT the case that R_i ⊆ {j'}, R_{i'} ⊆ {j}, C_j ⊆ {i'}, C_{j'} ⊆ {i}, no pebble at (i,j) and (i',j').

One way: ensure every row has ≥ 2 pebbles. Then R_i ⊆ {j'} is impossible. This costs at least 2n pebbles.

Another way: ensure every column has ≥ 2 pebbles. Also at least 2n.

Or: ensure that at most one row has ≤ 1 pebble, OR at most one column has ≤ 1 pebble. Because condition (C) needs TWO sparse rows and TWO sparse columns.

Wait, let me re-examine. Condition (C) needs two rows i, i' with |R_i| ≤ 1 and |R_{i'}| ≤ 1, AND two columns j, j' with |C_j| ≤ 1 and |C_{j'}| ≤ 1. If at most one row has ≤ 1 pebble, we can't find two such rows, so (C) can't trigger. Similarly for columns.

So if at most one row has 0 or 1 pebbles, condition (C) is avoided. This means n-1 rows have ≥ 2 pebbles and 1 row can have 0 or 1. Total row weight ≥ 2(n-1) + 0 = 2(n-1).

Or if at most one column has ≤ 1 pebble: n-1 columns have ≥ 2 pebbles, total column weight ≥ 2(n-1).

So the minimum is at least 2(n-1) if we use this approach. But maybe we can be cleverer.

Actually, wait. Even if we have two sparse rows and two sparse columns, the cross-pattern might not trigger because of the specific structure. Let me re-examine.

The cross-pattern for (i,j), (i',j') with i≠i', j≠j' requires:
1. R_i ⊆ {j'} (row i has pebbles only possibly at column j')
2. R_{i'} ⊆ {j} (row i' has pebbles only possibly at column j')
3. C_j ⊆ {i'} (column j has pebbles only possibly at row i')
4. C_{j'} ⊆ {i} (column j' has pebbles only possibly at row i)
5. No pebble at (i,j)
6. No pebble at (i',j')

From 1 and 4: if R_i = {j'} (pebble at (i,j')), then C_{j'} contains i, and from 4, C_{j'} ⊆ {i}, so C_{j'} = {i}. Consistent.
If R_i = {} (no pebbles in row i), then from 4, C_{j'} ⊆ {i}, so C_{j'} ⊆ {i}. But also from 1, R_i = {} ⊆ {j'}, fine.

So the cross pattern means: in the 2×2 submatrix at rows (i,i') and columns (j,j'), the only possible pebbles are at (i,j') and (i',j), and there are no pebbles at (i,j) or (i',j'). Moreover, row i has no pebbles outside column j', row i' has no pebbles outside column j, column j has no pebbles outside row i', column j' has no pebbles outside row i.

So this is a very specific condition. Even with sparse rows and columns, it might not trigger if the sparse rows/columns don't align in this cross pattern.

Let me think about this differently. Let me consider the approach where we ensure all rows have ≥ 2 pebbles (or all but one row).

Approach 1: All rows have ≥ 2 pebbles, row types pairwise distance ≥ 2, column types pairwise distance ≥ 2.

Minimum total weight: We need n row vectors of length n, pairwise distance ≥ 2, each of weight ≥ 2. And the column vectors also need pairwise distance ≥ 2.

For the rows: n vectors of length n, weight ≥ 2, pairwise distance ≥ 2. The minimum total weight is 2n (each vector has weight exactly 2). Can we find n weight-2 vectors of length n with pairwise distance ≥ 2? Two weight-2 vectors have distance 2 if they share exactly one element, distance 4 if they share none, distance 0 if identical. So we need them to be distinct and not share exactly one element. So they either share 0 or 2 elements (but sharing 2 means identical). So they must share 0 elements: pairwise disjoint pairs.

But n pairwise disjoint 2-element subsets of [n] require 2n ≤ n, i.e., n ≤ 0. Impossible for n ≥ 1.

So we can't have all weight-2 vectors pairwise disjoint. We need some vectors to share 0 elements (distance 4) — wait, distance 2 is fine as long as it's not distance 1. Two weight-2 vectors sharing 1 element have distance 2, which is ≥ 2. So that's fine!

Wait, I was confused. Distance ≥ 2 means distance 2, 3, 4, etc. Two weight-2 vectors sharing 1 element have Hamming distance 2 (each has one element the other doesn't). That's ≥ 2, so it's fine!

So we just need the weight-2 vectors to be distinct (no two identical). There are C(n,2) weight-2 vectors, and we need n of them. For n ≥ 2, C(n,2) ≥ n iff n(n-1)/2 ≥ n iff n-1 ≥ 2 iff n ≥ 3. For n = 2, C(2,2) = 1 < 2, so we can't use 2 distinct weight-2 vectors. But for n ≥ 3, we can.

Wait, for n=2: we need 2 row vectors of length 2, weight ≥ 2, pairwise distance ≥ 2. Weight-2 vectors of length 2: only {1,2} = (1,1). So only one such vector. Can't have 2 distinct ones. So we'd need higher weight, but max weight is 2 for length 2. So approach 1 fails for n=2.

For n=2, we already know P(2) = 3. Let me check: with 3 pebbles, the matrix is e.g. [[1,1],[1,0]]. Row types: (1,1) and (1,0), distance 1. That violates condition (A) or (B)! 

Wait, but P(2) = 3 works. Let me recheck. The pebble placement (1,1),(1,2),(2,1) gives matrix [[1,1],[1,0]]. Row types: R_1 = {1,2}, R_2 = {1}. Distance = |{2}| = 1. So condition (B) for column j=1: R_1 \ {1} = {2}, R_2 \ {1} = {}. These are different, so (B) is satisfied for j=1. For j=2: R_1 \ {2} = {1}, R_2 \ {2} = {1}. These are the same! So condition (B) is violated for j=2.

But we said P(2) = 3 works. Let me recheck the pebble sets.
Matrix [[1,1],[1,0]]:
- S(1,1) = row1 ∪ col1 = {(1,1),(1,2)} ∪ {(1,1),(2,1)} = {(1,1),(1,2),(2,1)}
- S(1,2) = row1 ∪ col2 = {(1,1),(1,2)} ∪ {(1,2)} = {(1,1),(1,2)}
- S(2,1) = row2 ∪ col1 = {(2,1)} ∪ {(1,1),(2,1)} = {(1,1),(2,1)}
- S(2,2) = row2 ∪ col2 = {(2,1)} ∪ {(1,2)} = {(1,2),(2,1)}

All four are distinct. So it works. But condition (B) for j=2 says R_1 \ {2} = R_2 \ {2} = {1}, which means S(1,2) should equal S(2,2)? Let me check: S(1,2) = {(1,1),(1,2)}, S(2,2) = {(1,2),(2,1)}. These are different!

I think my condition (B) was wrong. Let me re-derive.

For same column j, different rows i, i': S(i,j) = S(i',j) iff row_i \ col_j = row_{i'} \ col_j (as edge sets). The edges in row i not in column j are {(i,l) : l ∈ R_i, l ≠ j}. The edges in row i' not in column j are {(i',l) : l ∈ R_{i'}, l ≠ j}. These are always different because they're in different rows (i ≠ i')! 

Oh wait, I see my error. The edges in S(i,j) that are in row i but not column j are {(i,l) : l ∈ R_i, l ≠ j}. The edges in S(i',j) that are in row i' but not column j are {(i',l) : l ∈ R_{i'}, l ≠ j}. Since i ≠ i', these are edges in different rows, so they're automatically different sets (an edge (i,l) is never equal to (i',l')). 

So S(i,j) = S(i',j) (same column, different rows) iff:
- The row-i-only edges = the row-i'-only edges: impossible since they're in different rows, UNLESS both are empty.
- Both must be empty: R_i \ {j} = {} and R_{i'} \ {j} = {}, i.e., R_i ⊆ {j} and R_{i'} ⊆ {j}.
- And the column j edges are the same (trivially, since it's the same column).

So S(i,j) = S(i',j) iff R_i ⊆ {j} and R_{i'} ⊆ {j}. This means both rows i and i' have pebbles only in column j (at most 1 pebble each, at column j).

Similarly, S(i,j) = S(i,j') (same row, different columns) iff C_j ⊆ {i} and C_{j'} ⊆ {i}.

And S(i,j) = S(i',j') (different row and column) iff the cross-pattern condition holds (as before).

So my earlier conditions (A) and (B) were WRONG. Let me redo.

Condition for all S(i,j) distinct:
- Same row, different columns: S(i,j) ≠ S(i,j') for j≠j' iff NOT (C_j ⊆ {i} and C_{j'} ⊆ {i}). So for each row i, at most one column j has C_j ⊆ {i}.
- Same column, different rows: S(i,j) ≠ S(i',j) for i≠i' iff NOT (R_i ⊆ {j} and R_{i'} ⊆ {j}). So for each column j, at most one row i has R_i ⊆ {j}.
- Different row and column: S(i,j) ≠ S(i',j') for i≠i', j≠j' iff NOT (cross-pattern condition).

Let me re-examine the cross-pattern condition. S(i,j) = S(i',j') with i≠i', j≠j':
- Edges in S(i,j) = row i ∪ col j. Edges in S(i',j') = row i' ∪ col j'.
- An edge (a,b) in S(i,j) has a=i or b=j. An edge (a,b) in S(i',j') has a=i' or b=j'.
- For equality, every edge in S(i,j) must be in S(i',j') and vice versa.
- Edge (i, l) with l ≠ j: in S(i,j) (row i). In S(i',j')? Need i=i' (no) or l=j' (yes if l=j'). So for l ≠ j, j', edge (i,l) is in S(i,j) but not S(i',j'). So no such edge: R_i ⊆ {j, j'} and specifically no pebble at (i,l) for l ∉ {j,j'}.
- Similarly, edge (i', l) with l ≠ j': in S(i',j') but not S(i,j) unless l=j. So R_{i'} ⊆ {j, j'}.
- Edge (k, j) with k ≠ i: in S(i,j) (col j). In S(i',j')? Need k=i' (yes if k=i') or j=j' (no). So for k ≠ i, i', edge (k,j) is in S(i,j) but not S(i',j'). So C_j ⊆ {i, i'}.
- Similarly, C_{j'} ⊆ {i, i'}.
- Edge (i, j): in S(i,j). In S(i',j')? Need i=i' (no) or j=j' (no). So edge (i,j) NOT in S(i',j'). So no pebble at (i,j).
- Edge (i', j'): in S(i',j') but not S(i,j). So no pebble at (i',j').
- Edge (i, j'): in S(i,j) (row i) and in S(i',j') (col j'). In both. OK.
- Edge (i', j): in S(i,j) (col j) and in S(i',j') (row i'). In both. OK.

So the conditions are:
- R_i ⊆ {j, j'}, R_{i'} ⊆ {j, j'}, C_j ⊆ {i, i'}, C_{j'} ⊆ {i, i'}
- No pebble at (i,j) or (i',j')
- Since R_i ⊆ {j, j'} and no pebble at (i,j): R_i ⊆ {j'}
- Since R_{i'} ⊆ {j, j'} and no pebble at (i',j'): R_{i'} ⊆ {j}
- Since C_j ⊆ {i, i'} and no pebble at (i,j): C_j ⊆ {i'}
- Since C_{j'} ⊆ {i, i'} and no pebble at (i',j'): C_{j'} ⊆ {i}

So: R_i ⊆ {j'}, R_{i'} ⊆ {j}, C_j ⊆ {i'}, C_{j'} ⊆ {i}. Same as before.

And the pebble sets are: S(i,j) = {(i,j') if pebble} ∪ {(i',j) if pebble} = S(i',j'). So they're always equal when these conditions hold.

So the conditions for all pebble sets distinct are:
(1) For each row i, at most one column j has C_j ⊆ {i} (i.e., column j has pebbles only in row i).
(2) For each column j, at most one row i has R_i ⊆ {j} (i.e., row i has pebbles only in column j).
(3) No cross-pattern: for no i≠i', j≠j' do we have R_i ⊆ {j'}, R_{i'} ⊆ {j}, C_j ⊆ {i'}, C_{j'} ⊆ {i}.

Now, R_i ⊆ {j'} means row i has at most 1 pebble (at column j'). If row i has 0 pebbles, R_i = {} ⊆ {j'} for any j'. If row i has 1 pebble at column j', then R_i = {j'} ⊆ {j'}.

Similarly, C_j ⊆ {i'} means column j has at most 1 pebble (at row i').

So condition (3) says: there don't exist two rows i, i' each with ≤ 1 pebble, and two columns j, j' each with ≤ 1 pebble, such that:
- If row i has 1 pebble, it's at column j'; if 0 pebbles, any j' works.
- If row i' has 1 pebble, it's at column j; if 0 pebbles, any j works.
- If column j has 1 pebble, it's at row i'; if 0 pebbles, any i' works.
- If column j' has 1 pebble, it's at row i; if 0 pebbles, any i works.
- No pebble at (i,j) and (i',j').

This is complex. Let me think about when condition (3) can be avoided.

Simple sufficient condition: All rows have ≥ 2 pebbles. Then R_i ⊆ {j'} is impossible, so (3) never triggers. Cost: ≥ 2n pebbles.

Another: All columns have ≥ 2 pebbles. Cost: ≥ 2n.

Another: At most one row has ≤ 1 pebble. Then we can't find two such rows, so (3) never triggers. Cost: ≥ 2(n-1) pebbles (n-1 rows with ≥ 2 pebbles, 1 row with 0).

Similarly: At most one column has ≤ 1 pebble. Cost: ≥ 2(n-1).

But maybe we can do better by being more careful about condition (3).

Let me think about what configurations with some sparse rows/columns can avoid (3).

Suppose we have k rows with ≤ 1 pebble and l columns with ≤ 1 pebble. Condition (3) requires k ≥ 2 and l ≥ 2 to even have a chance of triggering. If k ≤ 1 or l ≤ 1, (3) is automatically avoided.

If k ≥ 2 and l ≥ 2, we need to check if the cross-pattern actually occurs. The sparse rows have their single pebble (if any) at specific columns, and the sparse columns have their single pebble (if any) at specific rows.

Let me think about this more carefully. Let's say the sparse rows (≤ 1 pebble) are rows i_1, ..., i_k, and sparse columns are j_1, ..., j_l. For condition (3) to trigger, we need two sparse rows i, i' and two sparse columns j, j' with:
- Row i's pebble (if any) is at column j' (so j' is the column of row i's pebble, or row i has 0 pebbles).
- Row i's pebble (if any) is NOT at column j (no pebble at (i,j)).
- Row i''s pebble (if any) is at column j.
- Row i''s pebble (if any) is NOT at column j'.
- Column j's pebble (if any) is at row i'.
- Column j's pebble (if any) is NOT at row i.
- Column j''s pebble (if any) is at row i.
- Column j''s pebble (if any) is NOT at row i'.

This is a very specific matching condition. If the sparse rows' pebbles and sparse columns' pebbles don't form this cross pattern, (3) is avoided.

This is getting quite complex. Let me try a different approach and think about the problem from the competition math perspective.

Let me reconsider. The answer P(2021) is likely a nice expression. Let me think about what it could be.

Let me compute P(n) for small n more carefully.

P(1) = 0.
P(2) = 3.

Let me try P(3).

We need 9 distinct pebble sets on a 3×3 board.

Let me try to find a configuration with few pebbles.

Try 4 pebbles: We need conditions (1), (2), (3) satisfied.

With 4 pebbles on 3×3, the average row weight is 4/3, so at least 2 rows have ≤ 1 pebble (by pigeonhole, if 2 rows have ≥ 2 pebbles, that's ≥ 4, so the third has 0). Actually, if 2 rows have 2 pebbles each (4 total), the third has 0. So k ≥ 1 (at least one row with 0 pebbles). Similarly for columns.

With 4 pebbles: could have row weights (2,2,0) or (2,1,1) or (3,1,0) or (4,0,0) etc.

Let me try row weights (2,1,1) and column weights (2,1,1). 

Example: pebbles at (1,1),(1,2),(2,3),(3,3). Row weights: 2,1,1. Column weights: 1,1,2.
R_1 = {1,2}, R_2 = {3}, R_3 = {3}.
C_1 = {1}, C_2 = {1}, C_3 = {2,3}.

Check condition (1): For each row i, at most one column j has C_j ⊆ {i}.
- Row 1: C_1 = {1} ⊆ {1} ✓, C_2 = {1} ⊆ {1} ✓. Two columns have C_j ⊆ {1}. Violation!

So S(1,1) and S(1,2) might be equal. Let me check:
S(1,1) = row1 ∪ col1 = {(1,1),(1,2)} ∪ {(1,1)} = {(1,1),(1,2)}
S(1,2) = row1 ∪ col2 = {(1,1),(1,2)} ∪ {(1,2)} = {(1,1),(1,2)}
Yes, equal. Violation.

The issue is columns 1 and 2 both have pebbles only in row 1. So S(1,1) = S(1,2).

To fix: columns 1 and 2 should not both have pebbles only in the same single row.

Let me try: pebbles at (1,1),(1,2),(2,1),(3,3). Row weights: 2,1,1. Column weights: 2,1,1.
R_1 = {1,2}, R_2 = {1}, R_3 = {3}.
C_1 = {1,2}, C_2 = {1}, C_3 = {3}.

Check (1): For each row i, at most one column j has C_j ⊆ {i}.
- Row 1: C_2 = {1} ⊆ {1} ✓. C_1 = {1,2} ⊄ {1}. C_3 = {3} ⊄ {1}. Only one. OK.
- Row 2: C_3 = {3} ⊄ {2}. C_2 = {1} ⊄ {2}. C_1 = {1,2} ⊄ {2}. None. OK.
- Row 3: C_3 = {3} ⊆ {3} ✓. C_2 = {1} ⊄ {3}. C_1 = {1,2} ⊄ {3}. Only one. OK.

Check (2): For each column j, at most one row i has R_i ⊆ {j}.
- Col 1: R_2 = {1} ⊆ {1} ✓. R_3 = {3} ⊄ {1}. R_1 = {1,2} ⊄ {1}. Only one. OK.
- Col 2: R_1 = {1,2} ⊄ {2}. R_2 = {1} ⊄ {2}. R_3 = {3} ⊄ {2}. None. OK.
- Col 3: R_3 = {3} ⊆ {3} ✓. R_2 = {1} ⊄ {3}. R_1 = {1,2} ⊄ {3}. Only one. OK.

Check (3): Cross-pattern. Sparse rows (≤ 1 pebble): rows 2 (R_2 = {1}) and 3 (R_3 = {3}). Sparse columns (≤ 1 pebble): col 2 (C_2 = {1}) and col 3 (C_3 = {3}).

We need i, i' from {2, 3} and j, j' from {2, 3} with i≠i', j≠j', and:
- R_i ⊆ {j'}, R_{i'} ⊆ {j}, C_j ⊆ {i'}, C_{j'} ⊆ {i}, no pebble at (i,j) or (i',j').

Case: i=2, i'=3, j=2, j'=3:
- R_2 = {1} ⊆ {3}? No. Fails.

Case: i=2, i'=3, j=3, j'=2:
- R_2 = {1} ⊆ {2}? No. Fails.

Case: i=3, i'=2, j=2, j'=3:
- R_3 = {3} ⊆ {3}? Yes. R_2 = {1} ⊆ {2}? No. Fails.

Case: i=3, i'=2, j=3, j'=2:
- R_3 = {3} ⊆ {2}? No. Fails.

So condition (3) is satisfied! Let me verify all 9 pebble sets are distinct.

Pebbles: (1,1),(1,2),(2,1),(3,3).
R_1 = {1,2}, R_2 = {1}, R_3 = {3}.
C_1 = {1,2}, C_2 = {1}, C_3 = {3}.

S(1,1) = {(1,1),(1,2)} ∪ {(1,1),(2,1)} = {(1,1),(1,2),(2,1)}
S(1,2) = {(1,1),(1,2)} ∪ {(1,2)} = {(1,1),(1,2)}
S(1,3) = {(1,1),(1,2)} ∪ {(3,3)} = {(1,1),(1,2),(3,3)}
S(2,1) = {(2,1)} ∪ {(1,1),(2,1)} = {(1,1),(2,1)}
S(2,2) = {(2,1)} ∪ {(1,2)} = {(1,2),(2,1)}
S(2,3) = {(2,1)} ∪ {(3,3)} = {(2,1),(3,3)}
S(3,1) = {(3,3)} ∪ {(1,1),(2,1)} = {(1,1),(2,1),(3,3)}
S(3,2) = {(3,3)} ∪ {(1,2)} = {(1,2),(3,3)}
S(3,3) = {(3,3)} ∪ {(3,3)} = {(3,3)}

All 9 are distinct! So P(3) ≤ 4.

Can P(3) = 3? With 3 pebbles on 3×3, we'd have average row weight 1. Let me check if 3 pebbles can work.

With 3 pebbles, row weights sum to 3. Possible: (1,1,1), (2,1,0), (3,0,0).

Case (1,1,1): Each row has exactly 1 pebble. Each column has at most 1 pebble (since 3 pebbles in 3 rows with 1 each, columns could have 0,1,2,3). 

If each row has 1 pebble, then for condition (2): for each column j, at most one row i has R_i ⊆ {j}. R_i is a singleton {c_i} where c_i is the column of row i's pebble. R_i ⊆ {j} iff c_i = j. So for each column j, at most one row has its pebble in column j. This means all pebbles are in distinct columns. So the pebbles form a permutation matrix.

With a permutation matrix (3 pebbles), check condition (3): all rows have exactly 1 pebble, all columns have exactly 1 pebble. So k = 3 ≥ 2 and l = 3 ≥ 2. We need to check if the cross-pattern triggers.

For a permutation matrix with pebbles at (i, π(i)):
R_i = {π(i)}, C_j = {π^{-1}(j)}.

Cross-pattern for (i,j), (i',j') with i≠i', j≠j':
- R_i = {π(i)} ⊆ {j'}: π(i) = j'.
- R_{i'} = {π(i')} ⊆ {j}: π(i') = j.
- C_j = {π^{-1}(j)} ⊆ {i'}: π^{-1}(j) = i', i.e., π(i') = j. (Same as above.)
- C_{j'} = {π^{-1}(j')} ⊆ {i}: π^{-1}(j') = i, i.e., π(i) = j'. (Same as above.)
- No pebble at (i,j): π(i) ≠ j, i.e., j' ≠ j. (Already given.)
- No pebble at (i',j'): π(i') ≠ j', i.e., j ≠ j'. (Already given.)

So the cross-pattern triggers for any i≠i' with j = π(i') and j' = π(i). This gives S(i, π(i')) = S(i', π(i)).

S(i, π(i')) = {(i, π(i))} ∪ {(π^{-1}(π(i')), π(i'))} = {(i, π(i)), (i', π(i'))}.
S(i', π(i)) = {(i', π(i'))} ∪ {(π^{-1}(π(i)), π(i))} = {(i', π(i')), (i, π(i))}.
Same! So condition (3) is violated for any permutation matrix with n ≥ 2.

So 3 pebbles with row weights (1,1,1) (permutation matrix) doesn't work.

Case (2,1,0): One row has 2 pebbles, one has 1, one has 0. Let me try.
Pebbles at (1,1),(1,2),(2,3). R_1={1,2}, R_2={3}, R_3={}. C_1={1}, C_2={1}, C_3={2}.

Check (1): For each row i, at most one column j has C_j ⊆ {i}.
- Row 1: C_1={1}⊆{1}✓, C_2={1}⊆{1}✓. Two! Violation.

S(1,1) = {(1,1),(1,2)} ∪ {(1,1)} = {(1,1),(1,2)}
S(1,2) = {(1,1),(1,2)} ∪ {(1,2)} = {(1,1),(1,2)}
Equal. Violation.

Try pebbles at (1,1),(1,2),(2,1). R_1={1,2}, R_2={1}, R_3={}. C_1={1,2}, C_2={1}, C_3={}.
Check (1): 
- Row 1: C_2={1}⊆{1}✓, C_3={}⊆{1}✓. Two! Violation.

S(1,2) = {(1,1),(1,2)} ∪ {(1,2)} = {(1,1),(1,2)}
S(1,3) = {(1,1),(1,2)} ∪ {} = {(1,1),(1,2)}
Equal. Violation.

The issue with row 3 having 0 pebbles: C_j ⊆ {i} is satisfied for any column j with C_j = {} or C_j = {i}. If row i has pebbles, columns with pebbles only in row i and empty columns both satisfy C_j ⊆ {i}. So if there's an empty column and a column with pebbles only in row i, that's already 2 columns with C_j ⊆ {i}.

With 3 pebbles and 3 columns, if one column is empty, and another column has pebbles only in one row, that's a problem.

Let me try to avoid empty columns. With 3 pebbles in 3 columns, each column has exactly 1 pebble. Then C_j is a singleton for each j. 

Pebbles at (1,1),(1,2),(2,3): C_1={1}, C_2={1}, C_3={2}. 
Check (1): Row 1: C_1⊆{1}, C_2⊆{1}. Two! Violation.

Pebbles at (1,1),(2,2),(2,3): C_1={1}, C_2={2}, C_3={2}.
Check (1): Row 2: C_2⊆{2}, C_3⊆{2}. Two! Violation.

It seems like with 3 pebbles, we always get a violation. Let me think about why.

With 3 pebbles on 3×3, by pigeonhole, some row has ≤ 1 pebble. If a row has 0 pebbles, then for that row i, C_j ⊆ {i} = {} means C_j = {}. So only empty columns satisfy C_j ⊆ {i}. If there are ≥ 2 empty columns, violation. With 3 pebbles in 3 columns, at most 3 columns are non-empty, so 0 empty columns if all columns have pebbles. But if a row has 0 pebbles, C_j ⊆ {} means C_j = {}, so we need at most 1 empty column.

With 3 pebbles, if all 3 columns are non-empty, no empty columns, so the 0-pebble row is fine for condition (1). But then we need to check other conditions.

Let me try: pebbles at (1,1),(2,2),(3,3) (identity). We already know this fails (cross-pattern).

Pebbles at (1,1),(2,2),(2,3): R_1={1}, R_2={2,3}, R_3={}. C_1={1}, C_2={2}, C_3={2}.
Check (1): 
- Row 1: C_1={1}⊆{1}✓. C_2={2}⊄{1}. C_3={2}⊄{1}. One. OK.
- Row 2: C_2={2}⊆{2}✓, C_3={2}⊆{2}✓. Two! Violation.

S(2,2) = {(2,2),(2,3)} ∪ {(2,2)} = {(2,2),(2,3)}
S(2,3) = {(2,2),(2,3)} ∪ {(2,3)} = {(2,2),(2,3)}
Equal. Violation.

Pebbles at (1,1),(2,2),(3,1): R_1={1}, R_2={2}, R_3={1}. C_1={1,3}, C_2={2}, C_3={}.
Check (1):
- Row 1: C_3={}⊆{1}✓. C_2={2}⊄{1}. C_1={1,3}⊄{1}. One. OK.
- Row 2: C_2={2}⊆{2}✓. C_3={}⊆{2}✓. Two! Violation.

S(2,2) = {(2,2)} ∪ {(2,2)} = {(2,2)}
S(2,3) = {(2,2)} ∪ {} = {(2,2)}
Equal. Violation.

The problem is that with 3 pebbles, we always have some row with 0 pebbles (if row weights are (2,1,0)) or all rows with 1 pebble (permutation matrix, which has cross-pattern issues), or (3,0,0) which is even worse.

With (2,1,0): the row with 0 pebbles causes issues because empty columns satisfy C_j ⊆ {i} for that row. With 3 pebbles in 3 columns, if all columns are non-empty, no empty columns, so the 0-pebble row is fine. But then the 1-pebble row: the column with its pebble has C_j containing that row, and if C_j is a singleton {i}, then C_j ⊆ {i}. We need at most one such column. But if the 2-pebble row has both pebbles in the same column... no, 2 pebbles in 2 different columns. 

Hmm, let me try more carefully. With row weights (2,1,0) and all 3 columns non-empty:
- Row 1 has 2 pebbles in 2 columns, say cols a, b.
- Row 2 has 1 pebble in col c.
- Row 3 has 0 pebbles.
- All columns non-empty: cols a, b, c must cover all 3 columns. So {a,b,c} = {1,2,3} (if a≠b and c is the third). Or c ∈ {a,b} and the third column is empty — but we need all non-empty. So c must be the third column, and a, b are the other two.

So: pebbles at (1,a),(1,b),(2,c) where {a,b,c} = {1,2,3}.
C_a = {1}, C_b = {1}, C_c = {2}.

Check (1) for row 1: C_a = {1} ⊆ {1} ✓, C_b = {1} ⊆ {1} ✓. Two! Violation.

So columns a and b both have pebbles only in row 1, causing S(1,a) = S(1,b). This always happens with this structure.

What if the 2 pebbles in row 1 are in the same column? No, each square has at most 1 pebble, so 2 pebbles in row 1 are in 2 different columns.

What if we don't require all columns non-empty? Then there's an empty column, and the 0-pebble row has ≥ 1 empty column with C_j = {} ⊆ {i}. If there's also a column with C_j = {i'} for some other row i', that's fine for the 0-pebble row (since {i'} ⊄ {i} when i' ≠ i). But we also need to check other rows.

This is getting complicated. Let me just check: is P(3) = 4?

We showed P(3) ≤ 4. Let me check if P(3) = 3 is impossible.

With 3 pebbles, the possible row weight distributions are (3,0,0), (2,1,0), (1,1,1).

(3,0,0): One row has all 3 pebbles. Columns each have 1 pebble, all in the same row. C_j = {1} for all j. Condition (1) for row 1: all 3 columns have C_j ⊆ {1}. Violation (3 > 1).

(2,1,0): As shown above, always has a violation.

(1,1,1): Permutation matrix, cross-pattern violation.

So P(3) = 4.

Now let me see the pattern: P(1) = 0, P(2) = 3, P(3) = 4.

Let me compute P(4).

Hmm, this is getting tedious. Let me think about the general pattern.

From the analysis, the key conditions are:
(1) For each row i, at most one column j has C_j ⊆ {i}.
(2) For each column j, at most one row i has R_i ⊆ {j}.
(3) No cross-pattern.

Let me think about what kind of matrix satisfies these with minimum weight.

Key insight: Condition (1) says that for each row i, the number of columns whose pebbles are all in row i (i.e., columns that only "touch" row i) is at most 1. A column "only touches" row i if all its pebbles are in row i, i.e., C_j ⊆ {i}, i.e., C_j = {} or C_j = {i}.

So for each row i, at most one column is either empty or has pebbles only in row i.

Similarly, condition (2): for each column j, at most one row is either empty or has pebbles only in column j.

Let me think about the number of empty rows and columns.

If there are e_r empty rows and e_c empty columns:
- For an empty row i (R_i = {}), condition (2) for each column j: R_i = {} ⊆ {j} is always true. So for each column j, the empty row counts toward the "at most one" limit. If there are ≥ 2 empty rows, then for every column j, we have ≥ 2 rows with R_i ⊆ {j}, violating (2). So e_r ≤ 1.
- Similarly, e_c ≤ 1.

So at most 1 empty row and at most 1 empty column.

Now, let's think about rows with exactly 1 pebble. If row i has 1 pebble at column j, then R_i = {j} ⊆ {j}. For condition (2), column j has this row counting toward its limit. If two rows both have their single pebble in the same column j, then column j has ≥ 2 rows with R_i ⊆ {j}, violating (2). So all single-pebble rows have their pebbles in distinct columns.

Similarly, all single-pebble columns have their pebbles in distinct rows.

Let me denote:
- a = number of empty rows (0 or 1)
- b = number of single-pebble rows
- c = number of rows with ≥ 2 pebbles
- a + b + c = n

Similarly for columns:
- a' = number of empty columns (0 or 1)
- b' = number of single-pebble columns
- c' = number of columns with ≥ 2 pebbles
- a' + b' + c' = n

Total pebbles = b + (sum of degrees of rows with ≥ 2 pebbles) ≥ b + 2c = b + 2(n - a - b) = 2n - 2a - b.
Also = b' + 2c' = 2n - 2a' - b'.

To minimize, we want to maximize a, b, a', b'. But there are constraints.

Constraints from conditions (1) and (2):

Condition (2): For each column j, at most one row i has R_i ⊆ {j}. The rows with R_i ⊆ {j} are: the empty row (if a=1, R = {} ⊆ {j} for all j), and rows with single pebble at column j. So for column j: (1 if a=1 else 0) + (number of single-pebble rows with pebble at column j) ≤ 1.

If a = 1: for each column j, the number of single-pebble rows with pebble at column j must be 0. So no single-pebble rows at all! b = 0. (Because the empty row already uses up the quota for every column.)

Wait, that's not right. The empty row has R = {} ⊆ {j} for every j. So for every column j, the empty row counts as 1. So the quota is used up, and no single-pebble row can have its pebble at any column. So b = 0.

If a = 0: for each column j, at most one single-pebble row has its pebble at column j. So the single-pebble rows have pebbles at distinct columns. b ≤ n (and specifically, b ≤ n - a' since empty columns can't have pebbles... wait, actually a single-pebble row has its pebble at some column, which must be non-empty. So b ≤ n - a'.)

Similarly, condition (1): 
If a' = 1: b' = 0 (no single-pebble columns).
If a' = 0: b' ≤ n (single-pebble columns have pebbles at distinct rows, so b' ≤ n - a).

Now let's consider cases:

Case 1: a = 1, a' = 1 (one empty row, one empty column).
Then b = 0, b' = 0. All non-empty rows have ≥ 2 pebbles, all non-empty columns have ≥ 2 pebbles.
c = n - 1, c' = n - 1.
Total pebbles ≥ 2(n-1) and ≥ 2(n-1). So ≥ 2(n-1).

But we also need condition (3). With a = 1 (one empty row) and a' = 1 (one empty column), the sparse rows are the empty row (R = {}) and any single-pebble rows (but b = 0, so no single-pebble rows). So only 1 sparse row. Condition (3) needs ≥ 2 sparse rows, so (3) is automatically satisfied.

So in this case, we need ≥ 2(n-1) pebbles, and we need to find a matrix with exactly 2(n-1) pebbles where all non-empty rows have exactly 2 pebbles, all non-empty columns have exactly 2 pebbles, and conditions (1) and (2) are satisfied.

With 2(n-1) pebbles, n-1 rows with 2 pebbles each, n-1 columns with 2 pebbles each, and 1 empty row, 1 empty column. This is a 2-regular bipartite graph on (n-1) + (n-1) vertices, which is a union of cycles. 

We need conditions (1) and (2) to hold. Condition (1) with a' = 1: for each row i, at most one column j has C_j ⊆ {i}. The empty column has C = {} ⊆ {i} for all i. So the empty column uses up the quota for every row. So no other column can have C_j ⊆ {i} for any row i. Since all non-empty columns have 2 pebbles, C_j has 2 elements, so C_j ⊆ {i} only if both pebbles are in row i, but |C_j| = 2 > 1 = |{i}|, impossible. So condition (1) is automatically satisfied.

Condition (2) with a = 1: similarly, the empty row uses up the quota for every column. No non-empty row has R_i ⊆ {j} since |R_i| = 2 > 1. So condition (2) is automatically satisfied.

So in Case 1, we just need a 2-regular bipartite graph on (n-1)+(n-1) vertices, which exists for n ≥ 3 (e.g., a single cycle of length 2(n-1)). Total pebbles = 2(n-1).

For n = 3: 2(3-1) = 4. Matches P(3) = 4!
For n = 2: 2(2-1) = 2. But P(2) = 3. So this doesn't work for n = 2. The issue is that for n = 2, a 2-regular bipartite graph on 1+1 vertices is a single edge (cycle of length 2), which has 2 pebbles. But we need to check: with 1 empty row and 1 empty column, the non-empty part is 1×1 with 2 pebbles... wait, 2-regular on 1+1 vertices means each vertex has degree 2, but there's only 1 vertex on each side, so we need 2 edges between them, which means 2 pebbles at the same position. But each square has at most 1 pebble! So this is impossible for n = 2.

For n = 2, we can't have a 2-regular bipartite graph on 1+1 vertices with at most 1 edge between any pair. So Case 1 doesn't work for n = 2.

For n ≥ 3, a cycle of length 2(n-1) in the bipartite graph on (n-1)+(n-1) vertices works. Each vertex has degree 2, and it's a simple graph (no multi-edges). This gives 2(n-1) pebbles.

But can we do better than 2(n-1)? Let's check other cases.

Case 2: a = 1, a' = 0 (one empty row, no empty columns).
Then b = 0 (from a = 1). b' ≤ n - a = n - 1 (single-pebble columns have pebbles at distinct non-empty rows).
Total pebbles ≥ 2(n-1) (from rows: b + 2c = 0 + 2(n-1) = 2(n-1)).
Also = b' + 2c' = b' + 2(n - b') = 2n - b'. To minimize, maximize b'. b' ≤ n - 1.
If b' = n - 1: total = 2n - (n-1) = n + 1. And from rows, total = 2(n-1) = 2n - 2. So n + 1 ≥ 2n - 2 iff n ≤ 3. For n = 3: n + 1 = 4 = 2n - 2. For n > 3: n + 1 < 2n - 2, so the binding constraint is from rows: 2(n-1).

Wait, I need to be more careful. Total pebbles = sum of row degrees = sum of column degrees. From rows: total = 0 (empty row) + 0 (b=0, no single-pebble rows) + sum of degrees of c = n-1 rows with ≥ 2 pebbles = ≥ 2(n-1). From columns: total = b' (single-pebble columns) + 2*c' (columns with ≥ 2 pebbles) ≥ b' + 2(n - b') = 2n - b'. 

So total ≥ max(2(n-1), 2n - b'). To minimize total, we want to minimize max(2(n-1), 2n - b'). Since b' ≤ n-1, 2n - b' ≥ 2n - (n-1) = n + 1. So total ≥ max(2n - 2, n + 1). For n ≥ 3, 2n - 2 ≥ n + 1 iff n ≥ 3. So for n ≥ 3, total ≥ 2(n-1), same as Case 1.

For n = 2: max(2, 3) = 3. So total ≥ 3. And we know P(2) = 3. So Case 2 gives P(2) = 3!

Let me verify: n = 2, a = 1 (one empty row), a' = 0 (no empty columns), b = 0, b' ≤ 1. Total ≥ 3. Can we achieve 3?

Row weights: 0, 2 (since b = 0, c = 1, a = 1). Wait, n = 2, a = 1, b = 0, c = 1. Row 1 has 2 pebbles, row 2 is empty. But 2 pebbles in a 2-column row means both columns. Column weights: each column has 1 pebble (from row 1). So b' = 2, c' = 0. But b' ≤ n - a = 2 - 1 = 1. So b' = 2 > 1. Violation!

Hmm, so the constraint b' ≤ n - a is violated. Let me recheck. b' is the number of single-pebble columns. These columns have their single pebble at some row, and by condition (1), for each row i, at most one column has C_j ⊆ {i}. With a = 1 (empty row), the empty row has no pebbles, so C_j ⊆ {} means C_j = {}. But a' = 0 (no empty columns), so no C_j = {}. So the empty row doesn't consume any quota. For non-empty rows (just row 1), at most one column has C_j ⊆ {1}. C_j = {1} (single pebble in row 1) satisfies this. So at most 1 column has C_j = {1}. So b' ≤ 1 (at most 1 single-pebble column with pebble in row 1).

But we have 2 pebbles in row 1 (columns 1 and 2), so both columns have C_j = {1}. That's 2 > 1. Violation of condition (1)!

So this doesn't work. We need row 1 to have 2 pebbles but only 1 column can have C_j = {1}. The other column must have C_j with ≥ 2 elements, but there are only 2 rows and row 2 is empty. So C_j ⊆ {1} for any non-empty column. So both columns have C_j ⊆ {1}, violation.

So Case 2 with a = 1 doesn't work for n = 2 with 2 pebbles in the non-empty row. We need the non-empty row to have more pebbles or a different structure.

Actually, for n = 2 with a = 1, we have 1 non-empty row with ≥ 2 pebbles, but only 2 columns. Both columns will have pebbles only in row 1 (since row 2 is empty), so C_j ⊆ {1} for both. Condition (1) allows at most 1. So we need one column to be empty (a' = 1), but we assumed a' = 0. Contradiction. So Case 2 is impossible for n = 2.

OK so for n = 2, the optimal is Case 2 with a = 0, a' = 0 (no empty rows or columns).

Case 3: a = 0, a' = 0 (no empty rows or columns).
b ≤ n (single-pebble rows with pebbles at distinct columns, but since a' = 0, all columns are non-empty, so b ≤ n). Actually, b ≤ n - a' = n. And the single-pebble rows have pebbles at distinct columns (condition (2)), so b ≤ n. Also, b' ≤ n (condition (1), single-pebble columns at distinct rows).

Total pebbles = b + (sum of degrees of rows with ≥ 2 pebbles) ≥ b + 2(n - b) = 2n - b.
Also = b' + 2(n - b') = 2n - b'.
So total ≥ max(2n - b, 2n - b'). To minimize, maximize b and b'. b ≤ n, b' ≤ n.

If b = n: all rows have exactly 1 pebble. Then total = n. But b' = ? Each column has some pebbles. If all rows have 1 pebble at distinct columns (permutation matrix), then b' = n (all columns have 1 pebble). Total = n. But we need condition (3) to hold. As shown, permutation matrices violate (3) for n ≥ 2.

So b = n doesn't work (for n ≥ 2) due to condition (3).

What about b = n - 1? One row has ≥ 2 pebbles, n-1 rows have 1 pebble each. Total ≥ 2n - (n-1) = n + 1.

For condition (3): we have n - 1 single-pebble rows and 1 multi-pebble row. The sparse rows (≤ 1 pebble) are the n - 1 single-pebble rows. For condition (3), we need ≥ 2 sparse rows and ≥ 2 sparse columns. If b' ≥ 2, we might have issues.

Let me think about this more carefully. With b = n - 1 single-pebble rows (pebbles at distinct columns) and 1 row with ≥ 2 pebbles:

The single-pebble rows have pebbles at n - 1 distinct columns. The multi-pebble row has pebbles at some columns. The columns not used by single-pebble rows: at most 1 column (since n - 1 single-pebble rows use n - 1 distinct columns out of n). 

Let's say the multi-pebble row is row n, and it has pebbles at columns including the one not used by single-pebble rows. 

Column weights: n - 1 columns have 1 pebble (from single-pebble rows) + possibly 1 more from row n. 1 column has pebbles only from row n.

If row n has 2 pebbles, one at the "unused" column and one at a "used" column:
- The unused column has C_j = {n} (only row n). This is a single-pebble column.
- The used column that row n also touches has C_j = {i, n} where i is the single-pebble row. This is a 2-pebble column.
- Other used columns have C_j = {i} (single pebble). These are single-pebble columns.

So b' = (n - 2) + 1 = n - 1 (the n - 2 other single-pebble columns plus the unused column). c' = 1 (the 2-pebble column).

Check condition (1): For each row i, at most one column j has C_j ⊆ {i}.
- For single-pebble row i (with pebble at column j_i): C_{j_i} = {i} or {i, n}. If C_{j_i} = {i} (row n doesn't touch column j_i), then C_{j_i} ⊆ {i}. Are there other columns with C_j ⊆ {i}? Only if some other column has all pebbles in row i. But other columns have pebbles from other single-pebble rows, so C_j ⊄ {i}. So at most 1. OK.
  If C_{j_i} = {i, n} (row n also touches column j_i), then C_{j_i} ⊄ {i}. Other columns with C_j ⊆ {i}? The columns with C_j = {k} for k ≠ i don't satisfy. So 0. OK.
- For row n: columns with C_j ⊆ {n}: the unused column with C_j = {n}. Any other? Only if another column has all pebbles in row n, but other columns have pebbles from single-pebble rows. So at most 1. OK.

Check condition (2): For each column j, at most one row i has R_i ⊆ {j}.
- For the unused column (C = {n}): R_n ⊆ {j}? R_n has 2 elements, so no. Single-pebble rows: R_i = {j_i} ⊆ {j} iff j_i = j. Since j is the unused column, no single-pebble row has j_i = j. So 0. OK.
- For a used column j_i (with C = {i} or {i, n}): R_i = {j_i} ⊆ {j_i}. Yes. R_n ⊆ {j_i}? R_n has 2 elements, so only if both are j_i, impossible. Other single-pebble rows: R_k = {j_k} ⊆ {j_i} iff j_k = j_i, but j_k are distinct. So exactly 1. OK.

Check condition (3): Sparse rows: n - 1 single-pebble rows. Sparse columns: n - 1 single-pebble columns. We need to check if any cross-pattern triggers.

For cross-pattern with rows i, i' (both single-pebble) and columns j, j' (both single-pebble), i ≠ i', j ≠ j':
- R_i = {j_i} ⊆ {j'}: j_i = j'.
- R_{i'} = {j_{i'}} ⊆ {j}: j_{i'} = j.
- C_j ⊆ {i'}: C_j is either {k} for some single-pebble row k, or {n} (unused column). C_j ⊆
