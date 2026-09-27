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

In a remote industrial facility, three specialized technicians—Alpha, Beta, and Gamma—operate a high-precision calibration machine. The machine requires exactly two technicians to operate it at all times, while the third technician rests and monitors the diagnostics. 

The protocol for shifts is strictly regulated: the two technicians who just completed a calibration cycle are evaluated, and the one who recorded the lower efficiency score must take the rest role for the very next cycle. The technician who was previously resting then steps in to replace them, working alongside the technician who recorded the higher efficiency score.

Records indicate the following cumulative activity levels:
- In Scenario 1, Technician Alpha worked a total of 10 cycles and Technician Beta worked a total of 10 cycles. Let $f(10, 10)$ be the minimum number of cycles Technician Gamma could have worked.
- In Scenario 2, Technician Alpha worked a total of 15 cycles and Technician Beta worked a total of 20 cycles. Let $f(15, 20)$ be the minimum number of cycles Technician Gamma could have worked.
- In Scenario 3, Technician Alpha worked a total of 25 cycles and Technician Beta worked a total of 30 cycles. Let $f(25, 30)$ be the minimum number of cycles Technician Gamma could have worked.

Calculate the sum: $f(10, 10) + f(15, 20) + f(25, 30)$.

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
