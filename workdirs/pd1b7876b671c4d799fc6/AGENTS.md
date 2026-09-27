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

A logistics company is designing a high-tech square warehouse, denoted by the corners $A, B, C$, and $D$ in clockwise order. Inside this warehouse, a single automated picking robot is located at a specific point $P$. 

The warehouse is divided into four triangular zones based on the robot's location: Zone 1 (defined by the robot and the wall $AB$), Zone 2 (the robot and wall $BC$), Zone 3 (the robot and wall $CD$), and Zone 4 (the robot and wall $DA$). The maintenance cost of each zone is directly proportional to its floor area.

To ensure operational efficiency, the company requires that for any possible position of the robot $P$ within the interior of the warehouse, there must exist at least two distinct zones such that the ratio of their areas (larger area divided by smaller area) is no greater than a specific threshold $a$.

Determine the smallest possible real number $a > 1$ such that, regardless of where the robot $P$ is placed, one can always find a pair of zones whose area ratio $R$ satisfies the constraint:
$$\frac{1}{a} \le R \le a$$

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
