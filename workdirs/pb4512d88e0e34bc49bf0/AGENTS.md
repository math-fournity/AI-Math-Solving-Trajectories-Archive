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

One of Michael's responsibilities in organizing the family vacation is to call around and find room rates for hotels along the root the Kubik family plans to drive.  While calling hotels near the Grand Canyon, a phone number catches Michael's eye.  Michael notices that the first four digits of $987-1234$ descend $(9-8-7-1)$ and that the last four ascend in order $(1-2-3-4)$.  This fact along with the fact that the digits are split into consecutive groups makes that number easier to remember.

Looking back at the list of numbers that Michael called already, he notices that several of the phone numbers have the same property: their first four digits are in descending order while the last four are in ascending order.  Suddenly, Michael realizes that he can remember all those numbers without looking back at his list of hotel phone numbers.  "Wow," he thinks, "that's good marketing strategy."

Michael then wonders to himself how many businesses in a single area code could have such phone numbers.  How many $7$-digit telephone numbers are there such that all seven digits are distinct, the first four digits are in descending order, and the last four digits are in ascending order?

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
