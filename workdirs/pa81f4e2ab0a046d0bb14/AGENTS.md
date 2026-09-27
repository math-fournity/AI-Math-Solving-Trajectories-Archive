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

A specialized chemical processing plant operates with 36 distinct canisters of gas. These canisters are categorized into 4 different elemental groups (Hydrogen, Helium, Argon, and Neon), with 9 unique pressure levels (levels 1 through 9) represented in each group.

An engineer, Dr. Aris, selects any 18 canisters to use for her experiments, leaving the remaining 18 canisters to her colleague, Dr. Boris. The experiment proceeds in 18 discrete phases. In each phase, Dr. Aris first selects one of her canisters and opens it into a testing chamber. Immediately after, Dr. Boris must select one of his canisters and open it into the same chamber.

If the two canisters released in a single phase share either the same elemental group or the same pressure level, a reaction occurs that produces a "stability unit." Dr. Aris aims to minimize these reactions through her choice of canisters and the order in which she releases them. Dr. Boris aims to maximize the number of stability units produced.

What is the maximum number of stability units Dr. Boris can guarantee he will produce, regardless of which 18 canisters Dr. Aris initially chooses or the order in which she releases them?

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
