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

A [i]calendar[/i] is a (finite) rectangular grid. A calendar is [i]valid[/i] if it satisfies the following conditions:

(i) Each square of the calendar is colored white or red, and there are exactly 10 red squares.

(ii) Suppose that there are $N$ columns of squares in the calendar. Then if we fill in the numbers $1,2,\ldots$ from the top row to the bottom row, and within each row from left to right, there do not exist $N$ consecutive numbers such that the squares they are in are all white.

(iii) Suppose that there are $M$ rows of squares in the calendar. Then if we fill in the numbers $1,2,\ldots$ from the left-most column to the right-most column, and within each column from bottom to top, there do not exist $M$ consecutive numbers such that the squares they are in are all white. In other words, if we rotate the calendar clockwise by $90^{\circ}$, the resulting calendar still satisfies (ii).

How many different kinds of valid calendars are there? 

(Remark: During the actual exam, the contestants were confused about what counts as different calendars. So although this was not in the actual exam, I would like to specify that two calendars are considered different if they have different side lengths or if the $10$ red squares are at different locations.)

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
