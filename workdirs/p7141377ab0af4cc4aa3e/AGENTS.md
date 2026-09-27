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

In a remote mining colony, two engineers, Dr. Aris and Commander Belen, are tasked with dividing 10 kilograms of rare isotope fuel rods, one rod at a time, over exactly 10 production cycles. Each cycle $i$ involves a single rod weighing exactly 1 kilogram.

The protocol for each cycle is as follows: 
1. Dr. Aris performs a precision cut on the $i$-th rod, dividing it into two portions of any size.
2. Commander Belen must then choose one of two operational modes: "Direct Claim" or "Deferred Claim."
   - If Belen chooses **Direct Claim**, she selects one of the two portions for her reactor first, and Aris takes the remaining portion.
   - If Belen chooses **Deferred Claim**, Aris selects a portion for his reactor first, and Belen takes whatever is left.

There is a strict regulatory constraint: Commander Belen must choose the **Deferred Claim** mode exactly once during the 10-cycle process. In the other 9 cycles, she must use the Direct Claim mode.

Both engineers are strictly competitive and will act with perfect mathematical strategy to maximize the total mass of isotope fuel they personally accumulate by the end of the 10th cycle. 

If the total mass of fuel Commander Belen ends up with is represented as a fraction $\frac{m}{n}$ in simplest form, find the value of $m + n$.

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
