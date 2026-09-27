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

In a remote desert, two research outposts, Station A and Station B, are established. A mobile drone, designated as Unit M, is surveying the terrain at any location that is not directly on the straight road connecting the two stations.

The drone's mission parameters involve two fixed efficiency constants, $a$ and $b$, both of which are values between 0 and 1. To maintain data synchronization, the drone’s software automatically designates two signal relay points, $P$ and $N$, based on the drone's current position:
- Relay Point $N$ is positioned on the straight-line path between Station B and the drone such that the distance from the station to the relay is exactly a fraction $b$ of the total distance from the station to the drone ($BN = b \cdot BM$).
- Relay Point $P$ is positioned on the straight-line path between Station A and the drone such that the distance from the station to the relay is exactly a fraction $a$ of the total distance from the station to the drone ($AP = a \cdot AM$).

The relay points $P$ and $N$ are never located exactly at the stations or at the drone's current position.

A specialized communication link is only possible when the distance from Station A to Relay Point $N$ is perfectly equal to the distance from Station B to Relay Point $P$ ($AN = BP$). Determine the geometric locus of all possible coordinates for Unit M that satisfy this specific distance equality.

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
