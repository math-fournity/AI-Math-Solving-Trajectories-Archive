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

A specialized logistics firm is tasked with distributing exactly 1 ton of a highly volatile chemical across $2n$ individual storage canisters (where $n$ is an integer and $n \ge 2$). The manager, Betya, must first decide the specific mass of chemical to be placed in each canister, $x_1, x_2, \dots, x_{2n}$, such that the total sum of these non-negative masses is exactly 1.

Once these masses are determined, the safety inspector, Vasya, takes these $2n$ canisters and arranges them in a circular containment ring. After the canisters are positioned, Vasya identifies the "risk factor" for every pair of adjacent canisters. The risk factor for any two neighboring canisters is defined as the product of their chemical masses. Vasya then records the highest risk factor found anywhere in the circle.

Betya’s objective is to choose the masses in such a way that the final recorded risk factor is as large as possible, regardless of how Vasya arranges them. Conversely, Vasya will always arrange the canisters in the circle to ensure that the highest risk factor is as small as possible. 

Assuming both Betya and Vasya play optimally according to their respective goals, what value will be recorded on the board?

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
