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

In the planetary logistics hub of Novis, cargo manifests are processed using a standardized "Base-20 Shift" protocol. Every shipment ID, represented by a positive integer $k$, is transformed into a "Priority Code" $k^{\prime}$ through a specific digit-swapping method: if $k$ is divided by 20 to get a quotient $a$ and a remainder $b$ (where $0 \le b < 20$), the Priority Code $k^{\prime}$ is calculated as $20b + a$.

A cargo controller is tracking automated relay sequences. For any starting shipment ID $n$, a sequence $d_1, d_2, d_3, \ldots$ is generated such that $d_1 = n$, and every subsequent ID $d_{i+1}$ is the Priority Code of the previous ID $d_i$.

The controller is interested in all shipment IDs $n$ in the range $\{1, 2, \ldots, 100,000\}$ that are "Origin-Linked," meaning the sequence starting with $n$ eventually includes the value 1.

Find the total number of Origin-Linked shipment IDs in this range.

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
