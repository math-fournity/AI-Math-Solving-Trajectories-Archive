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

In a remote desert outpost, a circular solar power station, $\omega$, has been constructed with a radius of exactly $1$ kilometer. The station is positioned such that it is perfectly inscribed within a triangular security perimeter defined by three straight fencing segments, $AB$, $BC$, and $AC$. A maintenance sensor, $D$, is located at the specific point on the southern fence segment $BC$ where the circular station $\omega$ touches the perimeter.

An underground fiber-optic cable, $AD$, is laid in a straight line from the northern corner $A$ to the sensor $D$. This cable enters the circular power station's boundary at a point $X$ before reaching its terminus at $D$. 

Aerial surveys confirm the following spatial ratios regarding the layout: the distance from corner $A$ to the entry point $X$ ($AX$), the distance the cable travels inside the station from $X$ to $D$ ($XD$), and the total length of the southern fence $BC$ are in a ratio of $1 : 3 : 10$.

Based on these technical specifications, calculate the exact length of the cable segment $XD$.

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
