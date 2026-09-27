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

In a futuristic city, two high-speed transit tracks, denoted as $l_1$ and $l_2$, are being constructed. These tracks are designed to be perfectly straight and must run tangent to a magnetic containment field defined by the boundary equation $x^2 - 4(x+y) + y^2 = 2xy + 8$.

The engineers have mandated that the two tracks must intersect at a specific control hub. While the exact location $(x_0, y_0)$ of this hub has not been finalized, the safety protocols strictly require that the sum of its coordinates must be exactly $-32$.

Each track has a specific gradient, or slope. Let $s_1$ be the slope of track $l_1$ and $s_2$ be the slope of track $l_2$. The construction firm aims to minimize the total gradient of the system, defined as the sum $s_1 + s_2$.

The minimum possible value of this sum can be expressed as a reduced fraction $\frac{m}{n}$, where $m$ and $n$ are relatively prime positive integers. Find the value of $m + n$.

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
