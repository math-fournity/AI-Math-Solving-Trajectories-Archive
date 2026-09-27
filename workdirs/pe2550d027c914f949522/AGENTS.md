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

A specialized logistics firm is designing a regional distribution network that utilizes three primary hubs. These hubs form a triangular perimeter, where the straight-line distances between the hubs are denoted as $a, b,$ and $c$ kilometers. For each hub, there is a "direct access corridor" representing the shortest distance from that hub to the opposite side of the triangular territory; these distances are recorded as $h_a, h_b,$ and $h_c$ kilometers, respectively.

The firm's efficiency analysts are studying a specific "resource overhead" metric. This metric is defined by a sensitivity power $m$, where the total overhead of the access corridors is $\frac{1}{h_a^m} + \frac{1}{h_b^m} + \frac{1}{h_c^m}$ and the total overhead of the perimeter routes is $\frac{1}{a^m} + \frac{1}{b^m} + \frac{1}{c^m}$.

The firm seeks to identify the maximum possible stability constant $k(m)$ such that the inequality
\[ \frac{1}{h_a^m} + \frac{1}{h_b^m} + \frac{1}{h_c^m} \geq k(m) \left(\frac{1}{a^m} + \frac{1}{b^m} + \frac{1}{c^m}\right) \]
is guaranteed to hold for any possible triangular hub configuration.

Research indicates that once the sensitivity power $m$ exceeds a critical threshold of approximately $4.8188$, the value of this maximum constant $k(m)$ becomes fixed and does not change as $m$ increases further. 

Given this information, calculate the value of $k(2025)$.

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
