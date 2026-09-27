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

The diagram below shows equilateral $\triangle ABC$ with side length $2$. Point $D$ lies on ray $\overrightarrow{BC}$ so that $CD = 4$. Points $E$ and $F$ lie on $\overline{AB}$ and $\overline{AC}$, respectively, so that $E$, $F$, and $D$ are collinear, and the area of $\triangle AEF$ is half of the area of $\triangle ABC$. Then $\tfrac{AE}{AF}=\tfrac m n$, where $m$ and $n$ are relatively prime positive integers. Find $m + 2n$.
[asy]
import math;
size(7cm);
pen dps = fontsize(10);
defaultpen(dps);
dotfactor=4;
pair A,B,C,D,E,F;
B=origin;
C=(2,0);
D=(6,0);
A=(1,sqrt(3));
E=(1/3,sqrt(3)/3);
F=extension(A,C,E,D);
draw(C--A--B--D,linewidth(1.1));
draw(E--D,linewidth(.7));
dot(A);
dot(B);
dot(C);
dot(D);
dot(E);
dot(F);
label("$A$",A,N);
label("$B$",B,S);
label("$C$",C,S);
label("$D$",D,S);
label("$E$",E,NW);
label("$F$",F,NE);
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
