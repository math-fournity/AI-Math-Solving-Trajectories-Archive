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

In a specialized laboratory, a chemist is working with a set of $n$ distinct chemical vials, where $n$ is an integer such that $2 \le n \le 100$. Each vial is labeled with a unique integer ID from 1 to $n$. Furthermore, each vial currently contains a solution that is either "Type-B" or "Type-W."

The chemist can perform a "Reaction" between any two vials under one strict condition: the vials must have different IDs and contain different types of solutions. When a Reaction occurs, the vial with the numerically smaller ID has its contents discarded and replaced with a solution identical in type to the one in the vial with the larger ID. 

A "Protocol" is a sequence of such Reactions that continues until no further Reactions are possible (meaning every remaining vial in the set either contains the same type of solution or has the same ID, though the latter is impossible by the rules of the set).

Let $L_n$ represent the maximum possible number of Reactions that can occur in any Protocol, starting from any possible initial distribution of Type-B and Type-W solutions across the $n$ vials and ending at any valid terminal state.

Calculate the sum of $L_n$ for all values of $n$ from 2 to 100.

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
