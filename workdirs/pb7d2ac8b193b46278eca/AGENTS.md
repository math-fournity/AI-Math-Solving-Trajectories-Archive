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

In a remote territory, three supply depots—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. A central logistics hub, the Incenter ($I$), is positioned such that it is equidistant from the three straight roads connecting the depots. This distance, the "inner supply radius," is exactly $r = 4$ units. The points where the supply lines from $I$ meet the roads $BC$, $CA$, and $AB$ are designated as checkpoints $D$, $E$, and $F$, respectively.

The entire region is monitored by a regional command tower, the Circumcenter ($O$), which is equidistant from the three depots $A$, $B$, and $C$. This "outer surveillance radius" is $R = \frac{65}{8}$ units.

Field engineers have mapped two specific trajectory lines:
1. A transmission line passing through checkpoints $F$ and $D$ extends until it intersects the road $CA$ at a relay station $P$.
2. A transmission line passing through checkpoints $D$ and $E$ extends until it intersects the road $AB$ at a relay station $Q$.

To stabilize the network, two synchronization beacons are placed: beacon $M$ is located exactly halfway between relay station $P$ and checkpoint $E$, while beacon $N$ is located exactly halfway between relay station $Q$ and checkpoint $F$.

A technician needs to calculate a specific spatial variance for the beacon $M$. Determine the absolute difference between the square of the distance from the command tower $O$ to beacon $M$ and the square of the distance from the logistics hub $I$ to beacon $M$. Specifically, calculate $|OM^2 - IM^2|$.

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
