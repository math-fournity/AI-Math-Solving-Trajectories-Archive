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

In a specialized logistics center, a security firm monitors four different server hubs labeled $H_1, H_2, H_3,$ and $H_4$. Due to intelligence reports, it is known that exactly one of these hubs contains a high-value encrypted drive, while the others contain decoy data. The probability that the drive is located in hub $H_n$ is exactly $\frac{n}{10}$ for $n \in \{1, 2, 3, 4\}$.

A technician is asked to perform a security test. First, the technician must designate one of the four hubs as their "primary target." Immediately after this designation, an automated system—unaware of the drive's location—randomly selects one of the three remaining hubs and broadcasts its contents to the technician (revealing either the drive or decoy data). 

Following this reveal, the technician is allowed to make a final, definitive choice by selecting any one of the four hubs (they may keep their original target or switch to any other hub, including the one that was just revealed). The technician wins if their final selection contains the encrypted drive.

Suppose the technician follows a strategy that maximizes their probability of winning. Let this maximum probability be expressed as the simplified fraction $\frac{m}{n}$, where $m$ and $n$ are relatively prime positive integers.

Compute the value of $100m + n$.

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
