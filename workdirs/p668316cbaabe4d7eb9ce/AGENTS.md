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

A specialized chemical processing plant operates a triangular cooling rack. The process begins with a top row consisting of $3n$ chemical canisters: exactly $n$ canisters of Reagent A, $n$ canisters of Reagent B, and $n$ canisters of Reagent C, arranged in any order.

A technician creates a second row below the first, containing one fewer canister, by placing a new canister between and below every adjacent pair from the row above. The choice of reagent for the new canister follows two strict safety protocols:
1. If the two canisters directly above it contain the same reagent, the new canister must be filled with that same reagent.
2. If the two canisters directly above it contain different reagents, the new canister must be filled with the third remaining reagent type (e.g., if the pair above is A and B, the new canister must be C).

This layering process continues row by row, with each subsequent row having one less canister than the one above it, until a final row consisting of a single canister is reached. This forms a large downward-pointing triangle of canisters.

Determine all positive integers $n$ such that, regardless of the initial arrangement of the $3n$ canisters in the top row, the three "corner" canisters of the completed triangle—specifically the leftmost canister of the top row, the rightmost canister of the top row, and the single final canister at the bottom vertex—are either all filled with the same reagent or are each filled with a different reagent.

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
