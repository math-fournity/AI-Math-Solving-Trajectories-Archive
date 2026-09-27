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

In a remote sector of the ocean, a rectangular rescue zone is defined by four coordinates. A high-tech pirate vessel is currently stationed at point $C$, while two merchant ships are located at points $B$ and $D$. The four points $A, B, C,$ and $D$ form a perfect square with side length $s$. 

The merchant ships are attempting to reach a safe harbor located at point $A$. To get there, the ship at $B$ must travel along the straight-line path (ray) $[BA$ towards $A$, and the ship at $D$ must travel along the straight-line path (ray) $[DA$ towards $A$. Both merchant ships have a maximum speed of $1$ knot.

The pirate vessel at $C$ intends to intercept both merchant ships before they can enter the safety of harbor $A$. Unlike the merchant ships, the pirate vessel is not restricted to specific paths and can travel in any direction across the open water at a maximum speed of $v$ knots.

Determine the minimum value of $v$ such that, regardless of the merchant ships' strategies, the pirate vessel can successfully intercept both ships (at any point on or before they reach $A$).

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
