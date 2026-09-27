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

In a specialized logistics warehouse, there are seven designated storage bays arranged in a row. A shipment of seven high-priority crates arrives, each labeled with a specific department code: A, L, G, E, B, R, and A. Note that the two crates labeled "A" are identical and interchangeable in every respect.

Originally, the crates were intended to be placed in the bays such that they spelled the word "ALGEBRA" from left to right. However, due to a system error, the warehouse manager must now reorganize the crates according to a strict "total displacement" protocol. 

The protocol requires that every single crate must be placed in a bay that does not match its original intended label. For example, the crate originally destined for the first bay (an "A") cannot be placed in the first bay, and the crate originally destined for the seventh bay (the other "A") cannot be placed in the seventh bay. Because the two "A" crates are indistinguishable, it does not matter which "A" was originally assigned to which "A" bay; the only constraint is that no bay receives a crate matching its original letter assignment.

How many unique ways can the crates be distributed among the seven bays such that no bay contains its original letter?

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
