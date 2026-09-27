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

In a specialized logistics hub, high-security cargo is organized into "Shipping Profiles." Each profile consists of a sequence of three specific weight-class ratings $(w_1, w_2, w_3)$, where each rating is a positive whole number.

A logistics manager needs to determine a safety threshold, $n$, for these profiles. This threshold is defined as the smallest number of Shipping Profiles that can be collected such that, no matter which specific ratings are chosen for the profiles, it is guaranteed that there will be a group of exactly three profiles—let’s call them Profile A $(a_1, a_2, a_3)$, Profile B $(b_1, b_2, b_3)$, and Profile C $(c_1, c_2, c_3)$—that satisfy a "Balance Condition."

The Balance Condition is met if the sum of the first ratings $(a_1 + b_1 + c_1)$, the sum of the second ratings $(a_2 + b_2 + c_2)$, and the sum of the third ratings $(a_3 + b_3 + c_3)$ are all exactly divisible by 3.

Find the smallest natural number $n$ that guarantees the existence of such a trio.

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
