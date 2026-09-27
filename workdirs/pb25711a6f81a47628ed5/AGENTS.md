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

In a specialized port facility, a robotic arm $O$ is positioned at the origin of a digital mapping system. Two sensors, $A_n$ and $B_n$, move along specific tracks as a sequence of tests $n = 1, 2, 3, \dots$ is performed. 

Sensor $A_n$ moves along a vertical track (the positive $y$-axis), while sensor $B_n$ moves along a curved rail defined by the efficiency trajectory $y = \sqrt{2x}$ for $x \geq 0$. During each test $n$, both sensors are deployed such that their direct distances from the robotic arm $O$ are exactly equal to the reciprocal of the test number, expressed as $|OA_n| = |OB_n| = \frac{1}{n}$.

For every test, a laser beam is fired along the straight line connecting sensor $A_n$ and sensor $B_n$. We define $a_n$ as the coordinate where this laser beam intersects the horizontal floor (the $x$-axis). Additionally, $b_n$ represents the horizontal distance of sensor $B_n$ from the vertical track.

Calculate the value of $a_1$ from the first test, and determine the stabilization limit $L = \lim_{n \to \infty} a_n$ as the number of tests increases indefinitely. Find the final combined value of $a_1 + L$.

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
