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

In the city-state of Arithmos, a shipment of cargo is classified as a "Royal Parcel" if the first and last digits of its identification number are identical. For example, a parcel with the ID code 4 is a Royal Parcel, as is one with the code 4104; however, a parcel labeled 10 is not.

A Royal Parcel is further distinguished as an "Imperial Parcel" if its identification number can be expressed as the sum of exactly two identification numbers of Royal Parcels. For instance, the ID 101 is an Imperial Parcel because $101 = 99 + 2$ (where both 99 and 2 are Royal Parcels). Similarly, the ID 22 is an Imperial Parcel because $22 = 11 + 11$. However, the ID 561 is not an Imperial Parcel; although $561 = 484 + 77$ (a sum of two Royal Parcels), the number 561 itself is not a Royal Parcel.

The Ministry of Logistics is currently auditing all shipments with 4-digit identification numbers (ranging from 1000 to 9999). Based on these criteria, how many 4-digit identification numbers qualify as Imperial Parcels?

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
