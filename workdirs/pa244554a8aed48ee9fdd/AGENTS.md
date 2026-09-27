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

In the high-tech logistics hub of Sector 28, there are exactly 28 unique docking bays, indexed by their ID numbers from 1 to 28. A specialized security protocol requires the formation of "Secure Squadrons." A Secure Squadron is defined as a collection of $k$ distinct docking bays where the ID numbers of every pair of bays in the collection share no common factors other than 1 (i.e., the IDs are pairwise coprime).

The central computer, $T(k)$, is programmed to calculate the total number of unique ways to form a Secure Squadron of exactly size $k$. 

Due to a system upgrade, the lead engineer needs to determine the cumulative sum of all possible Secure Squadrons that can be formed for every possible squadron size greater than one. Specifically, you must calculate the total value of:
$T(2) + T(3) + T(4) + T(5) + T(6) + T(7) + T(8) + T(9) + T(10) + T(11) + T(12)$

Find the final numerical value of this sum.

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
