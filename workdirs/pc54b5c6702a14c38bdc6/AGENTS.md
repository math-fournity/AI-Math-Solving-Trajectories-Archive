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

A high-security perimeter fence forms a square with a side length of 4 kilometers, centered at a central command tower located at the origin $O$. Sixteen surveillance sensors, $P_1, P_2, \ldots, P_{16}$, are installed along this perimeter such that the distance between any two consecutive sensors $P_i$ and $P_{i+1}$ is exactly 1 kilometer (where $P_{17}$ is defined as $P_1$).

Each sensor is equipped with a toggle that can flip its reported position. For each sensor $i$, a technician flips a fair coin. If the coin lands heads, the active coordinate $Q_i$ is set to the sensor's actual location $P_i$. If the coin lands tails, $Q_i$ is set to the point exactly opposite the tower from $P_i$ (the reflection of $P_i$ across point $O$).

The tower's central computer calculates a "Net Displacement Vector" by summing the position vectors of these sixteen active coordinates: $\vec{V} = \overrightarrow{OQ_1} + \overrightarrow{OQ_2} + \cdots + \overrightarrow{OQ_{16}}$. Let $D$ be the magnitude of this resulting vector $\vec{V}$.

Compute the expected value of $D^2$.

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
