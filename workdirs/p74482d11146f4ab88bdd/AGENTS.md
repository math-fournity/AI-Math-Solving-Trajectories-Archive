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

A block of cheese in the shape of a triangular prism with height \(3 \, \text{cm}\) and equilateral bases of side length \(4 \, \text{cm}\) is grated along a plane parallel to one of its lateral (non-base) faces. The grater is initially placed at the edge of the prism opposite the lateral face, and over time the prism is truncated along this edge. Call the "width" of the cheese the distance between the grater and the lateral face. The cheese that is grated falls into a funnel that is a square pyramid with height \(3 \sqrt{3} \, \text{cm}\) and base of side length \(4 \, \text{cm}\); the cheese falls through the square base at the top toward the vertex. Assume that the grated cheese is fine enough to fill the funnel continuously. If the width of the cheese decreases at a rate of \(1 \, \text{cm/s}\) when the width is \(2 \sqrt{3}-\sqrt{2} \, \text{cm}\), the height of the cheese in the funnel increases at a rate of \(d \, \text{cm/s}\). Compute \(d\).

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
