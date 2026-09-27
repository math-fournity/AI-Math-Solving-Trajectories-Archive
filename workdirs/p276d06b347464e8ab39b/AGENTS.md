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

In a remote high-tech facility, an automated sorting system consists of a grid-based storage rack with a $3 \times 3$ layout of slots. Two rival logistics engineers, Grant and Stephen, are testing a new protocol for filling the rack with canisters. Grant uses blue canisters (X) and Stephen uses red canisters (O). 

The goal of the protocol is to be the first to occupy any $2 \times 2$ cluster of four adjacent slots with canisters of their own color. If the entire $3 \times 3$ grid is filled and no such $2 \times 2$ cluster of a single color exists, the trial is declared a system neutral tie. 

Grant is granted the first move. Stephen, due to a hardware glitch, places his red canisters in any of the remaining empty slots with equal probability (playing completely randomly). Grant, aware of this glitch, programs his movements with a perfect strategy to maximize his chances of winning.

If the probability that Grant successfully completes a $2 \times 2$ blue cluster is expressed as the irreducible fraction $\frac{m}{n}$, find the value of $m+n$.

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
