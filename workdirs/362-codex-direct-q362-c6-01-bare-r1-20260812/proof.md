# Proof: Volume Bound for Search with One Lie and One Silence

## Problem Statement

There is an unknown target $x$ among $N$ candidates. A questioner asks $q$ adaptive yes/no questions, each of the form "does $x$ belong to this specified subset?" The responder may:

1. Lie in **at most one** round (give the wrong yes/no answer), and
2. Be silent in **at most one** round (give the symbol $*$ instead of yes/no).

The questioner does not know when (or whether) the lie or silence occurs. After all $q$ questions, the questioner outputs at most $t$ candidates and must guarantee the true target is among them.

**Claim.** If $N(q^2 + q + 1) > t\!\left(2^q + q\,2^{q-1}\right)$, then no such guaranteed strategy exists.

---

## Setup and Definitions

### Strategies as Decision Trees

A **strategy** for the questioner is a decision tree of depth $q$. At each internal node, the questioner chooses a subset $S$ of candidates and asks "does $x \in S$?" The responder's answer is one of $Y$, $N$, or $*$. The three possible answers lead to three child nodes. At each leaf (corresponding to a complete transcript of $q$ answers), the questioner outputs a set of at most $t$ candidates.

A transcript is a sequence $\tau = (a_1, a_2, \ldots, a_q)$ where each $a_i \in \{Y, N, *\}$, with **at most one** $*$ appearing (since the responder is silent at most once).

### Configurations

A **configuration** is a pair $(\ell, s)$ specifying the responder's behavior:

- $\ell \in \{\text{none}, 1, 2, \ldots, q\}$: the round in which the lie occurs (or "none"),
- $s \in \{\text{none}, 1, 2, \ldots, q\}$: the round in which the silence occurs (or "none"),

subject to the constraint $\ell \neq s$ when both are not "none" (a silent round produces $*$, which is neither $Y$ nor $N$, so there is no yes/no answer to lie about—hence the lie and silence must be on **different** rounds).

### Key Counts

**Number of configurations.** We count all valid $(\ell, s)$ pairs:

| Lie $\ell$ | Silence $s$ | Count |
|---|---|---|
| none | none | $1$ |
| none | round $j$ | $q$ |
| round $i$ | none | $q$ |
| round $i$ | round $j$, $i \neq j$ | $q(q-1)$ |

**Total:** $1 + q + q + q(q-1) = q^2 + q + 1$.

**Number of possible transcripts.** A transcript is a length-$q$ sequence over $\{Y, N, *\}$ with at most one $*$:

- **No $*$:** all $q$ entries are $Y$ or $N$: $2^q$ sequences.
- **Exactly one $*$:** choose the position of $*$ ($q$ choices), the remaining $q-1$ entries are $Y$ or $N$ ($2^{q-1}$ choices): $q \cdot 2^{q-1}$ sequences.

**Total:** $M = 2^q + q \cdot 2^{q-1}$.

---

## The Injectivity Lemma (Key Step)

**Lemma.** *For any fixed strategy (decision tree) and any fixed target $x$, the map from configurations to transcripts is injective: distinct configurations produce distinct transcripts.*

**Proof.** Suppose two configurations $(\ell_1, s_1) \neq (\ell_2, s_2)$ produce the same transcript $\tau = (a_1, \ldots, a_q)$. We show $(\ell_1, s_1) = (\ell_2, s_2)$, a contradiction.

**Step 1: The transcript determines the path, hence the questions.** The strategy is a deterministic decision tree. Given the full transcript $\tau$, the path through the tree is uniquely determined: at each round $i$, the answer $a_i$ determines which child to descend into. Therefore, the question $Q_i$ asked at each round $i$ is uniquely determined by $\tau$.

**Step 2: The questions and target determine the truthful answers.** For each round $i$, the truthful answer is $a_i^* = Y$ if $x \in Q_i$ and $a_i^* = N$ otherwise. Since both $Q_i$ and $x$ are fixed, $a_i^*$ is uniquely determined.

**Step 3: The transcript and truthful answers determine the configuration.**

- **Silence position:** The rounds where $\tau$ has $*$ are exactly the silent rounds. Since at most one $*$ appears, the silence position $s$ is uniquely determined by $\tau$ alone. Hence $s_1 = s_2$.

- **Lie position:** Among the non-silent rounds, a round $i$ is a lie round if and only if $a_i \neq a_i^*$ (the transcript answer differs from the truthful answer). Since at most one lie is allowed, there is at most one such round. The lie position $\ell$ is therefore uniquely determined by $\tau$ and $x$. Hence $\ell_1 = \ell_2$.

Therefore $(\ell_1, s_1) = (\ell_2, s_2)$, contradicting our assumption. $\square$

**Corollary.** *For every target $x$, the number of distinct transcripts that $x$ can produce is exactly $q^2 + q + 1$ (one for each configuration).*

---

## The Volume Bound

### Defining the Covering Sets

Fix a strategy. For each transcript $\tau$, define:

$$T(\tau) = \bigl\{ x \in \{1, \ldots, N\} : \text{there exists a configuration } (\ell, s) \text{ such that target } x \text{ with configuration } (\ell, s) \text{ produces transcript } \tau \bigr\}.$$

This is the set of all targets that can give rise to transcript $\tau$ under some valid configuration.

### Necessary Condition for a Valid Strategy

For the strategy to guarantee correctness, whenever transcript $\tau$ is observed, the output set $S(\tau)$ (of size $\leq t$) must contain the true target. Since the true target could be any element of $T(\tau)$ (each $x \in T(\tau)$ can produce $\tau$ under some configuration), we need:

$$T(\tau) \subseteq S(\tau) \quad \text{for every transcript } \tau.$$

Since $|S(\tau)| \leq t$, this requires:

$$|T(\tau)| \leq t \quad \text{for every transcript } \tau. \tag{$\star$}$$

### Double Counting

We compute $\sum_\tau |T(\tau)|$ by swapping the order of summation:

$$\sum_\tau |T(\tau)| = \sum_\tau \sum_{x} \mathbf{1}[x \in T(\tau)] = \sum_{x} \sum_\tau \mathbf{1}[x \in T(\tau)] = \sum_{x=1}^{N} |A(x)|,$$

where $A(x) = \{\tau : x \text{ can produce } \tau\}$ is the set of transcripts that target $x$ can generate.

By the Injectivity Lemma (Corollary), $|A(x)| = q^2 + q + 1$ for every $x$. Therefore:

$$\sum_\tau |T(\tau)| = N(q^2 + q + 1). \tag{1}$$

### Applying the Constraint

The sum runs over all possible transcripts. The number of possible transcripts is at most $M = 2^q + q \cdot 2^{q-1}$ (some transcripts may not appear as leaves of the decision tree, but no transcript outside this set can appear, since every transcript has at most one $*$). By constraint $(\star)$, each $|T(\tau)| \leq t$. Therefore:

$$\sum_\tau |T(\tau)| \leq M \cdot t = t\!\left(2^q + q \cdot 2^{q-1}\right). \tag{2}$$

### Combining (1) and (2)

$$N(q^2 + q + 1) = \sum_\tau |T(\tau)| \leq t\!\left(2^q + q \cdot 2^{q-1}\right).$$

This is a **necessary condition** for any valid strategy to exist.

---

## Conclusion

We have shown that any strategy guaranteeing identification of the target within $t$ candidates must satisfy:

$$N(q^2 + q + 1) \leq t\!\left(2^q + q \cdot 2^{q-1}\right).$$

By contrapositive, if

$$N(q^2 + q + 1) > t\!\left(2^q + q \cdot 2^{q-1}\right),$$

then **no such guaranteed strategy exists**. $\blacksquare$

---

## Summary of the Argument

The proof is a **volume (counting) bound** in the spirit of the Ulam–Rényi liar game framework:

1. **Each target $x$ generates exactly $q^2 + q + 1$ distinct transcripts** — one for each valid (lie position, silence position) configuration. The injectivity of the configuration-to-transcript map is the crucial step: given a transcript and a target, the configuration is uniquely recoverable (the $*$'s reveal the silence position; the mismatches with truthful answers reveal the lie position).

2. **Each transcript can "cover" at most $t$ targets** — the output set at that transcript has size $\leq t$ and must contain every target that could produce it.

3. **The total number of transcripts is at most $2^q + q \cdot 2^{q-1}$** — sequences of $q$ answers from $\{Y, N, *\}$ with at most one $*$.

4. **Double counting** gives $N(q^2 + q + 1) \leq t(2^q + q \cdot 2^{q-1})$, and violating this inequality makes a valid strategy impossible.
