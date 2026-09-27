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

In a remote industrial refinery, two engineers, Sarah and Mark, are tasked with decommissioning a massive chemical pressurized vessel. The vessel contains a specific volume of toxic residue, measured in liters. Sarah goes first, and they take turns reducing the volume of the residue.

On each engineer's turn, they must choose exactly one of two extraction protocols:
1.  **The Precision Drain:** Manually siphon exactly 1 liter from the vessel.
2.  **The Centrifuge Flush:** Activate a pump that removes exactly half of the current volume. If the current volume is an odd number, the pump is calibrated to round up the extraction to the nearest whole liter (for example, if 5 liters remain, the pump removes 3 liters, leaving 2).

The engineer who performs the final extraction that brings the vessel’s volume to exactly 0 liters is awarded the safety commendation.

The refinery supervisor presents two different scenarios to test their efficiency:
- **Scenario A:** The vessel starts with exactly 512 liters.
- **Scenario B:** The vessel starts with exactly 513 liters.

Assuming both Sarah and Mark play optimally to win the safety commendation, and Sarah always takes the first turn, which of these two starting volumes—512 or 513—allows Sarah to guarantee a win?

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
