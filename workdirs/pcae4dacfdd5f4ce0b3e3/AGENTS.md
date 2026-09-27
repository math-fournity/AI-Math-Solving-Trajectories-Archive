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

In a sprawling digital metropolis, a data architect is analyzing two distinct sequences of server clusters, indexed from $n = 2$ to $n = 1,000,000$. 

For any cluster ID $n$, the architect defines a "Critical Security Key," denoted as $f(n)$, which is equivalent to the largest prime factor of that ID. 

The architect needs to compare the total security complexity of two massive databases:
1.  The first database consists of the Security Keys for a transformed sequence, where each entry is calculated as $f(n^2 - 1)$ for every $n$ in the range.
2.  The second database consists of the Security Keys for the standard sequence, calculated as $f(n)$ for every $n$ in the same range.

The architect calculates the "Network Efficiency Ratio" by dividing the sum of the keys in the first database by the sum of the keys in the second database. To normalize this ratio for the system's dashboard, the architect multiplies the result by $10,000$ and takes the floor of the final value (the greatest integer less than or equal to the result).

Let $N$ be this final integer:
\[ N = \left\lfloor 10,000 \cdot \frac{\sum_{n=2}^{1,000,000} f(n^2 - 1)}{\sum_{n=2}^{1,000,000} f(n)} \right\rfloor \]

Your task is to provide an estimate $E$ for the value of $N$. Your score for this task will be determined by the precision of your estimate according to the following formula:
\[ \text{Score} = \max \left(0, \left\lfloor 20 - 20 \left( \frac{|E - N|}{1,000} \right)^{1/3} \right\rfloor \right) \]

What is your estimate $E$?

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
