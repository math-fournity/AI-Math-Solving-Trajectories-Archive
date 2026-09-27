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

A specialized logistics company manages a high-tech warehouse represented by a $50 \times 50$ grid of storage sectors. The company is testing "Climate-Control Units" (CCUs) to regulate the thermal energy across the entire facility. 

The engineers define a "Configuration Case" as a pair of positive integers $(n, k)$, where $1 \leq k \leq n \leq 50$. For each case, they attempt to assign a specific real-number energy value to every $1 \times 1$ sector within an $n \times n$ subsection of the warehouse. A configuration is considered "Energetically Paradoxical" if it satisfies two conditions:
1. The total sum of energy values across all $n^2$ sectors in the $n \times n$ subsection is strictly positive.
2. The sum of energy values within every possible $k \times k$ contiguous block of sectors inside that $n \times n$ subsection is strictly negative.

Let $S$ be the set of all possible pairs $(n, k)$ that allow for at least one Energetically Paradoxical configuration to exist. 

Calculate the total number of unique pairs in set $S$.

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
