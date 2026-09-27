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

Find the distance $\overline{CF}$ in the diagram below where $ABDE$ is a square and angles and lengths are as given:
[asy]
markscalefactor=0.15;
size(8cm);
pair A = (0,0);
pair B = (17,0);
pair E = (0,17);
pair D = (17,17);
pair F = (-120/17,225/17);
pair C = (17+120/17, 64/17);
draw(A--B--D--E--cycle^^E--F--A--cycle^^D--C--B--cycle);  
label("$A$", A, S);
label("$B$", B, S);
label("$C$", C, dir(0));
label("$D$", D, N);
label("$E$", E, N);
label("$F$", F, W);
label("$8$", (F+E)/2, NW);
label("$15$", (F+A)/2, SW);
label("$8$", (C+B)/2, SE);
label("$15$", (D+C)/2, NE);
draw(rightanglemark(E,F,A));
draw(rightanglemark(D,C,B));
[/asy]
The length $\overline{CF}$ is of the form $a\sqrt{b}$ for integers $a, b$ such that no integer square greater than $1$ divides $b$. What is $a + b$?

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
