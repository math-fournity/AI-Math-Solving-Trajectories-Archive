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

A specialized robotic survey drone is programmed to scout a construction site by following a closed path consisting of $30$ straight-line telemetry legs, $L_1, L_2, \dots, L_{30}$. The path is a continuous loop, where the end of the final leg $L_{30}$ connects perfectly back to the start of the first leg $L_1$, and no three waypoints (vertices where legs meet) lie on the same straight line.

The drone’s navigation system is governed by a strict geometric protocol: at every waypoint where two legs meet, the drone must perform a precise maneuver. Specifically, for every sequence of three consecutive waypoints $W_i, W_{i+1}, W_{i+2}$ (where $W_{31}=W_1$ and $W_{32}=W_2$), the drone must turn such that the interior angle formed at $W_{i+1}$ is exactly $60^\circ$. Furthermore, the drone is hardcoded to always turn in a consistent direction, ensuring that every triangle formed by three consecutive waypoints $W_i, W_{i+1}, W_{i+2}$ is oriented counterclockwise.

As the drone executes this complex, looping $30$-segment path, its trail may cross over itself multiple times on the site map. Based on these geometric constraints, what is the maximum possible number of points where the drone's path can intersect itself?

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
