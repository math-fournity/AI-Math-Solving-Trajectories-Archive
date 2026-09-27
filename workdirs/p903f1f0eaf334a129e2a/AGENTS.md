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

In the high-stakes world of quantum encryption, a security architect is designing "Validation Protocols," which are specific types of mathematical sequences represented by polynomials $f$ with integer coefficients. 

To ensure the integrity of a global server network, a protocol is deemed "Stable" only if it satisfies a specific divisibility constraint: for every sufficiently large server ID number $n$, the protocol’s output $f(n)$ must be a perfect divisor of the value $n^{n-1} - 1$.

Let $K$ represent the total number of unique stable protocols that can be designed under these parameters. 

Beyond simply counting these protocols, the architect needs to measure the "Stress Impact" of the system. The Stress Impact of a single protocol is defined as the absolute value of its output when the server ID is exactly 10, denoted as $|f(10)|$. Let $S$ be the sum of the Stress Impacts of all possible stable protocols identified.

Calculate the final system metric, which is the sum of the number of protocols and their total Stress Impact: $K + S$.

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
