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

A specialized waste management facility operates 55 separate decontamination canisters. To ensure chemical stability, the canisters are filled with specific volumes of hazardous liquid: the first canister contains exactly 1 liter, the second contains 2 liters, the third contains 3 liters, and so on, with the 55th canister containing 55 liters.

Two technicians, Alex and Blake, are tasked with emptying these canisters following a strict safety protocol. They take turns performing the extraction, with Alex going first. 

In a single turn, a technician must extract exactly 1 liter of liquid from any canister that is not yet empty. 
- If the liter extracted is the very last liter remaining in a canister (leaving it empty), the technician receives a "Completion Credit" for successfully decommissioning that unit.
- If the liter extracted is not the last liter in that canister, the liquid is simply processed as waste, and no credit is awarded.

The process continues until every canister is completely empty. If Alex plays optimally to maximize his own credits, and Blake plays optimally to minimize Alex's credits, what is the maximum number of Completion Credits that Alex can guarantee he will receive?

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
