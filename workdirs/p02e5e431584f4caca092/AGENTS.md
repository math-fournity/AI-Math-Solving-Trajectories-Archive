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

A high-tech industrial park is designed as a perfect regular $n$-gon, with a specialized docking station located at each of its $n$ vertices. Initially, $n$ autonomous delivery drones are parked, with exactly one drone at each station.

During a system-wide maintenance cycle, all $n$ drones take off and relocate to the docking stations such that, once again, each station is occupied by exactly one drone.

A "trio" is defined as a specific set of three drones. For any trio, we define two geometric states:
- **State A:** The type of triangle formed by the three stations where the drones were initially parked.
- **State B:** The type of triangle formed by the three stations where the same three drones are parked after the relocation.

Triangle types are classified as acute, right, or obtuse. A trio is considered "stable" if its State A and State B are the same (for example, if they started at stations forming an acute triangle and ended at stations forming an acute triangle).

Let $S$ be the set of all integers $n$ in the range $3 \le n \le 15$ such that, no matter how the $n$ drones are redistributed among the $n$ stations, there must exist at least one stable trio.

Find the sum of all elements in $S$.

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
