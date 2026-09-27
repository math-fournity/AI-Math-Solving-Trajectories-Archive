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

In $\triangle ABC$ with $AB < AC < BC$, let $O$ and $I$ be its circumcenter and incenter, respectively. Let $M_b$ and $M_c$ be the midpoints of the arc $AC$ (not containing $B$) and the arc $AB$ (not containing $C$), respectively, on the circumcircle $\odot O$. Let $S_b$ be a point on $\odot O$ such that $IS_b \perp BS_b$, and let $S_c$ be a point on $\odot O$ such that $IS_c \perp CS_c$. Let $H_a$ be the intersection of lines $M_bS_c$ and $M_cS_b$. Points $H_b$ and $H_c$ are defined analogously.It is given that the lines $AH_a, BH_b, CH_c$ are pairwise non-parallel. Let $G$ be the centroid of the triangle formed by these lines (if the three lines are concurrent, $G$ is defined as their point of concurrency). Let the side lengths of $\triangle ABC$ be $BC = a$, $CA = b$, and $AB = c$. Find the product of the distances from point $G$ to the lines $IH_a, IH_b, IH_c$. (Expressed in terms of $a, b, c$ and simplified completely.)
After solving the above problem, please output your final answer in the following format:
### The final answer is: $\boxed{<your answer>}$
Example:
### The final answer is: $\boxed{a+b+c}$
Your final answer must be a formula containing a, b, and c.
Your final answer must not contain any intermediate variables other than a, b, and c, such as s, r, R, or \delta.
Do not include any restrictions on the values of a, b, or c in your final answer.
The final answer should be given as precisely as possible (using LaTeX symbols such as \sqrt, \frac, \pi, etc.). If the final answer involves a decimal approximation, it must be accurate to at least four decimal places.

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
