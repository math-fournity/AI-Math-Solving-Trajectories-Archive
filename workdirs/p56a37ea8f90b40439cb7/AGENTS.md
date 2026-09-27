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

Let $\mathcal{FG}$ be the category of finite groups, and let $S$ be a full subcategory of $\mathcal{FG}$. Assume that $G \in \mathcal{FG}$ and $P \in S$ is a subgroup of $G$. We say that $P$ is $S$-maximal if there is no object $P' \in S$ with $P \subset P' \subset G$. Assume that $S$ satisfies the following conditions:

1. The subcategory $S$ is closed under taking subgroups, extensions, and isomorphisms. That is, if $P \in S$ and $Q \subset P$, then $Q \in S$. Moreover, for every short exact sequence $1 \to P \to Q \to R \to 1$, we have $Q \in S$ if $P, R \in S$. Additionally, every group isomorphic to an object of $S$ lies in $S$.

2. For every $G \in \mathcal{FG}$, every two $S$-maximal subgroups of $G$ are conjugate. Moreover, for every maximal $S$-subgroup $P$ of $G \in \mathcal{FG}$, we have $N(N(P)) = N(P)$ and $|G|/|N(P)|$ is coprime to $|P|$.

Does it follow that $S$ is the category of $p$-groups for some prime number $p$?

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出：

   ### PROOF COMPLETE

3. **如果你无法做出这道题**，直接说：

   ### I CANNOT SOLVE THIS

4. **如果你发现题目中包含了答案**（答案泄漏），直接说：

   ### ANSWER LEAK DETECTED

以上是全部约束。现在请解题。
