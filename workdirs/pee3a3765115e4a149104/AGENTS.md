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

A digital library archives a massive collection of 100,000 rare manuscripts, indexed sequentially from Document 0 to Document 99,999. To manage the collection, the chief librarian organizes the manuscripts into 1,000 distinct storage bins, labeled Bin $i$ where $i$ ranges from 0 to 999. Each Bin $i$ contains exactly 100 documents: specifically, those with index numbers $n$ such that $100i \leq n < 100(i+1)$. For instance, Bin 4 stores all documents indexed from 400 through 499.

A security audit is conducted to identify "Perfect Bins." A bin is classified as a Perfect Bin if at least one document stored within it has an index number $n$ that is a perfect square (an integer $k$ such that $k^2 = n$).

Based on this organizational system, exactly how many of the 1,000 bins ($S_0, S_1, S_2, \ldots, S_{999}$) are not Perfect Bins?

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
