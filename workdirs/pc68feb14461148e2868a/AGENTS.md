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

In a remote desert, two observation outposts, Alpha and Bravo, are situated relative to a central command tower, Victor. The distance from Victor to Alpha is exactly $\sqrt{2}$ kilometers, and the distance from Victor to Bravo is exactly $\sqrt{3}$ kilometers. From the perspective of the command tower, the angle between the lines of sight to Alpha and Bravo is precisely $75^\circ$.

A specialized ecological preservation zone, shaped as a "lune"—a region bounded by two circular arcs meeting at endpoints Alpha and Bravo—is to be established. To avoid interfering with vital communication signals, the interior of this lune must not cross or touch the direct signal paths (the infinite lines) extending from the command tower through Alpha or from the tower through Bravo, except at the outposts themselves.

Environmental engineers wish to maximize the area of this preservation zone while adhering to these boundary constraints. Let $k$ represent the area of the largest possible lune that can be formed under these conditions.

Calculate the value of the expression:
\[ \dfrac {k}{(1+\sqrt{3})^2} \]

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
