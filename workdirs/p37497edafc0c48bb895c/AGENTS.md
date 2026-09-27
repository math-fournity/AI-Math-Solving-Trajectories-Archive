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

In the remote highlands of a coastal region, three primary radio towers are situated at specific GPS coordinates: Station Alpha ($A$) is located at $(0, 140)$, Station Beta ($B$) is at $(-120, 0)$, and Station Gamma ($C$) is at $(105, 0)$. These towers form a triangular coverage zone with boundary lengths $c$ (between Alpha and Beta), $a$ (between Beta and Gamma), and $b$ (between Gamma and Alpha).

An engineer is tasked with placing a central signal relay hub, point $P$, within the plane of these towers. To ensure signal stability, three specialized monitoring drones are deployed. Each drone—$O_a$, $O_b$, and $O_c$—is programmed to maintain a position that is equidistant from the relay hub $P$ and the two stations defining one side of the triangle (specifically, $O_a$ is equidistant from $P, B,$ and $C$; $O_b$ is equidistant from $P, A,$ and $C$; and $O_c$ is equidistant from $P, A,$ and $B$).

The engineer determines that there is only one specific location for the hub $P$ such that the distances between the drones' positions are perfectly proportional to the lengths of the triangle's boundaries opposite their respective sectors. Specifically, the hub $P$ is positioned such that:
\[ \frac{\text{Distance}(O_a, O_b)}{c} = \frac{\text{Distance}(O_b, O_c)}{a} = \frac{\text{Distance}(O_c, O_a)}{b} \]

Find the precise coordinates $(x, y)$ of this unique relay hub $P$ and calculate the sum of these two coordinates.

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
