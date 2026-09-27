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

In the high-tech logistics hub of Prime-Net, two distinct security servers, Server $p$ and Server $q$, are assigned specific encryption keys that must always be prime numbers. For the network to remain synchronized, the keys must satisfy two strict structural protocols:

1. When the value of Server $q$’s key is multiplied by 30 and then reduced by 1, the resulting total must be perfectly divisible by the value of Server $p$’s key.
2. Conversely, when the value of Server $p$’s key is multiplied by 30 and then reduced by 1, that resulting total must be perfectly divisible by the value of Server $q$’s key.

A configuration of keys $(p, q)$ is considered "Stable" only if both protocols are met simultaneously. Let $S$ be the complete set of all such unique Stable pairs of prime keys. 

Calculate the total sum of all individual key values across every pair in $S$. (For example, if the only Stable pairs were $(2, 3)$ and $(5, 7)$, the required sum would be $2+3+5+7$).

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
