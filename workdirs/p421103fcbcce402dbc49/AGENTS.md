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

In a specialized optics laboratory, a laser emitter is positioned at a fixed point $P$. Two robotic sensors, initially named $M_0$ and $N_0$, are placed such that the distances from the emitter to each sensor are equal ($M_0 P = N_0 P$). The sensors and the emitter form a triangular field of view $M_0 N_0 P$, where the angle at the emitter vertex $P$ is exactly $\alpha$ degrees.

The lab technician performs a sequence of 5 distance adjustments. For any current configuration of sensors $M_i$ and $N_j$ (where $i$ and $j$ are the number of adjustments made to each respective sensor), the technician can perform one of two operations:

- **Type-M Adjustment:** The sensor $M_i$ is moved further away from $P$ along the line $PM_i$ to a new position $M_{i+1}$. The displacement $M_i M_{i+1}$ must exactly equal the current straight-line distance between the two sensors, $M_i N_j$.
- **Type-N Adjustment:** The sensor $N_j$ is moved further away from $P$ along the line $PN_j$ to a new position $N_{j+1}$. The displacement $N_j N_{j+1}$ must exactly equal the current straight-line distance between the two sensors, $M_i N_j$.

After exactly 5 adjustments are completed, where $k$ of them were Type-M adjustments and the remaining $5-k$ were Type-N adjustments, the technician observes that the final triangle formed by the emitter and the two sensors, $M_k N_{5-k} P$, is once again an isosceles triangle.

Given that $10\alpha$ is an integer, find the value of $10\alpha$.

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
