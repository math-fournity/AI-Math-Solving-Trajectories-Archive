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

Let \( S \) be the set of integers modulo 2020. Suppose that \( a_{1}, a_{2}, \ldots, a_{2020}, b_{1}, b_{2}, \ldots, b_{2020}, c \) are arbitrary elements of \( S \). For any \( x_{1}, x_{2}, \ldots, x_{2020} \in S \), define \( f\left(x_{1}, x_{2}, \ldots, x_{2020}\right) \) to be the 2020-tuple whose \( i \)-th coordinate is \( x_{i-2}+a_{i} x_{2019}+b_{i} x_{2020}+c x_{i} \), where we set \( x_{-1}=x_{0}=0 \). Let \( m \) be the smallest positive integer such that, for some values of \( a_{1}, a_{2}, \ldots, a_{2020}, b_{1}, b_{2}, \ldots, b_{2020}, c \), we have, for all \( x_{1}, x_{2}, \ldots, x_{2020} \in S \), that \( f^{m}\left(x_{1}, x_{2}, \ldots, x_{2020}\right)=(0,0, \ldots, 0) \). For this value of \( m \), there are exactly \( n \) choices of the tuple \( \left(a_{1}, a_{2}, \ldots, a_{2020}, b_{1}, b_{2}, \ldots, b_{2020}, c\right) \) such that, for all \( x_{1}, x_{2}, \ldots, x_{2020} \in S, f^{m}\left(x_{1}, x_{2}, \ldots, x_{2020}\right)=(0,0, \ldots, 0) \). Compute \( 100m+n \).

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
