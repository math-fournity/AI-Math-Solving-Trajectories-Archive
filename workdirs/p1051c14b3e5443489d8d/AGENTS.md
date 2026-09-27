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

In a specialized logistics warehouse, a grid-based storage floor is organized into $m$ horizontal rows and $n$ vertical aisles. To monitor inventory, certain intersections (cells) of these rows and aisles are equipped with high-tech red sensors.

A configuration of sensors is considered "unstable" if it contains a "Data Loop." A Data Loop is defined as a sequence of $2r$ distinct sensors ($a_1, a_2, \ldots, a_{2r}$) where $2r \ge 4$, satisfying two conditions:
1. For every index $k \in \{1, \ldots, 2r\}$, sensor $a_k$ and sensor $a_{k+1}$ are positioned on the same diagonal line (where $a_{2r+1} = a_1$).
2. For every index $k \in \{1, \ldots, 2r\}$, sensor $a_k$ and sensor $a_{k+2}$ are NOT positioned on the same diagonal line (where $a_{2r+2} = a_2$).

Note: Two sensors are on the same diagonal if the line connecting their centers forms a $45^\circ$ angle with the aisles.

Determine, in terms of $m$ and $n$, the maximum number of red sensors that can be installed on the $m \times n$ grid such that no Data Loop exists.

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
