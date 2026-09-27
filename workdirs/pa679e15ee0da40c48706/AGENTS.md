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

A specialized telecommunications network is established between three major data hubs: Hub A, Hub B, and Hub C. The fiber-optic cables connecting them form a right-angled triangle, where the connection between Hub B and Hub C is a straight line of length 4 units. The angle at Hub A is $90^\circ$, while the angles at Hub B and Hub C are $60^\circ$ and $30^\circ$, respectively.

A central server, $I$, is positioned at the incenter of this network. It connects to the cables $BC, CA,$ and $AB$ at the nearest points $A_0, B_0,$ and $C_0$, respectively. To ensure redundancy, three circular backup zones are established: $\omega_A$ (the circle passing through $B_0, I, C_0$), $\omega_B$ (the circle passing through $C_0, I, A_0$), and $\omega_C$ (the circle passing through $A_0, I, B_0$).

Engineers then define three secondary signal territories:
1. Territory $T_A$: Formed by point $A_0$ and two additional relay points, $A_1$ and $A_2$. $A_1$ is the second intersection of the line $A_0B_0$ with circle $\omega_B$, and $A_2$ is the second intersection of the line $A_0C_0$ with circle $\omega_C$.
2. Territory $T_B$: Formed by point $B_0$ and two additional relay points, $B_1$ and $B_2$. $B_1$ is the second intersection of the line $B_0C_0$ with circle $\omega_C$, and $B_2$ is the second intersection of the line $B_0A_0$ with circle $\omega_A$.
3. Territory $T_C$: Formed by point $C_0$ and two additional relay points, $C_1$ and $C_2$. $C_1$ is the second intersection of the line $C_0A_0$ with circle $\omega_A$, and $C_2$ is the second intersection of the line $C_0B_0$ with circle $\omega_B$.

If the total combined area of these three signal territories ($T_A, T_B,$ and $T_C$) is expressed in the form $\sqrt{m}-n$, where $m$ and $n$ are positive integers, find the value of $m+n$.

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
