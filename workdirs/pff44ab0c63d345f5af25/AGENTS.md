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

An architect is designing a kite-shaped plaza, $ABCD$, where the northern walkways $AB$ and $AD$ are equal in length, and the southern boundary walls $BC$ and $CD$ are also equal. 

Inside this plaza, a rectangular central stage $KLL_1K_1$ is constructed such that its corners $K, L, L_1, K_1$ lie on the boundaries $AB, BC, CD, DA$ respectively. 

To maximize utility, two smaller rectangular storage units are built within the remaining triangular corner spaces. The first unit $MNPQ$ is built within the triangular garden $BLK$, with vertices $M$ on $KB$, $N$ on $BL$, and the side $PQ$ resting on the stage boundary $LK$. The second unit $M_1N_1P_1Q_1$ is built within the triangular garden $DK_1L_1$, with vertices $M_1$ on $DK_1$, $N_1$ on $DL_1$, and the side $P_1Q_1$ resting on the stage boundary $L_1K_1$.

Let $S$ represent the total area of the kite-shaped plaza $ABCD$. Let $S_1$ be the area of the central stage $KLL_1K_1$. Let $S_2$ and $S_3$ be the areas of the storage units $MNPQ$ and $M_1N_1P_1Q_1$ respectively.

As the positions of the stage corners are adjusted along the plaza boundaries, determine the maximum possible value of the ratio:
\[ \frac{S_1 + S_2 + S_3}{S} \]

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
