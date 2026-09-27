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

A specialized aerospace engineering firm is testing the stability of a drone's flight path governed by two physical constraints involving a horizontal displacement $x$ and a lateral stability coefficient $y$.

The first constraint relates the drone’s power output to its stability through the aerodynamic equilibrium equation:
The difference between three times the displacement and one, minus twice the displacement cubed, must exactly equal the product of twice the displacement cubed, the difference between the stability coefficient squared and one, and the square root of the quantity one plus twice the stability coefficient squared.

The second constraint concerns the structural integrity of the wing, defined by the stress-load balance:
The cube root of the displacement minus four, added to a constant offset of three, must equal the square root of the quantity: negative four minus the product of the displacement and the square root of the quantity one plus twice the stability coefficient squared.

Engineers must identify all real coordinate pairs $(x, y)$ that satisfy both the aerodynamic equilibrium and the stress-load balance simultaneously. Let these valid configurations be denoted as $(x_1, y_1), (x_2, y_2), \dots, (x_k, y_k)$. 

Calculate the total system efficiency, defined as the sum $\sum_{i=1}^k (x_i + y_i^2)$.

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
