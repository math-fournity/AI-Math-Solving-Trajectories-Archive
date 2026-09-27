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

In a remote territory, three survey outposts—Base $B$, Base $C$, and a central hub $I$—form the vertices of an acute scalene triangle. The hub $I$ serves as the "Incenter" of a larger triangular region $ABC$, where the main boundary is a circular defensive perimeter $\omega$ with a radius of $R$ meters.

A specialized communication relay $H$ is positioned at the orthocenter of the triangular zone $BIC$. This relay $H$ is located within the bounds of the perimeter $\omega$. To support signal transmission, two circular local networks, $\omega_1$ and $\omega_2$, are established: $\omega_1$ is the circle passing through bases $B, H,$ and $I$, while $\omega_2$ is the circle passing through bases $C, H,$ and $I$. Monitoring equipment confirms that these two network circles, $\omega_1$ and $\omega_2$, share an identical radius of $r$ meters.

A mobile command center $\Omega$ is deployed such that its circular footprint is tangent to the main perimeter $\omega$ at a single contact point $N$. Furthermore, the footprint of $\Omega$ is simultaneously tangent to both local network circles $\omega_1$ and $\omega_2$.

Express the radius of the mobile command center $\Omega$ in terms of the perimeter radius $R$ and the network radius $r$.

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
