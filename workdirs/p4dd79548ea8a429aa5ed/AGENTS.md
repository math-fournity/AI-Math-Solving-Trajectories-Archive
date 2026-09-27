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

Let $\triangle ABC$ be an acute triangle with circumcenter $O$ and centroid $G$. Let $X$ be the intersection of the line tangent to the circumcircle of $\triangle ABC$ at $A$ and the line perpendicular to $GO$ at $G$. Let $Y$ be the intersection of lines $XG$ and $BC$. Given that the measures of $\angle ABC, \angle BCA, $ and $\angle XOY$ are in the ratio $13 : 2 : 17, $ the degree measure of $\angle BAC$ can be written as $\frac{m}{n},$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$.
[asy]
unitsize(5mm);
pair A,B,C,X,G,O,Y;
A = (2,8);
B = (0,0);
C = (15,0);
dot(A,5+black); dot(B,5+black); dot(C,5+black);
draw(A--B--C--A,linewidth(1.3));
draw(circumcircle(A,B,C));
O = circumcenter(A,B,C);
G = (A+B+C)/3;
dot(O,5+black); dot(G,5+black);
pair D = bisectorpoint(O,2*A-O);
pair E = bisectorpoint(O,2*G-O);
draw(A+(A-D)*6--intersectionpoint(G--G+(E-G)*15,A+(A-D)--A+(D-A)*10));
draw(intersectionpoint(G--G+(G-E)*10,B--C)--intersectionpoint(G--G+(E-G)*15,A+(A-D)--A+(D-A)*10));
X = intersectionpoint(G--G+(E-G)*15,A+(A-D)--A+(D-A)*10);
Y = intersectionpoint(G--G+(G-E)*10,B--C);
dot(Y,5+black);
dot(X,5+black);
label("$A$",A,NW);
label("$B$",B,SW);
label("$C$",C,SE);
label("$O$",O,ESE);
label("$G$",G,W);
label("$X$",X,dir(0));
label("$Y$",Y,NW);
draw(O--G--O--X--O--Y);
markscalefactor = 0.07;
draw(rightanglemark(X,G,O));
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
