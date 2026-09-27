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

In a remote digital library, an automated archivist is tasked with assigning nine unique security clearance levels, represented by the set $\{1, 2, \dots, 9\}$, to nine distinct data terminals labeled $T_1$ through $T_9$. Each terminal must be assigned exactly one unique clearance level from the set such that no two terminals share the same level.

The system’s security protocol imposes the following operational constraints on the assignment process:

(i) The clearance level assigned to $T_1$ must be strictly higher than the level assigned to $T_2$. Additionally, terminal $T_9$ cannot be assigned the highest possible clearance level (Level 9).

(ii) For every terminal $T_i$ in the middle range where $i \in \{3, 4, 5, 6, 7, 8\}$, a "local peak" rule applies: if the clearance level assigned to $T_i$ is strictly greater than all the levels assigned to the preceding terminals ($T_1, T_2, \dots, T_{i-1}$), then the clearance level assigned to the immediately succeeding terminal $T_{i+1}$ must be strictly lower than the level assigned to $T_i$.

How many different valid assignments of clearance levels to terminals satisfy all of these security protocols?

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
