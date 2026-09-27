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

In a remote industrial zone, a specialized chemical reactor is powered by four primary catalysts, denoted as $a, b, c,$ and $d$. Due to strict safety protocols, these catalysts must be balanced such that the sum of their squared concentrations satisfies the equilibrium equation $a^2 + b^2 + c^2 + d^2 = 2$, where each concentration is a non-negative value.

The efficiency of the reaction is determined by comparing the "Interaction Index" to the "Catalytic Synergy." 

The Interaction Index is calculated by summing the products of every possible pair of catalysts and subtracting a constant stabilization factor of 1:
$(ab + bc + cd + da + ac + bd) - 1$.

The Catalytic Synergy is calculated by summing the products of every possible triplet of catalysts:
$(abc + abd + acd + bcd)$.

A safety engineer needs to determine a universal safety constant $k$ such that the Interaction Index never exceeds $k$ times the Catalytic Synergy, regardless of the specific concentrations of the four catalysts (provided they meet the equilibrium requirement).

Find the least real number $k$ such that the inequality:
$ab + bc + cd + da + ac + bd - 1 \leq k(abc + abd + acd + bcd)$
is guaranteed to hold true for all valid catalyst concentrations.

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
