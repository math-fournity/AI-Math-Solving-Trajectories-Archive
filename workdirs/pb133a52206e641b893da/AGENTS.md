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

In the mountainous region of Arithema, a land surveyor is tasked with mapping a triangular nature reserve defined by three landmarks: the Cedar Grove ($C$), the Fir Ridge ($F$), and the Mossy Peak ($M$). The interior of this acute-angled triangle contains a circular sanctuary $\omega$ with a radius of $6$ units and a center point $O$. This sanctuary is perfectly nested so that it touches the boundary trails $CM$ and $FM$ at two specific observation posts, $P$ and $K$ respectively.

A secondary circular boundary $\Omega$ is drawn to pass through the three points $P$, $K$, and $M$. The radius $R$ of this circle $\Omega$ is exactly $\frac{5\sqrt{13}}{2}$ units, and its center is located at a ranger station $T$.

Satellite imagery reveals a specific spatial relationship: the area of the triangular region formed by the landmarks $C$, $F$, and the ranger station $T$ is exactly $5/8$ of the total area of the entire nature reserve $CFM$.

The surveyor needs to calculate two specific values for the environmental report:
1. Let $L$ be the length of the straight-line trekking path $MA$, which acts as the internal angle bisector of the reserve at Mossy Peak ($M$), ending at point $A$ on the boundary $CF$.
2. Let $S$ be the total area of the triangular nature reserve $CFM$.

Based on these measurements, determine the value of:
$$\frac{L^2}{13} + S$$

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
