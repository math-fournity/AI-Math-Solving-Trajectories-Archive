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

In a specialized laboratory, a set of automated quality-control tests is conducted on various batches of chemical compounds. There are $n$ distinct testing stations and $m$ types of chemical compounds. At each station, a technician ranks all $m$ compounds based on their reactivity levels. To determine which compounds move to the final production phase, the top $k$ compounds from each station's list are granted a "clearance token." The compounds that accumulate the highest total number of clearance tokens across all $n$ stations are declared the winners.

A set of rankings from all stations is called a "profile" $R$. For a specific compound $a$, a new profile $R'$ is considered "favorable to $a$" if, for every testing station, any compound ranked lower than $a$ in the original profile $R$ remains ranked lower than $a$ in the new profile $R'$.

The selection threshold $k$ is defined as "stable" if the following condition holds: for every possible profile $R$, if a compound $a$ is among the winners under $R$, it must also be among the winners for any profile $R'$ that is "favorable to $a$."

Let $k(n, m)$ represent the smallest integer $k$ (where $1 \leq k \leq m$) such that the threshold $k$ is stable for a given number of stations $n$ and compounds $m$.

Calculate the sum of the required thresholds for the following three scenarios:
$k(10, 20) + k(100, 10) + k(7, 13)$.

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
