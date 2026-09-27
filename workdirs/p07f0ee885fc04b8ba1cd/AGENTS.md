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

In a remote sector of the North Sea, an offshore engineering firm is installing a triangular structural frame composed of three heavy-duty girders: Line A, Line B, and Line C. These girders connect three anchor points—Apex Alpha, Apex Beta, and Apex Gamma—forming a triangle.

A stabilization cable is stretched from Apex Gamma to a specific junction point, Joint X, located on the girder connecting Alpha and Beta. Monitoring sensors indicate that the angle formed between the girder segment (Beta to Joint X) and the stabilization cable is exactly 60°.

A secondary support beam is installed starting from Apex Beta and terminating at a point, Node P, located somewhere along the stabilization cable. This support beam is oriented so that it is perfectly perpendicular to the girder connecting Alpha and Gamma.

The engineering specifications for the frame are as follows:
- The length of the girder between Apex Alpha and Apex Beta is 6 units.
- The length of the girder between Apex Alpha and Apex Gamma is 7 units.
- The length of the support beam from Apex Beta to Node P is 4 units.

Based on these structural dimensions, calculate the precise distance between Apex Gamma and Node P.

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
