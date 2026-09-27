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

A remote island's radar system uses three communication beacons located at coordinates $A$, $B$, and $C$. The distances between these beacons form an isosceles triangle where the transmission range from the central hub $C$ to both $A$ and $B$ is exactly $\sqrt{5}$ kilometers ($AC = BC = \sqrt{5}$).

A technician is deploying three sensors, $D$, $E$, and $F$, along the signal lines connecting the beacons. Sensor $D$ is placed at the precise midpoint of the baseline between $A$ and $B$, such that the distance from $A$ to $D$ and from $D$ to $B$ is exactly 1 kilometer ($AD = DB = 1$). Sensors $E$ and $F$ are mobile units placed on the signal lines $BC$ and $CA$, respectively, such that the direct distance between these two mobile units is maintained at exactly 1 kilometer ($EF = 1$).

During a calibration phase, the technician measures the relative positioning of the sensors using displacement vectors. It is observed that the dot product of the vectors representing the paths from sensor $D$ to sensor $E$ and from sensor $D$ to sensor $F$ satisfies the signal constraint $\overrightarrow{DE} \cdot \overrightarrow{DF} \le \frac{25}{16}$.

The system's efficiency depends on the alignment of the mobile sensor path relative to the baseline of the beacons. Let the possible values of the dot product between the vector $\overrightarrow{EF}$ and the vector $\overrightarrow{BA}$ be represented by the interval $[m, M]$. 

Find the value of $3m + M$.

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
