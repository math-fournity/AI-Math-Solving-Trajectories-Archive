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

Determine the symmetry group of the following configuration: Consider six points $A_1$, $A_2$, $\cdots$, $A_6$ on a circle $(O_A)$ and a point $B_1$ on another circle $(O_B)$. Let the circle $(A_iA_{i+1}B_i)$ meet $(O_B)$ again at $B_{i+1}$ for $i=1,\cdots, 5$. Then the four points $A_6$, $A_1$, $B_1$, $B_6$ lie on a circle. Denote by $(O_i)$ the circle $(A_iA_{i+1}B_{i+1}B_i)$ for $i=1,\cdots,6$, taking subscripts modulo 6. If $(O_1)$ meets $(O_4)$ at two points $C_3, C_6$, $(O_2)$ meets $(O_5)$ at two points $C_4, C_1$, and $(O_3)$ meets $(O_6)$ at two points $C_2, C_5$, then the six points $C_1$, $C_2$, $C_3$, $C_4$, $C_5$, $C_6$ lie on a circle. What is the symmetry group of this configuration?

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
