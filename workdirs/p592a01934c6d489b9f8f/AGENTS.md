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

A network security engineer is designing a sequence of $n$ data packets to test a firewall's resilience. The firewall has a "Stability Buffer" that starts at zero. If the buffer ever reaches $+10$ (the Upper Critical Limit) or $-10$ (the Lower Critical Limit), the system crashes.

The engineer prepares an ordered list of $n$ commands. Each command $i$ (where $1 \le i \le n$) is a specific packet type:
- Type A: Increases the buffer by 5 units.
- Type B: Decreases the buffer by 5 units.

An automated auditor chooses a sampling interval $m$ (a positive integer). The firewall then processes only those packets whose position in the list is a multiple of $m$ (i.e., packet $m$, packet $2m$, packet $3m$, etc.), in their original relative order. To pass the security audit, the cumulative sum of the buffer adjustments for any chosen $m$ must never hit or exceed the limits ($+10$ or $-10$) at any point during the processing of that subsequence.

Find the largest integer $n$ for which the engineer can create a fixed list of $n$ commands such that the firewall passes the audit for every possible choice of $m \in \{1, 2, 3, \dots, n\}$.

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
