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

Robert is a robot who can move freely on the unit circle and its interior, but is attached to the origin by a retractable cord such that at any moment the cord lies in a straight line on the ground connecting Robert to the origin. Whenever his movement is counterclockwise (relative to the origin), the cord leaves a coating of black paint on the ground, and whenever his movement is clockwise, the cord leaves a coating of orange paint on the ground. The paint is dispensed regardless of whether there is already paint on the ground. The paint covers 1 gallon/unit², and Robert starts at \((1,0)\). Each second, he moves in a straight line from the point \((\cos (\theta), \sin (\theta))\) to the point \((\cos (\theta+\alpha), \sin (\theta+\alpha))\), where \(\alpha\) changes after each movement. \(\alpha\) starts out as \(253^{\circ}\) and decreases by \(2^{\circ}\) each step. If he takes 89 steps, then the difference, in gallons, between the amount of black paint used and orange paint used can be written as \(\frac{\sqrt{a}-\sqrt{b}}{c} \cot 1^{\circ}\), where \(a, b\) and \(c\) are positive integers and no prime divisor of \(c\) divides both \(a\) and \(b\) twice. Find \(a+b+c\).

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
