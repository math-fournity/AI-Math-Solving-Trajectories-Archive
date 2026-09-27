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

In a remote territory, a telecommunications company is planning to install a central signal hub at point $T$ to serve three rural outposts located at coordinates $A$, $B$, and $C$. These outposts form the vertices of a scalene triangle where all internal angles are less than $90^\circ$. 

The engineering team determines that to minimize interference, the signal hub $T$ must be positioned such that the transmission lines $(AT, BT, CT)$ meet at specific angles: the angle between the lines to outposts $A$ and $B$ ($\angle ATB$) must be exactly $120^\circ$, and the angle between the lines to outposts $B$ and $C$ ($\angle BTC$) must also be exactly $120^\circ$.

A survey drone is programmed to fly in a circular path. The center of this circular flight path is located at a control station $E$, and the path is calibrated to pass exactly through the three midpoints of the roads connecting the outposts (the midpoints of segments $AB$, $BC$, and $CA$). 

During the final inspection, the lead surveyor notes a unique alignment: the outpost at $B$, the signal hub at $T$, and the control station at $E$ all lie perfectly along a single straight line.

Based on this specific geometric configuration, calculate the measure of the interior angle at outpost $B$ (angle $ABC$) in degrees.

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
