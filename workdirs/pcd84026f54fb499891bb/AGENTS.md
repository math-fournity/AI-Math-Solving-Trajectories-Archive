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

A prestigious museum has a "Top 30" gallery wall featuring 30 historical artifacts, each assigned a preservation value. Currently, the wall displays 30 artifacts with values of $30, 29, 28, \ldots, 1$. 

The museum curator has a rule for updating the wall: when a new artifact is donated, its value is compared to the current lowest value on the wall. If the new artifact’s value is strictly greater than the lowest value, it is added to the wall and the artifact with the lowest value is permanently removed. If the new artifact’s value is equal to the lowest value on the wall, the most recently added artifact (the newcomer) is the one removed. In the ranking system, a new artifact "surpasses" or displaces only those existing items that have a strictly lower value.

A local collector intends to donate a series of new artifacts, one at a time. Each time they donate an item, it is guaranteed to be valuable enough to make it onto the wall (meaning its value will always be higher than the current minimum). 

What is the minimum number of artifacts the collector must donate to ensure that every single one of the 30 spots on the wall is occupied by an artifact from their personal collection?

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
