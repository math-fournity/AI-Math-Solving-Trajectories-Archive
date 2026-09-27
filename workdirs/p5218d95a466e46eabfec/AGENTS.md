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

In a remote industrial refinery, a Logistics Manager and an Auditor are engaged in a mandatory resource allocation protocol involving 1001 liters of a rare chemical catalyst.

The process begins with the Manager distributing the entire 1001 liters across three primary storage vats. Once the Auditor observes the exact volume in each of these three vats, the Auditor must declare a target density value, $N$, which can be any integer from 1 to 1001.

To fulfill the protocol, the Manager must then extract a portion of the catalyst from the three primary vats and transfer it into a fourth emergency containment tank. The Manager must continue this transfer until at least one of the four vats (the three primary vats or the emergency tank) contains exactly $N$ liters.

The Auditor’s bonus for the quarter is calculated as the exact number of liters that the Manager was forced to move into the fourth tank to satisfy the condition. The Auditor aims to select an $N$ that guarantees the largest possible bonus, while the Manager distributes the initial 1001 liters in a way that minimizes this inevitable payout.

What is the maximum number of liters the Auditor can be guaranteed to receive, regardless of the Manager's initial distribution strategy?

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
