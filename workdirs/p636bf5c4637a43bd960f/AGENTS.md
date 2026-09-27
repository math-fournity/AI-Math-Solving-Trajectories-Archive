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

A specialized laboratory is testing the durability of 20 different alloy samples, labeled $S = \{x_1, x_2, \dots, x_{20}\}$. Each sample has been assigned a "wear-resistance coefficient" measured as a real number within the continuous range $[0, 1]$.

For a specific stress-test simulation, the engineers must divide all 20 samples into two distinct testing chambers:
- **Chamber A** receives exactly 9 samples.
- **Chamber B** receives the remaining 11 samples.

The laboratory defines a configuration as "Balanced" if the difference between the average wear-resistance of the samples in Chamber A and the average wear-resistance of the samples in Chamber B does not exceed a tolerance threshold of $\frac{20}{198}$. Specifically, a subset of 9 samples $A$ is Balanced if:
$$ \left| \frac{1}{9} \sum_{x_i \in A} x_i - \frac{1}{11} \sum_{x_j \in S \setminus A} x_j \right| \leq \frac{20}{198} $$

Regardless of the specific values assigned to the 20 coefficients in the set $S$, there is a guaranteed minimum number of ways to choose a 9-element subset $A$ that satisfies this Balanced condition. 

Calculate $N$, the minimum possible number of such Balanced 9-element subsets.

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
