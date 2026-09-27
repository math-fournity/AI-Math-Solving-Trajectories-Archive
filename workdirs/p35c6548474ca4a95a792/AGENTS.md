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

In a remote industrial facility, two automated power systems, Unit P and Unit I, exchange energy credits during a series of operational cycles. At the start of each cycle, an internal sensor generates a random binary signal. If the signal is "High," Unit P receives credits from Unit I. If the signal is "Low," Unit I receives credits from Unit P.

The amount of credits transferred increases exponentially each cycle: in the first cycle, the transfer is exactly 1 credit; in the second cycle, it is 2 credits; in the third, it is 4 credits; and so on, with the transfer amount doubling every cycle.

Prior to the first cycle, Unit P’s credit balance was represented by a single-digit integer ($1 \le P_0 \le 9$), while Unit I’s balance was a four-digit integer ($1000 \le I_0 \le 9999$). The protocols dictate that neither unit can ever have a negative balance; a transfer only occurs if the loser has sufficient credits to pay the full amount for that cycle.

After a specific number of cycles, the session ended. At that moment, Unit I was left with a two-digit credit balance ($10 \le I_{final} \le 99$), and Unit P had accumulated a three-digit credit balance ($100 \le P_{final} \le 999$). 

Based on these final balances, what is the minimum number of cycles that Unit P could have won?

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
