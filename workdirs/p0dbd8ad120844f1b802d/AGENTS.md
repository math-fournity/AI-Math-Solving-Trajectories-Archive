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

A specialized waste management company operates 10 identical silos, each initially containing 10 tons of hazardous material. Two technicians, the Supervisor and the Operator, must process this material according to strict security protocols. 

The following three-step sequence constitutes one complete work cycle:

1. **Extraction and Allocation:** The Operator extracts exactly 1 ton of material from every active silo currently in the facility. The Supervisor, who cannot see the silos, dictates exactly how the Operator must redistribute this total gathered tonnage back into the active silos (non-integer amounts are not allowed).

2. **Decontamination and Reporting:** After the redistribution, the Operator reports the exact tonnage currently stored in each silo to the Supervisor. Immediately following this report, any silo that contains 0 tons of material is permanently decommissioned and removed from the facility.

3. **Security Shuffling:** The Operator secretly swaps the physical positions of two remaining silos. The Supervisor is informed that a swap occurred but is not told which two silos were moved.

The Supervisor’s goal is to strategically dictate the allocations in Step 1 so that, after a finite number of work cycles, a specific number of silos are guaranteed to be decommissioned, regardless of the Operator’s secret shuffling choices.

Based on these protocols, find the maximum number of silos $n$ that the Supervisor can guarantee will be destroyed.

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
