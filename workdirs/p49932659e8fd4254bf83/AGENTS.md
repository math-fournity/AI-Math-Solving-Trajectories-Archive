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

In a specialized chemistry laboratory, a technician named Elena is presented with 100 sealed vials of a rare liquid catalyst. She is informed that each vial contains a different discrete volume of the catalyst: one vial contains exactly 1 milliliter, another contains 2 milliliters, and so on, up to the 100th vial which contains 100 milliliters. However, the vials are unlabelled and identical in appearance.

To extract the catalyst, Elena must use a precision automated extractor. For each vial, she must program the extractor to withdraw a specific, fixed volume of liquid. 
- If the vial contains at least the volume she programs, the extractor successfully withdraws exactly that requested amount into a collection beaker.
- If the vial contains less than the programmed volume, the extractor fails to withdraw any liquid at all.
- Regardless of whether the extraction is successful or not, the process contaminates the remaining contents of the vial and the vial itself, rendering them unusable for any further attempts. 

Elena does not have a gauge to see how much liquid was originally in any vial; she only knows how much she successfully collected in her beaker. What is the maximum total volume of catalyst, in milliliters, that Elena can guaranteed to collect?

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
