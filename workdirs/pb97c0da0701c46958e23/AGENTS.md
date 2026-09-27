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

In a remote sector of deep space, a massive circular space station, Sector Gamma, has a radius of 12 units. Nestled entirely within its hull are two smaller, circular research laboratories, Laboratory 1 ($\omega_1$) and Laboratory 2 ($\omega_2$), with radii of 2 and 3 units, respectively. Laboratory 1 is docked flush against the outer hull of Sector Gamma at docking port $X_1$, while Laboratory 2 is docked flush against the hull at docking port $X_2$. The two laboratories do not overlap or touch each other.

A straight supply corridor is constructed such that it is internally tangent to both laboratories, touching the perimeter of Laboratory 1 at a service hatch $T_1$ and Laboratory 2 at a service hatch $T_2$. This corridor extends in both directions until it terminates at two points, $A$ and $B$, on the outer hull of Sector Gamma.

Sensors indicate that the distance between docking port $X_2$ and service hatch $T_2$ is exactly twice the distance between docking port $X_1$ and service hatch $T_1$ ($2 X_1 T_1 = X_2 T_2$).

Calculate the total length of the supply corridor $AB$.

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
