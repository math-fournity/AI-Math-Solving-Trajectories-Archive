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

A prestigious logistics firm is designing a complex hub-and-spoke delivery network involving $n$ regional distribution centers, where $n \geq 4$. These centers are situated at the vertices of a convex $n$-sided perimeter.

To ensure redundancy in the system, the firm plans to install two separate types of high-speed transit lines:
1.  **Green Hyperloops:** Exactly $n-3$ straight green hyperloop tracks are built between non-adjacent centers. The layout is designed such that no two green hyperloop tracks cross each other.
2.  **Red Pneumatic Tubes:** Exactly $n-3$ straight red pneumatic tube lines are built between non-adjacent centers. Similarly, the layout is designed such that no two red pneumatic tube lines cross each other.

Engineers are concerned about the complexity of the network and want to determine $I(n)$, defined as the maximum possible number of locations where a green hyperloop track and a red pneumatic tube line could cross paths within the interior of the perimeter.

Calculate the total sum of these maximum intersection points as the number of centers grows from 4 to 10:
$$\sum_{n=4}^{10} I(n)$$

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
