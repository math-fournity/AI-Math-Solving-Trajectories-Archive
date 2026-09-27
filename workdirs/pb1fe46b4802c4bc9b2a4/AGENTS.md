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

In a remote industrial distillation complex, chemical engineers organize pressurized canisters in a downward-stacking triangular formation. A "Stable Configuration" is defined as a setup where every canister in the array contains a unique, positive integer volume of catalyst (in liters), and every canister located below the top row contains a volume exactly equal to the quotient of the two volumes directly above it.

For example, a configuration with two canisters in the top row containing 42 and 7 liters would have a single canister below them containing 6 liters (since $42/7=6$), provided all three volumes are distinct.

The Chief Engineer is designing a massive four-tier configuration, which begins with a top row of 4 canisters, followed by a row of 3, then a row of 2, and finally a single canister at the bottom. 

To minimize equipment costs, the team needs to find the smallest possible value for the largest single volume of catalyst present anywhere within such a 10-canister Stable Configuration.

Find the smallest positive integer that can occur as the greatest element in a Stable Configuration with four canisters in the top row.

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
