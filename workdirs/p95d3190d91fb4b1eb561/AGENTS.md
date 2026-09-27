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

In a digital signal processing laboratory, a team of engineers is studying "Complexity Ratings." For any positive integer signal strength $k$, the Complexity Rating $S(k)$ is defined as the sum of the digits of its decimal representation.

The laboratory is testing a new compression algorithm characterized by a "Efficiency Factor" $\beta$, where $\beta$ is a rational number such that $0 < \beta < 1$. A sequence of $n$ primary data packets with integer strengths $a_1, a_2, \dots, a_n$ is said to be "$\beta$-Harmonized" if, for every possible sub-collection of at least two packets, the Complexity Rating of the sum of their strengths is exactly equal to $\beta$ times the sum of their individual Complexity Ratings. Formally, for any subset of indices $I \subseteq \{1, 2, \dots, n\}$ with $|I| \ge 2$, the following condition must be met:
$$ S\left(\sum_{i \in I} a_i\right) = \beta \sum_{i \in I} S(a_i). $$

The engineers want to determine the limits of this architecture. They are searching for the largest possible integer $N \ge 2$ such that, regardless of which rational Efficiency Factor $\beta \in (0, 1)$ is chosen, it is always possible to find a set of $N$ positive integer strengths $a_1, a_2, \dots, a_N$ that are $\beta$-Harmonized.

Find the value of $N$.

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
