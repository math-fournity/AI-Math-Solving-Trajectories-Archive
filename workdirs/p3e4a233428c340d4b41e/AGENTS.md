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

In a sprawling logistics warehouse measuring $10 \times 10$ meters, three different safety inspectors independently ordered three identical floor tarps, each also measuring $10 \times 10$ meters. To avoid wasting the surplus material, the warehouse manager decided to layer all three tarps over the floor, aligning them strictly with the warehouse corners.

The first tarp was folded so that it covered a rectangular region of $6 \times 8$ meters, tucked into the northwest corner. The second tarp was folded into a $6 \times 6$ meter square and placed firmly into the southeast corner. The third tarp was folded into a $5 \times 7$ meter rectangle and positioned in the southwest corner. 

Assuming the warehouse floor is a perfect coordinate plane with corners at $(0,10), (10,10), (10,0),$ and $(0,0)$, the tarps occupy the following regions:
- Tarp 1: From $(0,2)$ to $(6,10)$
- Tarp 2: From $(4,0)$ to $(10,6)$
- Tarp 3: From $(0,0)$ to $(5,7)$

Find the area of the portion of the warehouse floor that is covered by all three layers of tarps (give the answer in square meters).

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
