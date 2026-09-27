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

In a specialized semiconductor manufacturing line, eight automated assembly stations are arranged in a strict linear sequence. Each station maintains an internal buffer containing exactly four processing chips. At the beginning of a production cycle, the first station receives a new chip from the raw material feeder.

Each station processes the incoming chip using the following logic: there is a 50% probability that the station passes the incoming chip directly to the next station in the sequence. Otherwise, the station swaps the incoming chip with one of the four chips currently in its internal buffer (each with an equal 25% chance of being selected) and passes the displaced chip to the next station. This continues until the eighth station receives a chip, processes it according to the same logic, and ejects the final displaced chip from the line.

In this specific cycle, a "Golden Chip" is introduced at the start of the line (received by the first station). It is known that the internal buffer of the fifth station already contains a second "Golden Chip." All other "Golden Chips" have been decommissioned and are not present in the line or the feeder. 

The probability that the eighth station receives a "Golden Chip" during this cycle is expressed as a reduced fraction $\frac{m}{n}$, where $m$ and $n$ are coprime positive integers. Calculate $100m + n$.

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
