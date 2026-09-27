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

# Problem

In the remote alpine region of Triangulia, three base camps—A, B, and C—form a scalene territory. A logistics officer is mapping a sequence of supply depots $I_t$. The primary depot $I_0$ is located exactly at camp $A$. For every subsequent year $t = 1, 2, 3, \dots$, a new depot $I_t$ is established at the "center of safety" (the incenter) of the triangular region formed by the previous depot $I_{t-1}$ and the fixed camps $B$ and $C$.

A geological survey reveals that the primary camp $A$ and all subsequent depots $I_1, I_2, \dots$ lie perfectly along a natural hyperbolic ridge $\mathcal{H}$. The boundaries of the valley containing this ridge are defined by two straight canyon walls, $\ell_1$ and $\ell_2$, which serve as the asymptotes of the hyperbola.

A straight supply road is constructed passing through camp $A$ such that it is perpendicular to the straight path connecting camps $B$ and $C$. This road intersects the first canyon wall $\ell_1$ at point $P$ and the second canyon wall $\ell_2$ at point $Q$. 

Satellite measurements confirm that the squared distance between camps $A$ and $C$ is exactly $1$ unit more than $\frac{12}{7}$ times the squared distance between camps $A$ and $B$ (i.e., $AC^2 = \frac{12}{7}AB^2 + 1$). 

The regional director wishes to minimize the land area of the quadrilateral zone $BPCQ$. Given that the smallest possible value of this area can be expressed in the form $\frac{j\sqrt{k}+l\sqrt{m}}{n}$ for positive integers $j, k, l, m, n$ where $\gcd(j,l,n)=1$, the radicals $k$ and $m$ are squarefree, and $j > l$, compute the value of $10000j + 1000k + 100l + 10m + n$.

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出（必须用英文原文，不要翻译成中文）：

   ### PROOF COMPLETE

3. **如果你无法做出这道题**，直接说（必须用英文原文）：

   ### I CANNOT SOLVE THIS

4. **如果你发现题目中包含了答案**（答案泄漏），直接说：

   ### ANSWER LEAK DETECTED

以上是全部约束。现在请解题。
