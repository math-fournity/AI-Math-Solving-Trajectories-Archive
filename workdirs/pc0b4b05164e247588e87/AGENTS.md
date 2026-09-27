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

In a specialized logistics hub, a technician is tasking with organizing several rectangular shipping containers in a high-density storage bay. To ensure stability while maintaining specific access corridors, the containers—all oriented with their edges perfectly aligned to the warehouse's North-South, East-West, and Up-Down axes—must be positioned according to a strict connectivity protocol.

Let $n$ be the total number of containers, labeled $P_1, P_2, \ldots, P_n$. The safety requirements dictate a specific pattern of physical contact: 

1. Every container $P_i$ must have a non-zero volume of intersection (overlap or touching) with every other container in the set, with exactly two exceptions.
2. The exceptions for container $P_i$ are its immediate neighbors in the numerical sequence: $P_{i-1}$ and $P_{i+1}$. These two containers must not have any points in common with $P_i$.
3. This sequence is cyclical, meaning $P_1$ cannot touch $P_n$ or $P_2$, and $P_n$ cannot touch $P_{n-1}$ or $P_1$.

Determine the maximum possible number of containers $n$ that can be arranged in the storage bay under these spatial constraints.

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
