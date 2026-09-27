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

In a specialized logistics competition, a head dispatcher named Bob and an operations manager named Alice are tasked with organizing inventory layouts. There are 2011 distinct storage warehouses, each featuring a square floor plan of $2011 \times 2011$ designated storage slots. Bob is assigned 1 warehouse, while Alice is assigned the remaining 2010 warehouses.

They are required to populate every slot in their respective warehouses with the unique identification tags $1, 2, \ldots, 2011^2$. The tags must be arranged such that the values strictly increase from left-to-right across every row and from top-to-bottom down every column. Alice must ensure that no two of her 2010 warehouses have identical inventory layouts.

Once Alice has finalized her layouts, Bob is permitted to inspect all of them. He may then modify his own warehouse layout by performing a series of "legal swaps." A swap consists of exchanging the positions of two tags in his grid, provided that after the exchange, the strictly increasing order across rows and down columns is preserved. 

After Bob finished his adjustments, a single warehouse is randomly selected from Alice’s 2010 facilities. Bob is declared the winner if there exist two specific identification tags that occupy the same column in the selected Alice’s warehouse but are located in the same row within Bob's warehouse. If no such pair exists, Alice wins.

Assuming Bob chooses his initial layout optimally to minimize the effort required after seeing Alice's work, what is the maximum number of swaps Bob might need to perform to guarantee he wins regardless of which of Alice's warehouses is chosen?

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
