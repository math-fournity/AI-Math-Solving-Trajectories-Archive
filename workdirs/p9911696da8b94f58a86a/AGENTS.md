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

In the city of Metropolia, a specialized industrial engine operates using a core power constant of $a = 120$ units. To maintain the engine's stability, engineers must select a strictly increasing sequence of calibration codes consisting of natural numbers, denoted as $b_1 < b_2 < b_3 < \dots$.

The safety protocol of the engine requires that for any consecutive pair of codes in the sequence, $b_i$ and $b_{i+1}$, three specific diagnostic values must result in perfect squares:
1. The product of the power constant and the current code, plus one: $(a \times b_i) + 1$.
2. The product of the power constant and the next code, plus one: $(a \times b_{i+1}) + 1$.
3. The product of the two codes themselves, plus one: $(b_i \times b_{i+1}) + 1$.

The engineering team has initialized the sequence by setting the first calibration code, $b_1$, to 1. Following the safety protocol to determine the subsequent codes in the sequence, find the value of the third calibration code, $b_3$.

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
