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

A specialized digital vault stores a sequence of encrypted data packets, each assigned a unique weight represented by a positive integer. To prevent system instability, the vault’s security protocol imposes two strict constraints on any sequence of packets $a_{1}, \ldots, a_{L}$:

1.  **Capacity Limit:** The weight of every individual packet in the sequence must be less than or equal to $2^{2023}$.
2.  **Equilibrium Prevention:** No contiguous segment of the sequence $a_{i}, a_{i+1}, \ldots, a_{j}$ (where $1 \leqslant i \leqslant j \leqslant L$) can be "balanced." A segment is considered balanced if there exists any configuration of polarity—assigning each packet weight either a positive ($+1$) or negative ($-1$) charge—such that the resulting sum of the signed weights $s_{i} a_{i} + s_{i+1} a_{i+1} + \cdots + s_{j} a_{j}$ equals exactly zero.

What is the maximum possible number of packets $L$ that can be stored in a single sequence without violating these security protocols?

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
