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

In a remote automated chemical plant, a sensor continuously monitors a high-pressure valve and records its state every second. The state is binary: either "C" (Closed) or "M" (Maintained). Because the valve's mechanical transitions are governed by a fair stochastic process, each second has an equal and independent 1/2 probability of being recorded as C or M.

The plant’s safety protocol involves monitoring the chronological sequence of these states. A specialized monitoring team, Team A, is assigned the signature sequence $CMMC$. A second team, Team B, is permitted to select two distinct signature sequences, each exactly three characters long, with the restriction that neither of their chosen sequences can be contained within Team A's sequence ($CMMC$).

The plant’s emergency alarm triggers as soon as any of the three selected sequences appears in the data stream. Team B "wins" the safety drill if Team A’s sequence appears first. If either of Team B’s two sequences appears before Team A’s sequence, Team A wins.

Assuming Team B selects their two sequences optimally to maximize the probability of Team A's sequence appearing first, calculate the probability that Team B wins. If this probability is expressed as an irreducible fraction $\frac{a}{b}$, find the value of $a + b$.

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
