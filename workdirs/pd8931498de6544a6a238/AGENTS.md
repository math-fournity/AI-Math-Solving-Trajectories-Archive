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

In a sprawling digital metropolis, a central server is tasked with arranging 6,051 specific data packets into a circular buffer for transmission. The packets consist of three distinct types: 2,017 identical "Crimson" packets, 2,017 identical "Jade" packets, and 2,017 identical "Azure" packets.

The security protocol of the buffer requires the following constraints for any valid sequence:
1. No Crimson packet can be placed immediately adjacent to a Jade packet.
2. No Azure packet can be placed immediately adjacent to another Azure packet.

The buffer slots are indexed, meaning that any rotation or reflection of a sequence that results in different packets at specific indices is counted as a unique configuration. Let $N$ be the total number of distinct ways to arrange these 6,051 packets while adhering to the security protocol.

A system architect determines that $N$ can be expressed in the form $p^m \cdot n$, where $p=2017$, $m$ is a non-negative integer, and $n$ is an integer not divisible by $p$. If $r$ is the remainder when $n$ is divided by $p$, calculate the value of $pm + r$.

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
