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

In a specialized logistics network, cargo shipments are tracked using two-component data packets $(X, Y)$, where $X$ represents the "Standard Load" and $Y$ represents the "Variable Load." When two shipments are merged using a "Synthesized Protocol," the resulting data packet is calculated by the following rule:
Merging shipment $(a, b)$ with shipment $(c, d)$ results in a new packet $(ac + bd, ad + bc)$.

A logistics supervisor is processing a sequence of six shipments. Each shipment $k$ (where $k$ ranges from 1 to 6) has a fixed Standard Load equal to its sequence number $k$, and an unknown integer Variable Load $a_k$. The shipments are merged sequentially as follows:

1. The first shipment $(1, a_1)$ is merged with the second shipment $(2, a_2)$.
2. The result is then merged with the third shipment $(3, a_3)$.
3. This process continues until the result of the first five shipments is merged with the sixth shipment $(6, a_6)$.

After all five merge operations are completed, the final resulting data packet is measured to be $(350, 280)$.

Find the total number of distinct ordered six-tuples of integers $(a_1, a_2, a_3, a_4, a_5, a_6)$ that would result in this specific final data packet.

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
