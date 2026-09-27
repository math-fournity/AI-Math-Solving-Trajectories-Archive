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

In a sprawling agricultural facility, four straight, parallel irrigation pipes—$L_1, L_2, L_3,$ and $L_4$—are laid out on flat ground. The pipes are spaced at perfectly equal intervals. A large square solar-powered greenhouse, $ABCD$, is positioned such that corner $A$ sits exactly atop the first pipe ($L_1$) and the opposite corner $C$ sits exactly atop the fourth pipe ($L_4$).

A small automated sensor, $P$, is dropped at a uniformly random location anywhere inside the interior floor space of the greenhouse. A second sensor, $Q$, is programmed to patrol the perimeter (the four exterior walls) of the greenhouse, and it is currently at a uniformly random position along that boundary.

The facility manager calculates that the probability of sensor $P$ landing in the zone between the two middle pipes ($L_2$ and $L_3$) is exactly $\frac{53}{100}$.

Let the probability that sensor $Q$ is located in the zone between the middle pipes ($L_2$ and $L_3$) be represented by the fraction $\frac{a}{b}$ in lowest terms. Compute the value of $100a + b$.

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
