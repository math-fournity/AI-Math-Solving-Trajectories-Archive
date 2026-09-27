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

In a specialized optics laboratory, a laser source is positioned at a fixed point $P$. Two robotic sensors, $M$ and $N$, are initially placed at positions $M_0$ and $N_0$ such that the distances from the source are equal ($PM_0 = PN_0$). The two sensors and the source form a configuration where the angle $\angle M_0PN_0$ is exactly $\alpha$ degrees.

The laboratory operates under a specific protocol for adjusting the sensors' distances from the source. At any step, if the current positions of the sensors are $M_i$ and $N_j$, a technician can perform one of two "calibration shifts":
- An **M-shift**: Sensor $M$ is moved further away from the source $P$ along the line $\vec{PM_i}$ to a new position $M_{i+1}$. The distance of this shift, $M_iM_{i+1}$, must exactly equal the current straight-line distance between the two sensors, $M_iN_j$.
- An **N-shift**: Sensor $N$ is moved further away from the source $P$ along the line $\vec{PN_j}$ to a new position $N_{j+1}$. The distance of this shift, $N_jN_{j+1}$, must exactly equal the current straight-line distance between the two sensors, $M_iN_j$.

A technician performs a total of 5 calibration shifts. Out of these 5 shifts, exactly $k$ shifts were M-shifts, and the remaining $5-k$ shifts were N-shifts. At the end of these 5 operations, the technician records the final positions as $M_k$ and $N_{5-k}$. 

It is observed that in this final configuration, the distances from the source to the two sensors are once again equal, making the triangle formed by $M_k, N_{5-k},$ and $P$ an isosceles triangle ($PM_k = PN_{5-k}$). 

Given that $10\alpha$ is an integer, compute the value of $10\alpha$.

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
