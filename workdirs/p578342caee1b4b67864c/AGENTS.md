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

In a remote territory, three observation outposts—Alpha ($A$), Beta ($B$), and Gamma ($C$)—form an acute triangular perimeter. Within this territory, three maintenance stations, $H_1, H_2,$ and $H_3$, are located at the feet of the altitudes from outposts $A, B,$ and $C$ to their respective opposite boundaries. To secure the interior, a circular patrol route (the incircle of $\triangle ABC$) is established, touching the boundaries $BC, AC,$ and $AB$ at checkpoints $T_1, T_2,$ and $T_3$ respectively.

Engineers are designing a secondary triangular inner-perimeter, denoted as $\mathcal{T}$. This perimeter is defined by three laser-fences. The first fence is the reflection of the path $H_1H_2$ across the line connecting checkpoints $T_1$ and $T_2$. The second fence is the reflection of path $H_2H_3$ across the line $T_2T_3$. The third fence is the reflection of path $H_3H_1$ across the line $T_3T_1$. 

The area enclosed by the circular patrol route is exactly $100\pi$ square units. It is observed that the three corners (vertices) of the inner-perimeter $\mathcal{T}$ lie exactly on the path of the circular patrol route. 

If the internal angles of the original outpost triangle are $\alpha = 60^\circ, \beta = 40^\circ,$ and $\gamma = 80^\circ$, calculate the area of the triangular region $\mathcal{T}$ rounded to the nearest integer.

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
