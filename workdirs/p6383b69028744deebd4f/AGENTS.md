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

In a specialized digital ecosystem, there are exactly $p = 491$ unique data signals available. We consider a "Packet" of size $k$ to be an ordered sequence of $k$ signals, where each signal is represented by an integer from $0$ to $490$. Let $S$ be the set of all possible Packets of size $k$.

The "Signal Resonance" between two Packets $u = (a_1, \dots, a_k)$ and $v = (b_1, \dots, b_k)$ is calculated as the sum of the products of their corresponding signals, taken modulo $491$: 
$$\text{Resonance}(u, v) = (a_1b_1 + a_2b_2 + \dots + a_kb_k) \pmod{491}$$

A data transformation function $f: S \to S$ is classified as "Harmonic" if it preserves the Signal Resonance for every possible pair of Packets. That is, for all $u, v \in S$, the Resonance of $f(u)$ and $f(v)$ must be identical to the Resonance of $u$ and $v$.

Let $m(k)$ denote the total number of distinct Harmonic functions that can exist for Packets of size $k$.

Your task is to calculate the sum of the number of Harmonic functions for all Packet sizes from $k=1$ up to $k=491$. Specifically, find the remainder when the following sum is divided by $488$:
$$m(1) + m(2) + m(3) + \dots + m(491)$$

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
