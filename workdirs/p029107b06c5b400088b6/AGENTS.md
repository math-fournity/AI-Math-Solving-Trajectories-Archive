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

In a bustling coastal region, several independent merchant guilds organized a trade exhibition. The event followed a strict "Round-Robin" protocol, where every guild engaged in a single collaborative trade venture with every other guild exactly once.

The success of these ventures was measured in Reputation Credits using a standard tri-level scale:
*   If a venture was highly profitable, the guild deemed the "lead partner" earned **3 credits**, while the other earned **0 credits**.
*   If a venture was moderately successful for both, it was declared a "balanced trade," and both guilds earned **1 credit** each.
*   The "maximum possible score" for a guild is defined as the number of credits they would have earned if they had won every single one of their trade ventures.

When the exhibition concluded, the records showed a "Sole Victor"—one specific guild that had earned strictly more total credits than any other individual guild. Curiously, this sole victor’s total credit count was strictly **less than 50%** of the maximum possible score a single participant could have achieved.

Based on this outcome, what is the minimum number of merchant guilds that could have participated in the exhibition?

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
