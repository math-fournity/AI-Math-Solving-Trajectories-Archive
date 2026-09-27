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

A digital artist is designing a repeating mosaic on a 20x20 grid of pixels. The color of each pixel at coordinate $(i, j)$ is determined by its "color-index," which is the remainder of $i+j$ when divided by 5. There are 5 possible colors: 0, 1, 2, 3, and 4.

The artist selects a rectangular region of the grid defined by the corners $(0, 0)$, $(a, 0)$, $(a, b)$, and $(0, b)$, where $a$ and $b$ are integers between 1 and 20 inclusive.

The artist defines a rectangle as "balanced" if it satisfies two strict aesthetic conditions:
1. Along the boundary of the rectangle (the four edges), each of the 5 colors appears exactly the same number of times. Note: The pixels at the four vertices are counted as part of the boundary.
2. In the interior of the rectangle (the area strictly inside the four edges), each of the 5 colors appears exactly the same number of times.

Let $S$ be the set of all possible pairs $(a, b)$ that result in a balanced rectangle within the 20x20 limit. Determine the number of elements in the set $S$.

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
