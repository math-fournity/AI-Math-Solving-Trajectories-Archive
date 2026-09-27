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

In a specialized laboratory, a digital containment vessel is programmed with a maximum capacity $N$. To determine the value of $N$, a technician uses a weighted random generator that selects an integer from the range $1 \leq N \leq 2019$. The probability of any specific integer $i$ being selected is directly proportional to its value, specifically $P(N=i) = \frac{i}{\sum_{k=1}^{2019} k}$.

Two engineers, Arianna and Brianna, are tasked with a sequential stress test on the vessel. Arianna begins the process by uploading the initial data packet labeled "1" into the system logs. From that point on, the engineers take turns adding a single new packet to the logs. On any given turn, the active engineer must choose any packet value $a$ already present in the logs and generate a new packet with a value of either $a+1$ or $2a$. However, two strict protocols must be followed:
1. Every packet value in the logs must be unique (no number can be written twice).
2. No packet value can ever exceed the pre-selected capacity $N$.

The logs are permanent and no data is ever deleted. The engineer who successfully uploads the packet with the exact value $N$ is awarded a commendation for completing the sequence.

Assuming both Arianna and Brianna employ optimal mathematical strategies to win the commendation, the probability that Brianna wins can be expressed as a simplified fraction $\frac{m}{n}$, where $m$ and $n$ are relatively prime positive integers.

Compute the value of $m + n$.

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
