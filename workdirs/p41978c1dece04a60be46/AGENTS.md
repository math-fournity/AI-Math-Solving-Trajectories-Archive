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

A high-security cyber-defense ring consists of 30 autonomous servers linked in a physical circle. Within this network, a specific number of servers have been upgraded with "Yale-OS," a perfectly reliable diagnostic firmware, while the remaining servers run a legacy OS that is prone to unpredictable, randomized data corruption.

An administrator initiates a network-wide audit. Each server is commanded to run a diagnostic check on its immediate neighbor to the right and report whether that neighbor is running Yale-OS. 

Servers running Yale-OS are programmed to always provide a 100% accurate report about their neighbor. However, servers running the legacy OS are malfunctioning and will provide a random "Yes" or "No" response regardless of their neighbor's actual firmware.

The administrator knows the exact total number of Yale-OS servers present in the ring. After collecting the list of "Yes/No" reports from all 30 positions, the administrator needs to be mathematically certain that they can identify the location of at least one specific Yale-OS server, regardless of how the legacy servers happen to answer or how the Yale-OS servers are distributed.

Find the smallest possible number of Yale-OS servers that must be in the ring to guarantee that at least one can be identified for certain.

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
