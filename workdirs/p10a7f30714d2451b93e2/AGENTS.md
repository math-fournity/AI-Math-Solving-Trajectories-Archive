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

A specialized logistics company is tasked with distributing 300 identical high-security data servers between two rival tech firms, Alpha and Beta. The distribution protocol is governed by a strict sequential procedure:

An engineer from Firm Alpha initiates a round by selecting a batch of servers (any number from 1 up to the total remaining) and placing them into a secure shipping container. Once the container is packed, a representative from Firm Beta chooses which firm—either Alpha or Beta—will receive that specific container. This process repeats in successive rounds.

The distribution concludes immediately upon the occurrence of either of the following events:
1. All 300 servers have been assigned to containers and distributed.
2. One of the two firms receives its 11th shipping container. In this specific scenario, any servers remaining in the warehouse that have not yet been placed in a container are immediately forfeited and delivered to the other firm.

Firm Alpha wishes to maximize the total number of servers it receives, while Firm Beta wishes to minimize Alpha's total. Assuming both firms act with perfect mathematical strategy, what is the maximum number of servers that Firm Alpha can guarantee it will acquire?

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
