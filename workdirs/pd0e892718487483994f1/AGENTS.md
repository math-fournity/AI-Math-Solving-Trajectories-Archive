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

Right triangle $ABC$ has its right angle at $A$. A semicircle with center $O$ is inscribed inside triangle $ABC$ with the diameter along $AB$. Let $D$ be the point where the semicircle is tangent to $BC$. If $AD=4$ and $CO=5$, find $\cos\angle{ABC}$.

[asy]
import olympiad;

pair A, B, C, D, O;
A = (1,0);
B = origin;
C = (1,1);
O = incenter(C, B, (1,-1));
draw(A--B--C--cycle);
dot(O);
draw(arc(O, 0.41421356237,0,180));
D = O+0.41421356237*dir(135);
label("$A$",A,SE);
label("$B$",B,SW);
label("$C$",C,NE);
label("$D$",D,NW);
label("$O$",O,S);
[/asy]

$\text{(A) }\frac{\sqrt{5}}{4}\qquad\text{(B) }\frac{3}{5}\qquad\text{(C) }\frac{12}{25}\qquad\text{(D) }\frac{4}{5}\qquad\text{(E) }\frac{2\sqrt{5}}{5}$

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
