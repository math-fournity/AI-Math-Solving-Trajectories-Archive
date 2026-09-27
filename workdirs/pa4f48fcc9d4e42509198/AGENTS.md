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

A specialized deep-sea salvage team is searching for a historic shipwreck located in one of three underwater sectors: Sector A (West), Sector B (Center), or Sector C (East). To locate the wreck, the team can deploy two types of sonar pings: a "West-Ping" to check if the wreck is in Sector A, or an "East-Ping" to check if it is in Sector C. 

The sonar system is faulty due to extreme pressure. For every ping sent, the terminal returns a reading of "Present" or "Absent," but the system is known to provide a false reading (a lie) at most 10 times throughout the entire mission. 

The mission commander must program the total number of pings into the automated drone's hardware before it launches. While the commander can choose which specific type of ping (West or East) to send based on the results of previous pings during the mission, the total quantity of pings must be declared in advance.

What is the minimum number of pings the commander must declare to guaranteed they will know exactly which of the three sectors contains the shipwreck?

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
