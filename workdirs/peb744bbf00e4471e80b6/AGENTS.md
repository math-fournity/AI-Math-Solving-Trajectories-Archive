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

In a remote desert, two long, straight pipelines meet at a central pumping station, designated as Point $A$. Pipeline $1$ extends from the station through a pressure gauge at Point $B$ and continues to a storage tank at Point $E$. Pipeline $2$ extends from the same station through a pressure gauge at Point $C$ and continues to a storage tank at Point $D$.

The distances from the pumping station are precisely measured: $AB = 2$ kilometers, $AC = 5$ kilometers, $AD = 200$ kilometers, and $AE = 500$ kilometers. The angle between the two pipelines at the station, $\angle BAC$, has a cosine value of $7/9$.

A land developer has purchased the convex quadrilateral-shaped plot of land bounded by the segments $BC$, $CD$, $DE$, and $EB$. They intend to install a series of circular cooling ponds within this boundary. To simplify the plumbing, every pond must be tangent to both the pipeline path $BE$ and the pipeline path $CD$.

What is the largest number of such nonoverlapping circular ponds that can be constructed entirely within the quadrilateral plot $BCDE$?

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
