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

In the city of Arithmos, there is a central warehouse that stocks crates of specialized equipment. The weights of these crates are always positive integers. A certain logistics company, "The Set," manages a collection of these weights, denoted by $S$, which must adhere to two strict operational protocols:

1.  **Combination Rule:** If the company possesses crates of weight $x$ and weight $y$ (where $x$ and $y$ can be the same), they are capable of handling any shipment that results from combining them, meaning a crate of weight $x + y$ must also be in their collection $S$.
2.  **Efficiency Rule:** If the company is capable of handling a shipment of an even weight $2x$, they must also be capable of handling a shipment of exactly half that weight, $x$, to ensure logistical flexibility.

The city council is investigating "Universal Companies"—those whose collection $S$ is so robust that it eventually includes every possible positive integer weight $\mathbb{N}$.

The council focuses on two specific starter weights, $a$ and $b$. They want to determine how many pairs of integer weights $(a, b)$, with $1 \le a, b \le 50$, have the following property: if the company's collection $S$ contains both weights $a$ and $b$, then $S$ must be the set of all positive integers $\mathbb{N}$.

Calculate the total number of such pairs $(a, b)$.

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
