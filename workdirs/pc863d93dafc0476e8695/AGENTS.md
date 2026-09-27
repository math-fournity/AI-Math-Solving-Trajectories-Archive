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

There are three types of piece shown as below. Today Alice wants to cover a $100 \times 101$ board with these pieces without gaps and overlaps. Determine the minimum number of $1\times 1$ pieces should be used to cover the whole board and not exceed the board. (There are an infinite number of these three types of pieces.)
[asy]
size(9cm,0);
defaultpen(fontsize(12pt));
draw((9,10) -- (59,10) -- (59,60) -- (9,60) -- cycle);
draw((59,10) -- (109,10) -- (109,60) -- (59,60) -- cycle);
draw((9,60) -- (59,60) -- (59,110) -- (9,110) -- cycle);
draw((9,110) -- (59,110) -- (59,160) -- (9,160) -- cycle);
draw((109,10) -- (159,10) -- (159,60) -- (109,60) -- cycle);
draw((180,11) -- (230,11) -- (230,61) -- (180,61) -- cycle);
draw((180,61) -- (230,61) -- (230,111) -- (180,111) -- cycle);
draw((230,11) -- (280,11) -- (280,61) -- (230,61) -- cycle);
draw((230,61) -- (280,61) -- (280,111) -- (230,111) -- cycle);
draw((280,11) -- (330,11) -- (330,61) -- (280,61) -- cycle);
draw((280,61) -- (330,61) -- (330,111) -- (280,111) -- cycle);
draw((330,11) -- (380,11) -- (380,61) -- (330,61) -- cycle);
draw((330,61) -- (380,61) -- (380,111) -- (330,111) -- cycle);
draw((401,11) -- (451,11) -- (451,61) -- (401,61) -- cycle);
[/asy]
[i]Proposed by amano_hina[/i]

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
