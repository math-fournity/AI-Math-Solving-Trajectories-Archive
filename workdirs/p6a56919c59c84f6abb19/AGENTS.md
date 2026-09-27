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

The diagram below shows a $1\times2\times10$ duct with $2\times2\times2$ cubes attached to each end. The resulting object is empty, but the entire surface is solid sheet metal. A spider walks along the inside of the duct between the two marked corners. There are positive integers $m$ and $n$ so that the shortest path the spider could take has length $\sqrt{m}+\sqrt{n}$. Find $m + n$.

[asy]
size(150);
defaultpen(linewidth(1));
draw(origin--(43,0)--(61,20)--(18,20)--cycle--(0,-43)--(43,-43)--(43,0)^^(43,-43)--(61,-23)--(61,20));
draw((43,-43)--(133,57)--(90,57)--extension((90,57),(0,-43),(61,20),(18,20)));
draw((0,-43)--(0,-65)--(43,-65)--(43,-43)^^(43,-65)--(133,35)--(133,57));
draw((133,35)--(133,5)--(119.5,-10)--(119.5,20)^^(119.5,-10)--extension((119.5,-10),(100,-10),(43,-65),(133,35)));
dot(origin^^(133,5));
[/asy]

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
