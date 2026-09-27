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

Let $A_1A_2A_3A_4A_5$ be a regular pentagon with side length 1. The sides of the pentagon are extended to form the 10-sided polygon shown in bold at right. Find the ratio of the area of quadrilateral $A_2A_5B_2B_5$ (shaded in the picture to the right) to the area of the entire 10-sided polygon.

[asy]
size(8cm);
defaultpen(fontsize(10pt)); 
pair A_2=(-0.4382971011,5.15554989475), B_4=(-2.1182971011,-0.0149584477027), B_5=(-4.8365942022,8.3510997895), A_3=(0.6,8.3510997895), B_1=(2.28,13.521608132), A_4=(3.96,8.3510997895), B_2=(9.3965942022,8.3510997895), A_5=(4.9982971011,5.15554989475), B_3=(6.6782971011,-0.0149584477027), A_1=(2.28,3.18059144705); 
filldraw(A_2--A_5--B_2--B_5--cycle,rgb(.8,.8,.8));
draw(B_1--A_4^^A_4--B_2^^B_2--A_5^^A_5--B_3^^B_3--A_1^^A_1--B_4^^B_4--A_2^^A_2--B_5^^B_5--A_3^^A_3--B_1,linewidth(1.2)); draw(A_1--A_2--A_3--A_4--A_5--cycle);

pair O = (A_1+A_2+A_3+A_4+A_5)/5;
label("$A_1$",A_1, 2dir(A_1-O));
label("$A_2$",A_2, 2dir(A_2-O));
label("$A_3$",A_3, 2dir(A_3-O));
label("$A_4$",A_4, 2dir(A_4-O));
label("$A_5$",A_5, 2dir(A_5-O));
label("$B_1$",B_1, 2dir(B_1-O));
label("$B_2$",B_2, 2dir(B_2-O));
label("$B_3$",B_3, 2dir(B_3-O));
label("$B_4$",B_4, 2dir(B_4-O));
label("$B_5$",B_5, 2dir(B_5-O));
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
