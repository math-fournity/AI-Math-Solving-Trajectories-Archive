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

In a remote industrial complex, three chemical compounds—Alpha ($a$), Beta ($b$), and Gamma ($c$)—are stored in pressurized tanks. The volumes of these compounds are positive real quantities measured in liters.

The facility operates under a strict equilibrium safety protocol. The interaction between the three storage levels is governed by the "Root-Product Constant." Specifically, the product of the following three efficiency factors must exactly equal 1:
1. The square root of the product of Alpha and Beta, minus 1.
2. The square root of the product of Beta and Gamma, minus 1.
3. The square root of the product of Gamma and Alpha, minus 1.

The plant's engineers are monitoring six specific "pressure differentials" within the piping system, defined by the following formulas:
- The volume of Alpha minus the ratio of Beta to Gamma ($a - b/c$)
- The volume of Alpha minus the ratio of Gamma to Beta ($a - c/b$)
- The volume of Beta minus the ratio of Alpha to Gamma ($b - a/c$)
- The volume of Beta minus the ratio of Gamma to Alpha ($b - c/a$)
- The volume of Gamma minus the ratio of Alpha to Beta ($c - a/b$)
- The volume of Gamma minus the ratio of Beta to Alpha ($c - b/a$)

If a pressure differential exceeds a value of 1, a warning light is triggered. Based on the equilibrium safety protocol, what is the maximum possible number of these six pressure differentials that can be greater than 1?

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
