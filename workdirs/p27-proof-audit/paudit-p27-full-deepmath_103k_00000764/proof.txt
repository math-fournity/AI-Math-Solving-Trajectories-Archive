# Proof

**Claim.** For every natural number $n$, there exists a natural number $N$ such that for any subset $A$ of $\{1, 2, \ldots, N\}$, either $A$ or its complement $\overline{A} = \{1,\ldots,N\}\setminus A$ contains an arithmetic progression of length $n$.

**Answer: TRUE.**

## Reduction to van der Waerden's theorem

We show the claim is exactly the $r=2$, $k=n$ special case of **van der Waerden's theorem**:

> **van der Waerden's theorem.** For all positive integers $r$ and $k$, there exists a number $W(r,k)$ such that every $r$-coloring of $\{1,2,\ldots,W(r,k)\}$ contains a monochromatic arithmetic progression of length $k$.

Given $n$, set $N = W(2,n)$. Let $A \subseteq \{1,\ldots,N\}$ be arbitrary. Define a 2-coloring $c:\{1,\ldots,N\}\to\{1,2\}$ by
$$
c(i) = \begin{cases} 1 & \text{if } i \in A,\\ 2 & \text{if } i \in \overline{A}.\end{cases}
$$
By van der Waerden's theorem (with $r=2$, $k=n$), there is a monochromatic arithmetic progression $a, a+d, a+2d, \ldots, a+(n-1)d$ of length $n$ inside $\{1,\ldots,N\}$. Monochromatic means all its terms share one color: either color $1$, in which case the whole progression lies in $A$; or color $2$, in which case it lies in $\overline{A}$. This is exactly what the claim requires. $\square$

## Justification of van der Waerden's theorem (proof sketch)

We recall the standard double-induction proof (Graham–Rothschild–Spencer; see also *Proofs from THE BOOK*), which establishes $W(r,k)$ for all $r,k\ge 1$.

**Base cases.** $W(1,k)=k$ (a single color makes the first $k$ points a monochromatic AP), and $W(r,1)=1$ (an AP of length $1$ is trivially monochromatic). Also $W(r,2)=r+1$ by the pigeonhole principle.

**Inductive structure.** Fix $k\ge 2$ and assume $W(r,k-1)$ exists for every $r$ (outer induction on $k$). We prove $W(r,k)$ exists by induction on $r$. The key tool is the notion of a **color-focused fan**:

> **Definition.** In an $r$-coloring of $\{1,\ldots,L\}$, a *fan of degree $m$ with focus $f$* is a collection of $m$ monochromatic APs $P_1,\ldots,P_m$, each of length $k-1$, each of a (pairwise) distinct color, with respective common differences $d_1,\ldots,d_m$ (which may differ), such that every $P_i$ ends at the same point $f$:
> $$P_i = \{f-(k-1)d_i,\; f-(k-2)d_i,\;\ldots,\; f-d_i,\; f\}\setminus\{f\}, \qquad i=1,\ldots,m.$$

The crucial observation: **if a fan of degree $r$ exists (covering all $r$ colors), then a monochromatic AP of length $k$ exists.** Indeed, the focus $f$ itself has some color $j$; appending $f$ to $P_j$ extends the color-$j$ progression $P_j$ to length $k$.

**Fan lemma.** For every $m\le r$ there exists $L_m$ such that every $r$-coloring of $\{1,\ldots,L_m\}$ contains a fan of degree $m$.

*Proof of the fan lemma (induction on $m$).* Set $w = W(r,k-1)$ (which exists by the outer induction on $k$).

- **Base $m=1$:** Take $L_1 = w$. By definition of $W(r,k-1)=w$, any $r$-coloring of $\{1,\ldots,w\}$ contains a monochromatic AP of length $k-1$; this is a fan of degree $1$ (its last element is the focus).

- **Inductive step $m-1\to m$:** Assume $L_{m-1}$ exists. Set
$$L_m = 2w\cdot L_{m-1}.$$
Partition $\{1,\ldots,L_m\}$ into $2L_{m-1}$ consecutive blocks $B_1,\ldots,B_{2L_{m-1}}$, each of size $w$. In each block $B_s$, by $W(r,k-1)=w$, there is a monochromatic AP of length $k-1$; record its color $c_s\in\{1,\ldots,r\}$ and the *relative position* of its focus within the block, i.e. an index $\rho_s\in\{1,\ldots,w\}$ (the offset of the focus from the block's left endpoint). This produces a sequence of $2L_{m-1}$ "typed" blocks, each carrying a label $(c_s,\rho_s)\in\{1,\ldots,r\}\times\{1,\ldots,w\}$.

Now apply the induction hypothesis $L_{m-1}$ to the *sequence of labels*: viewing the $2L_{m-1}$ blocks as positions colored by their label $(c_s,\rho_s)$ from a palette of $rw$ possible labels, and using $W(rw,\,2)=rw+1\le 2L_{m-1}$ (pigeonhole), we extract a sub-collection of blocks whose labels agree. More precisely, by the inductive construction of $L_{m-1}$ applied at the level of the label sequence, one obtains $m-1$ blocks $B_{s_1},\ldots,B_{s_{m-1}}$ carrying fans of degree $m-1$ that are *aligned*: their foci sit at the same relative position $\rho$ inside their respective blocks, and the blocks themselves are equally spaced (common block-difference $\Delta$). The color of the fan inside $B_{s_i}$ is some color $c^{(i)}$, and these $m-1$ colors are distinct.

Because the foci are at the same relative position $\rho$ in equally-spaced blocks, the actual foci in $\{1,\ldots,L_m\}$ form an arithmetic progression with common difference $\Delta\cdot w$. Looking one block further along this progression, at block $B_{s_m}:=B_{s_1+\Delta\cdot m}$ (which exists since we reserved $2L_{m-1}$ blocks), the point at relative position $\rho$ in $B_{s_m}$ is the common focus $f$ of a fan of degree $m$: the $m-1$ existing APs (translated to end at $f$) contribute $m-1$ distinct colors, and the AP of length $k-1$ inside $B_{s_m}$ contributes a new color (distinct from the others by construction). This yields a fan of degree $m$, completing the induction. $\square$ (fan lemma)

**Completing the proof.** Taking $m=r$ in the fan lemma gives $L_r$ such that every $r$-coloring of $\{1,\ldots,L_r\}$ contains a fan of degree $r$. As noted above, a fan of degree $r$ forces a monochromatic AP of length $k$. Hence $W(r,k)\le L_r$ exists, completing the inner induction on $r$, and thus the outer induction on $k$.

Therefore van der Waerden's theorem holds for all $r,k\ge 1$, and in particular $W(2,n)$ exists for every $n$, which is exactly what the claim requires.

$$\boxed{\text{TRUE}}$$

### PROOF COMPLETE
