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

In a remote mining district, two industrial excavators, Model A and Model B, were evaluated over a 48-hour operation. By the end of the evaluation, each machine had processed a total of 500 metric tons of raw ore.

On the first day, Model A processed 300 tons and successfully extracted 160 units of high-grade mineral. On the second day, Model A processed the remaining 200 tons and extracted 140 units.

Model B followed a different schedule. On the first day, it processed a quantity of ore that was not equal to 300 tons. On the second day, it processed the remainder of its 500-ton quota. For each of the two days, Model B’s mineral yield was a positive integer. Furthermore, Model B’s "extraction efficiency" (units extracted divided by tons processed) was strictly lower than Model A’s efficiency on each respective day.

While Model A achieved an overall two-day extraction ratio of 300/500 (or 3/5), Model B’s designers aimed to maximize its total two-day efficiency despite being less efficient than Model A on each individual day. The largest possible two-day extraction ratio Model B could have achieved is expressed as the simplified fraction $m/n$, where $m$ and $n$ are relatively prime positive integers.

What is the value of $m+n$?

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
