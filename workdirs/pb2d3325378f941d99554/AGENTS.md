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

A specialized laboratory is testing the durability of three different industrial coatings—Alloy-X, Boron-Y, and Carbon-Z—on a batch of 300 steel plates. To qualify for a high-performance certification in the first round of testing, a coating must be rated as "Superior" on at least 127 individual plates.

The laboratory technicians have already processed the first 200 plates. The results show that Alloy-X was rated Superior on 90 plates, Boron-Y was rated Superior on 60 plates, and Carbon-Z was rated Superior on 40 plates. Additionally, 10 plates were discarded due to surface defects and received no rating.

The technicians are now preparing to rate the remaining 100 plates. Each of these plates will be assigned exactly one of three possible outcomes: a rating for Alloy-X, a rating for Boron-Y, or a rating for Carbon-Z. Unlike the first batch, the technicians will ensure there are no discarded or invalid plates in this final group.

In how many distinct ways can the ratings for the final 100 plates be distributed among the three coatings such that Alloy-X reaches the threshold to earn the high-performance certification?

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
