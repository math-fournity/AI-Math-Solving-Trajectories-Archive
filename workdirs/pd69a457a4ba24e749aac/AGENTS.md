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

An elite espionage agency employs $n$ undercover agents (where $n \ge 3$), each assigned a unique numerical clearance level from 1 to $n$. A high-ranking Director knows the full hierarchy of these agents but keeps it strictly confidential. 

An independent Auditor is tasked with verifying a chain of command. The Auditor is permitted to conduct several inquiries. For each inquiry, the Auditor selects exactly three agents and presents their names to the Director. The Director then reviews their files and discloses the identity of either the highest-ranking agent among those three or the lowest-ranking agent among those three, choosing which of these two pieces of information to reveal at their own discretion.

The Auditor’s goal is to establish a definitive "Reporting Chain," which is a sequence of agents $S_{1}, S_{2}, \dots, S_{N}$ such that the clearance level of agent $S_i$ is strictly higher than the clearance level of agent $S_{i+1}$ for all $1 \le i < N$.

Given that the Director will always provide the least helpful information possible to minimize the length of the chain the Auditor can guarantee, find the maximum value of $N$ that the Auditor can definitely determine regardless of the underlying clearance levels or the Director's choices.

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
