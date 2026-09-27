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

In the city of Quadrata, a central plaza is shaped like a perfect square $ABCD$. Two main decorative stone pathways are laid out in the shape of a parallelogram $AECF$ (where $E$ lies on side $BC$ and $F$ lies on side $AD$). A team of architects decides to install a second set of identical pathways by reflecting the first set across the diagonal $AC$, creating a new parallelogram $AE'CF'$.

The zone where these two parallelogram pathways overlap is designated as a "Heritage Garden." This garden has a total surface area of $m$ square units and a boundary length (perimeter) of $n$ units. 

An observer notes that the distance from vertex $A$ to the point $F$ along the plaza's edge is exactly one-quarter of the total length of the edge $AD$ (such that $AF : AD = 1 : 4$). 

To finalize the project budget, the planners need to calculate the ratio of the garden's area to the square of its perimeter, expressed as $\frac{m}{n^2}$. If this ratio is represented as an irreducible fraction $\frac{a}{b}$, what is the value of $a+b$?

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
