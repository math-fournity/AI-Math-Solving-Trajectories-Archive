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

Cube $ABCDEFGH$, labeled as shown below, has edge length $1$ and is cut by a plane passing through vertex $D$ and the midpoints $M$ and $N$ of $\overline{AB}$ and $\overline{CG}$ respectively. The plane divides the cube into two solids. The volume of the larger of the two solids can be written in the form $\frac{p}{q}$, where $p$ and $q$ are relatively prime positive integers. Find $p+q$.
[asy]

draw((0,0)--(10,0)--(10,10)--(0,10)--cycle);
draw((0,10)--(4,13)--(14,13)--(10,10));
draw((10,0)--(14,3)--(14,13));
draw((0,0)--(4,3)--(4,13), dashed);
draw((4,3)--(14,3), dashed);
dot((0,0));
dot((0,10));
dot((10,10));
dot((10,0));
dot((4,3));
dot((14,3));
dot((14,13));
dot((4,13));
dot((14,8));
dot((5,0));
label("A", (0,0), SW);
label("B", (10,0), S);
label("C", (14,3), E);
label("D", (4,3), NW);
label("E", (0,10), W);
label("F", (10,10), SE);
label("G", (14,13), E);
label("H", (4,13), NW);
label("M", (5,0), S);
label("N", (14,8), E);
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
