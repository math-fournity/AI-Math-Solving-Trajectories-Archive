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

A circular high-security server farm contains $n$ server racks arranged in a perfect ring. A technician is tasked with assigning unique ID badges, labeled $1, 2, 3, \dots, n$, to these racks, placing exactly one badge on each rack.

The "System Stress Level" ($S$) of the configuration is calculated by taking the numerical difference between the IDs of every pair of adjacent racks in the circle and summing these absolute values together (this includes the difference between the first and the last rack in the ring).

For any given $n$, let $M(n)$ represent the maximum possible System Stress Level that can be achieved by arranging the badges optimally. Furthermore, let $C(n)$ represent the total number of distinct ways to arrange the badges $1, 2, \dots, n$ such that the resulting sum $S$ is exactly equal to $M(n)$. (Note: Two arrangements are considered different if the ID assigned to at least one specific physical rack location differs; rotations and reflections are counted as distinct arrangements).

Calculate the final value of:
$M(10) + M(11) + C(4) + C(5)$

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
