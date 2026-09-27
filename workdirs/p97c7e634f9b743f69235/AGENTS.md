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

$A_{1} A_{2} A_{3} A_{4}$ is a cyclic quadrilateral inscribed in circle $\Omega$, with side lengths $A_{1} A_{2}=28$, $A_{2} A_{3}=12 \sqrt{3}$, $A_{3} A_{4}=28 \sqrt{3}$, and $A_{4} A_{1}=8$. Let $X$ be the intersection of $A_{1} A_{3}$ and $A_{2} A_{4}$. For $i=1,2,3,4$, let $\omega_{i}$ be the circle tangent to segments $A_{i} X$, $A_{i+1} X$, and $\Omega$, where indices are taken cyclically $(\bmod 4)$. For each $i$, $\omega_{i}$ is tangent to $A_{1} A_{3}$ at $X_{i}$, $A_{2} A_{4}$ at $Y_{i}$, and $\Omega$ at $T_{i}$. Let $P_{1}$ be the intersection of $T_{1} X_{1}$ and $T_{2} X_{2}$, and $P_{3}$ the intersection of $T_{3} X_{3}$ and $T_{4} X_{4}$. Let $P_{2}$ be the intersection of $T_{2} Y_{2}$ and $T_{3} Y_{3}$, and $P_{4}$ the intersection of $T_{1} Y_{1}$ and $T_{4} Y_{4}$. Find the area of quadrilateral $P_{1} P_{2} P_{3} P_{4}$.

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
