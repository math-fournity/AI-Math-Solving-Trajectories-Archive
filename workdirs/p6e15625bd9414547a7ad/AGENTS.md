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

In a specialized logistics center, there are 9 distinct delivery docks, numbered 1 through 9. There are also 9 unique cargo crates, also numbered 1 through 9.

A supervisor must create a "Dispatch Schedule" (a bijective function $f$) where every dock is assigned exactly one crate, and every crate is assigned to exactly one dock.

In this system, a "Symmetry Error" occurs for a specific number $i$ if the dock numbered $i$ receives a crate with a label other than $i$, and the dock labeled with that crate's number does not receive crate $i$. Specifically, the supervisor looks at the absolute difference between:
1. The label of the crate currently sitting at dock $i$.
2. The number of the dock where crate $i$ has been sent.

A schedule is considered "Highly Unstable" if there exists at least one dock $i \in \{1, 2, 3, \ldots, 9\}$ such that the absolute difference between the label of the crate at dock $i$ and the dock number where crate $i$ was delivered is strictly greater than 1.

How many different "Highly Unstable" Dispatch Schedules can the supervisor create?

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
