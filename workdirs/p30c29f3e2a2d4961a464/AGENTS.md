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

In a remote digital archives facility, there is a single long corridor containing a row of 2012 data storage slots, indexed sequentially from 1 to 2012. Today, 2012 unique data packets are scheduled to be uploaded into these slots, one packet at a time, until every slot is occupied.

The uploading protocol follows a specific spatial safety logic:
1. The very first packet is assigned to a slot chosen uniformly at random from all 2012 available slots.
2. For every subsequent packet, the system identifies all currently empty slots that maximize the minimum distance to any slot already containing a packet. The system then selects one of these "safest" slots uniformly at random for the current upload.

This process continues until all 2012 packets are stored. Engineers are interested in the scenario where the very last packet (the 2012th) has no choice but to be stored in slot 1 because it is the only remaining option that satisfies the safety protocol.

Determine the probability that the 2012th packet must be placed in slot 1. If this probability is expressed as an irreducible fraction $\frac{a}{b}$, calculate the final value $a + b$.

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
