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

In a remote research facility, an automated scanner monitors the structural integrity of a circular particle track with a total circumference of $2\pi$ meters. A sensor moves along this track, starting at position $x = 0$ and ending at $x = 2\pi$.

At every point $x$ along the track, the sensor calculates a "Stability Index," denoted by $f(x)$. The index is derived from the interference of two distinct vibration waves. The first wave follows the function $\sin(20x)$ and the second follows $\cos(24x)$. The Stability Index is calculated by taking the absolute value of the sum of these two waves and then reducing the result by half, such that $f(x) = \frac{1}{2}|\sin(20x) + \cos(24x)|$. 

Engineers have observed that throughout the entire track, this index remains strictly between 0 and 1. To optimize the facility's power consumption, the chief scientist needs to determine the average Stability Index across the full duration of the track.

Calculate the average value of $f$ over the interval $[0, 2\pi]$. Express your answer in the decimal form $0.abcdef$. If your calculated average is $V$, report the final integer result as $\lfloor 10^6 V \rfloor$.

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
