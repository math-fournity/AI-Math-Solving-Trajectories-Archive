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

In a futuristic circular city, six communication towers—$A, B, C, D, E,$ and $F$—are positioned along the city's perimeter road, which forms a perfect circle. To manage the network, several signal relay stations have been constructed at the intersections of straight fiber-optic lines connecting these towers:

1. Relay station $P$ is located where the line through towers $A$ and $B$ meets the line through towers $D$ and $C$. The angle of the signal beams crossing at $P$ (specifically $\angle BPC$) is measured at $50^{\circ}$.
2. Relay station $Q$ is located where the line through $B$ and $C$ meets the line through $E$ and $D$. The angle $\angle CQD$ is $45^{\circ}$.
3. Relay station $R$ is located where the line through $C$ and $D$ meets the line through $F$ and $E$. The angle $\angle DRE$ is $40^{\circ}$.
4. Relay station $S$ is located where the line through $D$ and $E$ meets the line through $A$ and $F$. The angle $\angle ESF$ is $35^{\circ}$.

A central hub, station $T$, is positioned exactly at the intersection of the direct lines connecting tower $B$ to tower $E$ and tower $C$ to tower $F$.

Calculate the measure of the angle $\angle BTC$ at the central hub in degrees.

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
