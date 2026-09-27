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

A maritime engineering firm is testing an automated stabilization system for a ship. The system’s vertical oscillation is determined by the interference of three distinct wave generators. Each generator produces a pure sine wave frequency corresponding to an integer setting on a control dial. 

The first generator is set to a fixed natural number frequency $k_0$. The second and third generators are set to natural number frequencies $k_1$ and $k_2$, respectively, such that $k_0 < k_1 < k_2$. While the frequencies are fixed integers, the intensity of the second generator ($A_1$) and the third generator ($A_2$) can be adjusted to any real number value. The first generator always maintains a baseline intensity of 1.

The total displacement of the water surface $y$ at a relative time $x$ (where $x$ is measured in radians over one full cycle from $0$ to $2\pi$) is given by the sum of these three waves:
$$y(x) = \sin(k_0 x) + A_1 \sin(k_1 x) + A_2 \sin(k_2 x)$$

An "equilibrium point" occurs whenever the total displacement $y(x)$ is exactly zero. Given the specific integer frequencies $k_0, k_1,$ and $k_2$, what is the minimum possible number of equilibrium points that can exist on the half-open time interval $[0, 2\pi)$?

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
