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

In a specialized laboratory, a sensitive thermal sensor is used to identify a single defective microchip from a batch of $N$ identical-looking chips. The defective chip is known to be slightly colder than the functional ones. 

The sensor operates as a differential comparator: you place an equal number of chips on two thermal pads, and the sensor indicates which side contains the colder (defective) chip. However, this sensor has a critical "double-fault" structural flaw. If the sensor ever tilts to indicate an imbalance (meaning the defective chip is present on one of the pads), it sustains internal damage. If the sensor is forced to indicate an imbalance for a second time, it fuses shut and becomes permanently inoperable. If the pads are balanced, the sensor remains perfectly intact.

You are permitted a total of $k=10$ measurement attempts to isolate the defective chip. If the sensor breaks before you find the chip, the mission fails. 

What is the largest possible number of chips $N$ in the batch such that you can guaranteed-ly identify the single colder defective chip within $10$ attempts without breaking the sensor more than once?

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
