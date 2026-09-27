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

In the technologically advanced city-state of Quintis, there exists a digital infrastructure built upon a specialized data network $F$ containing exactly $5^{14}$ unique data packets. In this network, two packets $x$ and $y$ can be combined using an addition operation ($x+y$) or a subtraction operation ($x-y$), and each packet $x$ has a corresponding squared state $x^2$. 

A transmission protocol $f: F \rightarrow F$ is classified as "Synchronized" if it satisfies the following equilibrium condition for every possible pair of packets $x$ and $y$ in the network:
$$\left(f(x+y)+f(x)\right)\left(f(x-y)+f(x)\right)=f(y^2)-f(x^2).$$

The network administrators are investigating the redundancy of these protocols. They are looking for specific "Collision Packets"—individual data packets $z$ where two different Synchronized protocols, $h_1$ and $h_2$ (where $h_1 \neq h_2$), yield the exact same output value ($h_1(z) = h_2(z)$).

How many such data packets $z$ exist within the network $F$ for which at least two distinct Synchronized protocols produce identical outputs?

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
