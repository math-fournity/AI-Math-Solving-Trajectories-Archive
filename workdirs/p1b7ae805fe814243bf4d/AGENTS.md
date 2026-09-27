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

In a circular research facility, four observation hubs are located at positions $A$, $C$, $D$, and $B$ along the outer perimeter $\omega$. A straight service tunnel connects hub $A$ and hub $B$. The straight-line distances between the other hubs are recorded as follows: the distance from $C$ to $A$ is 5 units, from $C$ to $D$ is 6 units, and from $D$ to $B$ is 7 units.

An analyst notices a specific phenomenon involving a signal transmitter located at a point $P$ on the perimeter $\omega$. When a signal is sent from $P$ to $C$, it crosses the $AB$ tunnel at a junction $P_1$. When a signal is sent from $P$ to $D$, it crosses the $AB$ tunnel at a junction $P_2$. Measurements show that $P_1$ is located 3 units from $A$, while $P_2$ is located 4 units from $B$. In this configuration, $P$ is the only point on the perimeter that produces these specific junction points $P_1$ and $P_2$.

Later, a second transmitter is placed at a different point $Q$ on the perimeter $\omega$. Signals from $Q$ to $C$ and $Q$ to $D$ cross the $AB$ tunnel at junctions $Q_1$ and $Q_2$, respectively. It is observed that $Q_1$ is positioned further along the tunnel toward $B$ than $P_1$ is. Furthermore, the distance along the tunnel between the junctions $P_2$ and $Q_2$ is exactly 2 units. In this configuration, $Q$ is the unique point on the perimeter satisfying these signal intersections.

The distance between the junctions $P_1$ and $Q_1$ can be expressed as a simplified fraction $\frac{p}{q}$. Find the value of $p+q$.

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
